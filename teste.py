import sys
def Subtraction(number_1,number_2):
    x = number_1
    y = number_2


    if len(x) > len(y):
        while len(y) != len(x):
            y = '0' + y
  
    result = ''
    changed = False
    carry = 0

    if y > x :
        x,y = y,x
        changed = True

    if len(y) == 1 and len(x) == 1:
        result = str(int(x[-1:]) - int(y[-1:]))
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
                aux = int(x[-1:]) - int(y[-1:]) - carry
                carry = 0
                result = str(aux) + result
        
            x = x[:-1]
            y = y[:-1]
        
    if changed == False:
        print(result)
        return str(result)
    else:
        print('-' + result)
        return '-' + str(result)



if __name__ == "__main__":
    
    if len(sys.argv)<2:
    
        print("\n\nFormato de entrada inválido!")
        print("Por favor, adicione dois número após a chamada do programa:\n")
        print("Ex: py Karatsuba 7 39\n")
        sys.exit(1)
        
    else:
        number_A = sys.argv[1]
        number_B = sys.argv[2]

    Subtraction(number_A,number_B)