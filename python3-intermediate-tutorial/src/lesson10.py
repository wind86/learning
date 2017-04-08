'''
Created on Apr 08, 2017

Getting Values from Multiprocessing Processes
https://www.youtube.com/watch?v=kUKOEuPJXGc&list=PLQVvvaa0QuDfju7ADVp5W1GF9jVhjbX-_&index=11

@author: ubuntu
'''
from multiprocessing import Pool

def job(num):
    return num * 2

if __name__ == '__main__':
    p = Pool(processes=20)
    data = p.map(job, [i for i in range(20)])
    p.close()
    print(data)