# Author : Dimitri da Silva Finger
# Projeto e Otimização de Algoritmos - 2021/1
# Pontifícia Universidade Católica do Rio Grande do Sul (PUC-RS)
# Karatsuba's Algorithm

import sys

def Karatsuba(number_A, number_B):
    
    

    # define shift size
    shift = int(len(number_A)/2) * '0'

    if len(number_A) == 1:
        return str(int(number_A) * int(number_B))

    if len(number_A) > len(number_B):
        while len(number_A) != len(number_B):
            number_B = '0' + number_B

    elif len(number_A) < len(number_B):
        while len(number_A) != len(number_B):
            number_A = '0' + number_A    

    if len(number_A)%2 != 0 and len(number_A) > 1:
        number_A = '0' + number_A
        number_B = '0' + number_B  

    #Sum(number_A,number_B)
    Subtraction(number_A, number_B)
    
    number_A_1 = number_A[:int(len(number_A)/2)]
    number_A_2 = number_A[int(len(number_A)/2):]
    number_B_1 = number_B[:int(len(number_B)/2)]
    number_B_2 = number_B[int(len(number_B)/2):]


def Sum(number_1, number_2):

    x = number_1
    y = number_2
    aux = 0
    result = ''

    while len(x) != 0:
        calc = int(x[-1:]) + int(y[-1:]) + aux
        result = str(calc%10) + result
        aux = int(calc/10)
        x = x[:-1]
        y = y[:-1]
    
    return print(str(result))



def Subtraction(number_1,number_2):
    x = number_1
    y = number_2
    result = ''
    aux2 = 0
    changed = False

    if y > x :
        x,y = y,x
        changed = True

    while len(x) != 0:
        if y[-1:] > x[-1:]:
            aux = int(x[-1:]) + 10
            aux = aux - int(y[-1:])
            aux2 = 1
            result = str(aux) + result
        else:
            #ajustar erro quando rouba de 0
            aux = int(x[-1:]) - aux2 - int(y[-1:])
            aux2 = 0
            result = str(aux) + result
    
        x = x[:-1]
        y = y[:-1]
    
    #if changed == False:
    print(result)
    











 
    #part1 = Karatsuba(number_A_1,number_B_1)
    #part2 = Karatsuba(number_A_2,number_B_1)
    #part3 = Karatsuba(number_A_1,number_B_2)
    #part4 = Karatsuba(number_A_2,number_B_2)

    #print(part1)
    
    #AB = (str(part1) + 2*shift) + (str(int(part2+part3)) + shift) + str(part4)
    #print(AB)
    #print(part1,part2,part3,part4)



    







if __name__ == "__main__":
    
    if len(sys.argv)<2:
    
        print("\n\nFormato de entrada inválido!")
        print("Por favor, adicione dois número após a chamada do programa:\n")
        print("Ex: py Karatsuba 7 39\n")
        sys.exit(1)
        
    else:
        number_A = sys.argv[1]
        number_B = sys.argv[2]

    Karatsuba(number_A,number_B)
   
    #print(x,y,z)
    #print(len(x),len(y),len(z))
    #print(type(x), type(y),type(z))

   

