# module print_fibonacci

# system
import sys


def fibonacci_sequence(n: int = 10) -> list[int]:
    """Return first N numbers in a sequence

    Args:
        n (int, optional): number of numbers to generate in a sequence. Defaults to 10.

    Returns:
        list[int]: fibonacci sequence
    """
    # initializing the first two numbers of the Fibonacci sequence
    sequence = [0, 1]
    
    # generating the Fibonacci sequence
    for _ in range(2, n):
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)
    
    return sequence[:n]


if __name__ == "__main__":
    # init and check for args
    n = 10
    if len(sys.argv) > 1: 
        try: n = int(sys.argv[1])
        except: pass
        
    # overflow control
    if n > 1000:
        print('Overflow. Only up to 1000 is allowed. Reset to 10.')
        n = 10

    # print out the sequence
    print(fibonacci_sequence(n))
