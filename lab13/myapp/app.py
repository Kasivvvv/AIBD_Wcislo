import numpy as np
from  typing import Union, List

#Faza 2 napisanie algorytmu 

def bubblesort(input: Union[List[int], List[float]]):
    length = len(input)
    for repeats in range(0,length-1):
        for iteration in range(0,length-1):
            if input[iteration] > input[iteration+1]:
                (input[iteration],input[iteration+1]) = (input[iteration+1],input[iteration])
    return input

#Faza 3 Refraktoryzacja - niepotrzebna

#Powtórzenie Fazy 2 zawierając nowe testy 

def bubblesort_2(input: Union[List[int], List[float]]):
    if isinstance(input, (Union[List[int], List[float]])):
        length = len(input)
        for repeats in range(0,length-1):
            for iteration in range(0,length-1):
                if input[iteration] > input[iteration+1]:
                    (input[iteration],input[iteration+1]) = (input[iteration+1],input[iteration])
        return input
    else:
        return np.NaN

#Faza 3 Refraktoryzacja - niepotrzebna