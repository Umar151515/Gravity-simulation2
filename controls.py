import sys 

import pygame
from pygame.math import Vector2


def event(window, core, config): 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
            if event.key == pygame.K_a:
                core.left = True
            elif event.key == pygame.K_d:
                core.right = True
            if event.key == pygame.K_w:
                core.up = True
            elif event.key == pygame.K_s:
                core.down = True
            if event.key == pygame.K_LEFT and config.speed_time > 0:
                config.speed_time *= 0.5
            elif event.key == pygame.K_RIGHT:
                config.speed_time *= 2
            if event.key == pygame.K_SPACE:
                if config.speed_time:
                    config.speed_time = 0
                else:
                    config.speed_time = 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                core.left = False
            elif event.key == pygame.K_d:
                core.right = False
            if event.key == pygame.K_w:
                core.up = False
            elif event.key == pygame.K_s:
                core.down = False
        if event.type == pygame.MOUSEMOTION:
            mouse_buttons = pygame.mouse.get_pressed()
            
            core.mouse.vector.x = core.mouse.x_window - event.pos[0]
            core.mouse.vector.y = core.mouse.y_window - event.pos[1]
            
            if mouse_buttons[0]:
                core.config.camera_position_x += core.mouse.vector.x
                core.config.camera_position_y += core.mouse.vector.y

            core.mouse.x_window, core.mouse.y_window = event.pos
        else:
            core.mouse.vector.xy = 0, 0
        

        if event.type == pygame.MOUSEWHEEL:
            world_mouse_x = (core.mouse.x_window + core.config.camera_position_x) / config.scale
            world_mouse_y = (core.mouse.y_window + core.config.camera_position_y) / config.scale

            if event.y > 0:
                config.scale += config.scrolling_speed * config.scale
            else:
                config.scale -= config.scrolling_speed * config.scale

            new_screen_mouse_x = world_mouse_x * config.scale - config.camera_position_x
            new_screen_mouse_y = world_mouse_y * config.scale - config.camera_position_y

            core.config.camera_position_x += (new_screen_mouse_x - core.mouse.x_window)
            core.config.camera_position_y += (new_screen_mouse_y - core.mouse.y_window)

def update(window, core):
    for unit in core.units:
        unit.update()
        unit.draw()
    for text in core.group_text:
        text.draw()

    core.update()
    core.mouse.update()
    core.group_text.update()

    core.text_scale.text = 'scale: ' + str(round(core.config.scale, 5))
    core.text_cor.text = 'cor camera: ' + str((round(core.config.camera_position_x, 2), round(core.config.camera_position_y, 2)))
    core.text_speed_time.text = 'speed time: ' + str(round(core.config.speed_time, 2))