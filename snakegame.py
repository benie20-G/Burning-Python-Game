import pygame
import colorsnake
from random import randint

pygame.init()


WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800

screen = pygame.display.set_mode([WINDOW_WIDTH,WINDOW_HEIGHT])
segment_size =10
pygame.display.set_caption('Snake game')

clock = pygame.time.Clock()

def set_food(snake_positions):
    x=randint(0,39) * segment_size
    y= randint(2,41) * segment_size
    if x not in(0, WINDOW_WIDTH ) and y not in(20, WINDOW_HEIGHT ):
        food_position=(x,y)
    if food_position not in  snake_positions :
        return food_position 


def draw(snake_positions,food_position):
    pygame.draw.rect(screen,colorsnake.FOOD,[food_position,(segment_size,segment_size)])
    for postion in snake_positions:
        if postion == snake_positions[0]:
            pygame.draw.rect(screen,colorsnake.head,[postion,(segment_size,segment_size)])
        else:
            pygame.draw.rect(screen,colorsnake.snake,[postion,(segment_size,segment_size)])

def move_snake(snake_positions, direction):
    head_x_position, head_y_position = snake_positions[0]

    if direction == "Left":
        new_head_position = (head_x_position - segment_size, head_y_position)
    elif direction == "Right":
        new_head_position = (head_x_position + segment_size, head_y_position)
    elif direction == "Down":
        new_head_position = (head_x_position, head_y_position + segment_size)
    elif direction == "Up":
        new_head_position = (head_x_position, head_y_position - segment_size)

    snake_positions.insert(0, new_head_position)
    del snake_positions[-1]

KEY_MAP ={
    273:'Up',
    274:'Down',
    275:'Right',
    276:'Left'
    }

def on_key_press(direction1, direction2):
    all_directions = ("Up", "Down", "Left", "Right")
    opposites = ({"Up", "Down"}, {"Left", "Right"})

    if (direction2 in all_directions and {direction1, direction2} not in opposites):
        return direction2
    return direction1


def check_collisions(snake_positions):
    head_x_position, head_y_position = snake_positions[0]

    return (
        head_x_position in (-10, WINDOW_WIDTH)
        or head_y_position in (10, WINDOW_HEIGHT
        )
        or (head_x_position, head_y_position) in snake_positions[1:]
    )

def check_food_collision(snake_positions, food_position):
    if snake_positions[0] == food_position:
        snake_positions.append(snake_positions[-1])

        return True



def playgame():
    score = 0
    snake_positions =[(100,100),(80,100),(60,100),(40,100)]
    food_position =set_food(snake_positions)
    current_direction ='Right'
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = 'Left'
                    current_direction = on_key_press(current_direction,direction)
                elif event.key == pygame.K_RIGHT:
                    direction ='Right'
                    current_direction = on_key_press(current_direction,direction)
                elif event.key == pygame.K_UP:
                     direction = 'Up'
                     current_direction = on_key_press(current_direction,direction)
                elif event.key == pygame.K_DOWN:
                    direction ='Down'
                    current_direction = on_key_press(current_direction,direction)
                    # current_direction = on_key_press(event, current_direction)


        screen.fill(colorsnake.Background)
        draw(snake_positions,food_position)
        font = pygame.font.Font(None,30)
        text = font.render(f"score is {score}",True,colorsnake.Text)
        screen.blit(text,(700,10))
        
        move_snake(snake_positions,current_direction)
        if check_collisions(snake_positions):
            return
    
        if check_food_collision(snake_positions, food_position):
            food_position = set_food(snake_positions)
            score += 1

        pygame.display.update()

        clock.tick(20)


playgame()








