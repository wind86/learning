'''
Created on Jan 21, 2017

@author: ubuntu
'''
def basic_window(height,width,
                 font='Tahoma',
                 backgroundColor='white'):
    print('size:',height,width,'font:',font,'background color:',backgroundColor)
    
basic_window(50, 100)
basic_window(20, 120, 'Arial')
basic_window(50, 150, backgroundColor='green')
    