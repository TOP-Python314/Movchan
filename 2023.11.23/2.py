a = int(input())
b = int(input())
c = int (a / b)
d = int (a % b)

if a % b == 0:
    print (f'{a} делится на {b} нацело', f'частное: {c}', sep='\n' )
    
elif a % b == 1:
    print (f'{a} не делится на {b} нацело', f'неполное частное: {c}', f'остаток: {d}', sep='\n')   