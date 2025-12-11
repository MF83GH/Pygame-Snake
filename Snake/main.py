import pygame
import random

pygame.init()
font = pygame.font.Font(None, 30)
fontBig = pygame.font.Font(None, 90)
screen = pygame.display.set_mode((800,600))

clock = pygame.time.Clock()
game_speed = 12
counter = 0

running = True
game_over = False
game_start = False

moving = False
direction_changed = False

score = 0

snake = [[100, 300], [80, 300], [60, 300]]
food = [random.randint(0, 29) * 20, random.randint(0, 19) * 20]


direction = "RIGHT"

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            # FIRST KEY PRESS

            if (moving == False and game_over == False and game_start == True 
            and event.key == pygame.K_UP and direction != "DOWN"):
                direction = "UP"
                moving = True
            elif (moving == False and game_over == False and game_start == True 
            and event.key == pygame.K_DOWN and direction != "UP"):
                direction = "DOWN"
                moving = True
            elif (moving == False and game_over == False and game_start == True 
            and event.key == pygame.K_RIGHT and direction != "LEFT"):
                direction = "RIGHT"
                moving = True
            

            # KEY CONTROLS
           
            if event.key == pygame.K_UP and direction != "DOWN" and direction_changed == False:
                direction = "UP"
                direction_changed = True
            elif event.key == pygame.K_DOWN and direction != "UP" and direction_changed == False:
                direction = "DOWN"
                direction_changed = True
            elif event.key == pygame.K_LEFT and direction != "RIGHT" and direction_changed == False:
                direction = "LEFT"
                direction_changed = True
            elif event.key == pygame.K_RIGHT and direction != "LEFT" and direction_changed == False:
                direction = "RIGHT"
                direction_changed = True

            if event.key == pygame.K_r and game_over == True:
                game_over = False
                direction = "RIGHT"
                game_speed = 12
                counter = 0
                score = 0
                snake = [[100, 300], [80, 300], [60, 300]]
                food = [random.randint(0, 39) * 20, random.randint(0, 29) * 20]

            if event.key == pygame.K_ESCAPE:
                game_over = False
                game_start = False
                direction = "RIGHT"
                game_speed = 12
                counter = 0
                score = 0
                snake = [[100, 300], [80, 300], [60, 300]]
                food = [random.randint(0, 39) * 20, random.randint(0, 29) * 20]


            if event.key == pygame.K_SPACE:
                game_start = True
    

    if game_start == False:
        
        # TITLE SCREEN
        
        moving = False
        screen.fill("white")

        startText = font.render("Press (space) to start game", True, "black")
        snakeText = fontBig.render("SNAKE", True, "black")
        screen.blit(startText, [266.5, 450])
        screen.blit(snakeText, [287.5, 200])

 
    else: 
        
        # GAME SCREEN -> SNAKE

        screen.fill("black")

        head_x = snake[0][0]  
        head_y = snake[0][1] 


        if direction == "UP":
            new_head = [head_x, head_y - 20]
        elif direction == "DOWN":
            new_head = [head_x, head_y + 20]
        elif direction == "LEFT":
            new_head = [head_x - 20, head_y]
        elif direction == "RIGHT":
            new_head = [head_x + 20, head_y]

        
        if snake[0][0] < 0 or snake[0][0] > 781:
            game_over = True
        elif snake[0][1] < 0 or snake[0][1] > 581: 
            game_over = True
        elif snake[0] in snake[1:]: 
            game_over = True 
    

       # APPLE 

        if moving:
            if snake[0] == food:
                food = [random.randint(0, 29) * 20, random.randint(0, 19) * 20]
                score += 1
                counter += 1
            else: 
                snake.pop()

            snake.insert(0, new_head)

            direction_changed = False

        for segment in snake:
            pygame.draw.rect(screen, "green", [segment[0], segment[1], 20, 20])

        pygame.draw.rect(screen, "red", [food[0], food[1], 20, 20])


        # SCORE DISPLAY
        
        text_surface = font.render(f"Score: {score}", True, "white")
        screen.blit(text_surface, [360.5, 20])


    if game_over == True:
        
        # GAME OVER SCREEN
        
        moving = False
        screen.fill("black")
        
        scoreText = font.render(f"Your score: {score}", True, "white")
        restartText = font.render("Press (r) to play again", True, "white")
        homeText = font.render("Press (esc) to exit to title screen", True, "white")

        screen.blit(scoreText, [337, 200])
        screen.blit(restartText, [293.5, 360])
        screen.blit(homeText, [239.5, 420])

    
    # SPEED INCREASE

    if game_speed < 22:
        if counter == 5:
            game_speed += 1
            counter = 0
    else:
        pass


    pygame.display.flip()

    clock.tick(game_speed)

pygame.quit()
