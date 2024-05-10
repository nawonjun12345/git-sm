for i in range(1,10,1):
    print("")
    for g in range(2,6,1) :
        a = i*g
        print(g ,'x', i ,'=', f'{a:2d}', end='\t')
        if g==5 :
            print('')
print("")  

for i in range(1,10,1):
    print("")
    for g in range(6,10,1) :
        a = i*g
        print(g ,'x', i ,'=', f'{a:2d}', end='\t')
        if g==9 :
            print('')

