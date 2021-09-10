def calculate():
    operation = input('''
    Por favor escolha uma operação que gostaria de completar:
    + para adição
    - para subtração
    / para divisão
    * para multiplicação
    ''')

    number_1 = float(input("Coloque seu primeiro numero: "))
    number_2 = float(input("Coloque seu segundo numero: "))

    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)
        
    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)
        
    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)

    elif operation == '*': 
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)

    else:
        print('Você não digitou um operador válido, por favor execute o programa novamente.')       
        
    again()

def again():
    calc_again = input('''
    Você dejesa calcular novamente?
    Por favor digite Y para sim e N para não.
    ''')

    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
        print('Até nunca mais.')
    else:
        again()

calculate()
        
        








    
