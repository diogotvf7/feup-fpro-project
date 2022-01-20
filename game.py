import pygame
import math
import imps as ip
import os


screen_size = (600, 600)
ss_size = 32

pygame.init()

screen = pygame.display.set_mode(screen_size)

menu = pygame.image.load(os.path.abspath(os.getcwd()) + '\\Images\\Menu.jpg')
button = pygame.image.load(os.path.abspath(os.getcwd()) + '\\Images\\Button.jpg')
button.set_colorkey(ip.color['black'])

player1 = pygame.image.load(os.path.abspath(os.getcwd()) + '\\Images\\ss.png')
player1.set_colorkey(ip.color['black'])

player2 = pygame.image.load(os.path.abspath(os.getcwd()) + '\\Images\\ss.png')
player2.set_colorkey(ip.color['black'])

running, in_menu, in_game, end = True, True, False, False



clock = pygame.time.Clock()

while running:

    y_player1 = screen_size[1] - ss_size - 10
    score_player1 = 0

    y_player2 = screen_size[1] - ss_size - 10
    score_player2 = 0

    up_key = down_key = w_key = s_key = enter_key = False
    pos = (0, 0)
    i = 0
    j = 0
    time = 0
    time_limit = 30 # seconds

    while in_menu:

        for ev in pygame.event.get():

            if ev.type == pygame.QUIT: #Exit
                running = False
                in_menu = False

            if ev.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

        if  275 <= pos[0] <= 480 and 450 <= pos[1] <= 515:

            for i in range(3, -1, -1):
                
                screen.blit(menu, (0, 0))
                number = pygame.image.load(ip.numbers[i])
                number.set_colorkey(ip.color['black'])
                screen.blit(number, (275, 450))
                pygame.display.flip() 
                pygame.time.delay(750)

            
            in_game = True
            in_menu = False

        screen.blit(menu, (0, 0))
        screen.blit(button, (275, 450))

        pygame.display.flip()   


    while in_game:  # gameloop

        frame_left = ip.visible(ip.level_left, 50, int(i))
        frame_right = ip.visible(ip.level_right, 50, int(j))

    #   _____________________________1._____________________________    #
    #                              KEYPAD                               #

        for ev in pygame.event.get():

            if ev.type == pygame.QUIT: #Exit
                running = False
                in_game = False

            elif ev.type == pygame.KEYDOWN: #Press Events 
                if ev.key == pygame.K_UP:
                    up_key = True
                elif ev.key == pygame.K_DOWN:
                    down_key = True
                if ev.key == pygame.K_w:
                    w_key = True
                elif ev.key == pygame.K_s:
                    s_key = True

            elif ev.type == pygame.KEYUP: #Release Events
                if ev.key == pygame.K_UP:
                    up_key = False
                elif ev.key == pygame.K_DOWN:
                    down_key = False
                if ev.key == pygame.K_w:
                    w_key = False
                elif ev.key == pygame.K_s:
                    s_key = False

    #   _____________________________2._____________________________    #
    #   ____________________________________________________________    #
    #                             PLAYER 1                              #

        if w_key: # Up
            y_player1 -= 0.3

        elif s_key and y_player1 < screen_size[1] - ss_size - 10: # Down
            y_player1 += 0.3

        if y_player1 <= -ss_size: #Score
            score_player1 += 1
            y_player1 = screen_size[1] - ss_size - 10

        if ip.contact(frame_right, frame_left, y_player1, (16, 19)): # Lose

            y_player1 = screen_size[1] - ss_size - 10

        score_player1_show = pygame.image.load(ip.numbers[score_player1])

    #   ____________________________________________________________    #
    #                             PLAYER 2                              #

        if up_key: # Up
            y_player2 -= 0.3

        elif down_key and y_player2 < screen_size[1] - ss_size - 10: # Down
            y_player2 += 0.3

        if y_player2 <= -ss_size: #Score
            score_player2 += 1
            y_player2 = screen_size[1] - ss_size - 10

        if ip.contact(frame_right, frame_left, y_player2, (33, 36)): # Lose

            y_player2 = screen_size[1] - ss_size - 10

        score_player2_show = pygame.image.load(ip.numbers[score_player2])

    #   ____________________________________________________________    #
    #                              GENERAL                              #

        if time >= time_limit * 1000:

            end = True
            in_game = False

    #   _____________________________3._____________________________    #
    #                          SCREEN DISPLAY                           #

        screen.fill(ip.color['black'])
        screen.blit(player1, (screen_size[0] / 3 - 5, y_player1))
        screen.blit(player2, (screen_size[0] * 2 / 3, y_player2))
        screen.blit(score_player1_show, (20, 520))
        screen.blit(score_player2_show, (516, 520))

        for row in range(0, len(frame_left)):
            for col in range(0, len(frame_left[row])):
                if frame_left[row][col] == '1':
                    pygame.draw.rect(screen, pygame.Color('yellow'), (col*12, row*12, 12, 12))
        
        for row in range(0, len(frame_right)):
            for col in range(0, len(frame_right[row])):
                if frame_right[row][col] == '1':
                    pygame.draw.rect(screen, pygame.Color('yellow'), (col*12, row*12, 12, 12))

        for t in range(math.ceil(time_limit - time // 1000)):

            pygame.draw.rect(screen, pygame.Color('white'), (312, 600 - t * 10, 10, 10))

        i += 0.015
        i %= 150
        j -= 0.015
        j %= 150
        time += clock.tick()

        pygame.display.flip()

    while end:

        for ev in pygame.event.get():

            if ev.type == pygame.QUIT: #Exit
                running = False
                end = False
            
            elif ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_RETURN: 
                    enter_key = True
            
            elif ev.type == pygame.KEYUP:
                if ev.key == pygame.K_RETURN: 
                    enter_key = False

        if enter_key:        
            end = False
            in_game = True

        if score_player1 == score_player2:

            bg = pygame.image.load(os.path.abspath(os.getcwd()) + '\\Images\\draw.jpg')
            screen.blit(bg, (0, 0))

        else:

            bg = pygame.image.load(os.path.abspath(os.getcwd()) + '\\Images\\the_winner_is.jpg')

            if score_player1 > score_player2:

                winner = pygame.image.load(os.path.abspath(os.getcwd()) + '\\Images\\Player 1.jpg')

            elif score_player2 > score_player1:

                winner = pygame.image.load(os.path.abspath(os.getcwd()) + '\\Images\\Player 2.jpg')

            winner.set_colorkey(ip.color['black'])
            screen.blit(bg, (0, 0))
            screen.blit(winner, (165, 355))
        
        pygame.display.flip()

pygame.quit()

    