# -*- coding: utf-8 -'
"""
Created on Sat Jan 30 22:11:39 2021

@author: Natalya Lisitskaya

"""
import numpy as np

def setup_sequence():
    '''  

    Returns
    -------
    list
        define the series of numbers

    '''
    
    return [x for x in range(1,101)]

def choose_half(x, predict):
    '''
    
    Parameters
    ----------
    x : list
        the series of numbers
    predict : integer
        the guessed number

    Returns
    -------
    x : list
        the sequence of numbers is corrected using the dichotomy method

    '''
    
    if number > predict: 
        x = x[len(x)//2:]
    else: # number < predict 
        x = x[:len(x)//2+1]
    
    return x    
    
count = 0    # the attempt counter
x = setup_sequence()  # determine the sequence of numbers from which the number will be guessed              
number = np.random.randint(x[0], x[-1])   # make a number

print (f"Загадано число от {x[0]} до {x[-1]} \n"\
       f"Это число {number} \n"\
       f"Посмотрим как компьютер угадает его..."    
       )

while True: 
    print (f"Угадываемое число больше {x[0]-1} и меньше {x[-1]+1} ")                  
    predict = x[len(x)//2]         # guess the number using the dichotomy method
    print(predict)
    count += 1                     # the attempt counter + 1
    
    if number == predict: 
        break    # successful exit from the loop, the number of correctly predicted
    else:
        x = choose_half(x, predict) # choose the half of the sequence in which the guessed number is located
     
print (f"Задуманное число {number} угадано за {count} попыток.")   
