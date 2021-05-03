

def foo():
    '''this programs prints from 1 to 50, but for multiples of 3, 
    it prints 'Fizz', for mulitples of 5 it prints 'Buzz' and for multiples of both,
    it prints 'FizzBuzz
    '''
    for i in range(1,51):
        if i%15==0:
            print('FizzBuzz')
        elif i%3 == 0:
            print('Fizz')
        elif i%5 == 0:
            print('Buzz')
        else:
            print(i)

if __name__ == '__main__':
    foo()
