'''
Created on Apr 08, 2017

Blob Class and Modularity - Object Oriented Programming
https://www.youtube.com/watch?v=mbHc1prq-4g&list=PLQVvvaa0QuDfju7ADVp5W1GF9jVhjbX-_&index=16

@author: ubuntu
'''

import pygame
from blob import Blob

STARTING_BLUE_BLOBS = 10
STARTING_RED_BLOBS = 3

WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

game_display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Blob World")
clock = pygame.time.Clock()

def draw_environment(blob_list):
    game_display.fill(WHITE)

    for blob_dict in blob_list:
        for blob_id in blob_dict:
            blob = blob_dict[blob_id]
            pygame.draw.circle(game_display, blob.color, [blob.x, blob.y], blob.size)
            blob.move()
            blob.check_bounds()

    pygame.display.update()
    
def create_blobs(color, quantity):
    return dict(enumerate([Blob(color,WIDTH,HEIGHT) for i in range(quantity)]))

def main():
    blue_blobs = create_blobs(BLUE, STARTING_BLUE_BLOBS)
    red_blobs = create_blobs(RED, STARTING_RED_BLOBS)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        draw_environment([blue_blobs,red_blobs])
        clock.tick(60)

if __name__ == '__main__':
    main()