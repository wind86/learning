'''
Created on Apr 08, 2017

List comprehension and generator expressions - Intermediate Python Programming p.4 
https://www.youtube.com/watch?v=ZoWgzG_r2qo&index=4&list=PLQVvvaa0QuDfju7ADVp5W1GF9jVhjbX-_

@author: ubuntu
'''

# with a generator, the values are generated from an original input, 
# but the values are not copied and instead are generated on-the-fly. 
# This means we will use far less memory, since the entire list is not processed all at once, 
# but also means the process is a bit slower, since things are indeed generated as we go
xyz = (i for i in range(50000000))
print(list(xyz)[:5])

# list comprehension puts the entire list into memory, so it is faster, 
# but the penalty is memory use
xyz = [i for i in range(50000000)]
print(xyz[:5])