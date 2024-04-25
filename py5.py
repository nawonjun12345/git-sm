def read_single_digit(a) :
    n1 = a%10
    n2 = ((a-n1) % 100) //10
    n3 = a//100
    z = read_number(n3)
    y = read_number(n2)
    x = read_number(n1)

def read_number(b):
    if b ==1 :
        print('일',end = '')
    elif b == 2:
        print('이',end = '')
    elif b == 3:
        print('삼',end = '')
    elif b == 4:
        print('사',end = '')
    elif b == 5:
        print('오',end = '')
    elif b == 6:
        print('육',end = '')
    elif b == 7:
        print('칠',end = '')
    elif b == 8:
        print('팔',end = '')
    else :
        print('구',end = '')




nu = int(input("세 자리 정수 입력:"))
read_single_digit(nu)
