import pygame

class Enemy:    # 클래스
    def __init__(self, enemy, enemy_size, enemy_width, enemy_height, enemy_x_pos, enemy_y_pos):
        self.enemy = enemy
        self.enemy_size = enemy_size
        self.enemy_width = enemy_width
        self.enemy_height = enemy_height
        self.enemy_x_pos = enemy_x_pos
        self.enemy_y_pos =enemy_y_pos
