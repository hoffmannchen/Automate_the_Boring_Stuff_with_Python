
def collatz(number):
    if number % 2 == 0:
        re = (number//2)
    else:
        re = (number*3+1)

    print(re)
    return re


print('Enter number:')
while True:
    try:
        num = int(input())
    except ValueError:
        print('It must be integer.')
        continue
    re = collatz(num)
    if re == 1:
        break
