# Author : Dimitri da Silva Finger
# Projeto e Otimização de Algoritmos - 2021/1
# Pontifícia Universidade Católica do Rio Grande do Sul (PUC-RS)
# Karatsuba's Algorithm

import sys

def Karatsuba(number_A, number_B):      

    if len(number_A) == 1 and len(number_B) == 1:
       #print(str(int(number_A) * int(number_B)))
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

    # define shift size
    shift = int(len(number_A)/2) * '0' 
    
    number_A_1 = number_A[:int(len(number_A)/2)]
    number_A_2 = number_A[int(len(number_A)/2):]
    number_B_1 = number_B[:int(len(number_B)/2)]
    number_B_2 = number_B[int(len(number_B)/2):]
  
    
    #A1_A2 = Sum(number_A_1,number_A_2)
    #B1_B2 = Sum(number_B_1,number_B_2)   

    #Subtraction(number_A, number_B) 
    Sum(number_A,number_B)
    
    #A1_B1 = Sum(number_A_1,number_B_1)
    #A2_B2 = Sum(number_A_2,number_B_2)

    

# strings sum
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
    if aux != 0:
        result = str(aux) + result

    print(result)        
   


# strings subtraction
def Subtraction(number_1,number_2):
    x = number_1
    y = number_2
    result = ''
    changed = False
    carry = 0

    if y > x :
        x,y = y,x
        changed = True

    if len(y) == 1 and len(x) == 1:
        result = int(x[-1:]) - int(y[-1:])
    else:
        while len(x) != 0:
            if y[-1:] > x[-1:]:
                aux = (int(x[-1:]) + 10) - carry
                aux = aux - int(y[-1:])
                carry = 1
                result = str(aux) + result
            elif y[-1:] == '0' and x[-1:] == '0' and carry > 0:
                aux = (int(x[-1:]) + 10) - carry            
                result = str(aux) + result
            else:
                #ajustar erro quando rouba de 0
                aux = int(x[-1:]) - int(y[-1:]) - carry
                carry = 0
                result = str(aux) + result
        
            x = x[:-1]
            y = y[:-1]
        
    if changed == False:
        print(result)
    else:
        print('-' + result)
    











 

    
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
