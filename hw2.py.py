def exchange(prompt) :
    n500 = prompt // 500
    prompt %= 500
    n100 = prompt//100
    prompt %= 100
    n50 = prompt//50
    prompt %= 50
    n10 = prompt//10
    print('\n','500원 동전의 개수:',n500,'\n','100원 동전의 개수: ',n100,'\n','50원 동전의 개수',n50,'\n','10원 동전의 개수:',n10)

def get_integer(money) :
    res = int(input(money))
    return res

money1 = get_integer('동전으로 교환하고자 하는 금액은?')
exchange(money1)
