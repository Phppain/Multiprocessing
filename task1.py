"""task1.py"""

from random import randint
from time import sleep, time
from multiprocessing import Process

def write_number_file(num: int) -> None:
    """
    This function create file "number.txt"
    and write random number

    Args:
        num: int
    
    Output:
        None
    """
    with open('number.txt', 'w') as file:
        sleep(1)
        file.write(str(num))

if __name__ == "__main__":   
    start = time()
    for i in range(1000):
        number = randint(-1000, 1000)
        print(i)
        write_number_file(number)
    end = time()

    start2 = time()
    for i in range(1000):
        print(i)
        number = randint(-1000, 1000)
        p = Process(target=write_number_file, args=(number, ))
        p.start()
    for _ in range(1000):
        p.join()
    end2 = time()
    print(end2 - start2, sep='\n')
