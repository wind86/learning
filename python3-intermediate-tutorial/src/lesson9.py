'''
Created on Apr 08, 2017

Multiprocessing with Python intro
https://www.youtube.com/watch?v=oEYDqQ1pq9o&list=PLQVvvaa0QuDfju7ADVp5W1GF9jVhjbX-_&index=10

@author: ubuntu
'''
import multiprocessing

def spawn(num):
    print('Spawned {}'.format(num))

def main():
    for i in range(5):
        p = multiprocessing.Process(target=spawn, args=(i,))
        p.start()
        #p.join()
        
if __name__ == '__main__':
    main()