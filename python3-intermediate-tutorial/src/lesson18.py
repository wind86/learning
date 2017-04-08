'''
Created on Apr 08, 2017

Operator Overloading Python Tutorial
https://www.youtube.com/watch?v=Qhj21B7kTkM&list=PLQVvvaa0QuDfju7ADVp5W1GF9jVhjbX-_&index=19

@author: ubuntu
'''
import random
import pygame
from blob import Blob

STARTING_BLUE_BLOBS = 10
STARTING_RED_BLOBS = 3
STARTING_GREEN_BLOBS = 5

WIDTH = 800
HEIGHT = 600

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

game_display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Blob World")
clock = pygame.time.Clock()


class BlueBlob(Blob):
    
    def __init__(self, x_boundary, y_boundary):
        Blob.__init__(self, BLUE, x_boundary, y_boundary)

    def __add__(self, other_blob):
        if other_blob.color == RED:
            self.size -= other_blob.size
            other_blob.size -= self.size
            
        elif other_blob.color == GREEN:
            self.size += other_blob.size
            other_blob.size = 0
            
        elif other_blob.color == BLUE:
            # for now, nothing. Maybe later it does something more. 
            pass
        else:
            raise Exception('Tried to combine one or multiple blobs of unsupported colors!')
        
class RedBlob(Blob):
    
    def __init__(self, x_boundary, y_boundary):
        Blob.__init__(self, RED, x_boundary, y_boundary)
        
        
class GreenBlob(Blob):
    
    def __init__(self, x_boundary, y_boundary):
        Blob.__init__(self, GREEN, x_boundary, y_boundary)



def draw_environment(blob_list):
    game_display.fill(WHITE)

    for blob_dict in blob_list:
        for blob_id in blob_dict:
            blob = blob_dict[blob_id]
            pygame.draw.circle(game_display, blob.color, [blob.x, blob.y], blob.size)
            blob.move()
            blob.check_bounds()

    pygame.display.update()

def main():
    blue_blobs = dict(enumerate([BlueBlob(WIDTH,HEIGHT) for i in range(STARTING_BLUE_BLOBS)]))
    red_blobs = dict(enumerate([RedBlob(WIDTH,HEIGHT) for i in range(STARTING_RED_BLOBS)]))
    green_blobs = dict(enumerate([GreenBlob(WIDTH,HEIGHT) for i in range(STARTING_GREEN_BLOBS)]))
    
    print('Current blue size: {}. Current red size: {}'.format(str(blue_blobs[0].size), str(red_blobs[0].size)))

    blue_blobs[0] + red_blobs[0]
    print('Current blue size: {}. Current red size: {}'.format(str(blue_blobs[0].size), str(red_blobs[0].size)))
    
#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 quit()
#         draw_environment([blue_blobs, red_blobs, green_blobs])
#         clock.tick(60)

if __name__ == '__main__':
    main()