
import sys

def Karatsuba(number_A, number_B):

    if len(number_A) <10 and len(number_B) <10:
       return str(int(number_A) * int(number_B))

    number_A,number_B = SameSize(number_A,number_B)
   
    shift = int(len(number_A)/2) * '0'
    
    a1,a2,b1,b2 = Slice(number_A, number_B)
    
    a1,a2 = SameSize(a1,a2)
    b1,b2= SameSize(b1,b2)
    a1a2 = Sum(a1,a2)
    b1b2 = Sum(b1,b2)

    a1_b1 = Karatsuba(a1,b1)
    a2_b2 = Karatsuba(a2,b2)
    a1a2_b1b2 = Karatsuba(a1a2,b1b2)
    
    a1a2_b1b2,a1_b1= SameSize(a1a2_b1b2,a1_b1)
    subtraction = Sub(a1a2_b1b2,a1_b1)
    
    subtraction, a2_b2= SameSize(subtraction, a2_b2)
    subtracted_part = Sub(subtraction, a2_b2)

    a1_b1 = (a1_b1 + shift + shift)    
    subtracted_part = subtracted_part + shift

    a1_b1,subtracted_part = SameSize(a1_b1,subtracted_part)
    sum = Sum(a1_b1,subtracted_part)
    sum,a2_b2= SameSize(sum,a2_b2)
    sum_result = Sum(sum,a2_b2)

    return sum_result



def SameSize(number_A, number_B):   
    if len(number_A) > len(number_B):
        while len(number_A) != len(number_B):
            number_B = '0' + number_B

    elif len(number_A) < len(number_B):
        while len(number_A) != len(number_B):
            number_A = '0' + number_A   

    if len(number_A)%2 != 0 and len(number_A) > 1:
        number_A = '0' + number_A
    if len(number_B)%2 != 0 and len (number_B) >1:
        number_B = '0' + number_B     

    return number_A,number_B
    


def Slice(number_A, number_B):
    a1 = number_A[:int(len(number_A)/2)]
    a2 = number_A[int(len(number_A)/2):]
    b1 = number_B[:int(len(number_B)/2)]
    b2 = number_B[int(len(number_B)/2):]
    
    return a1,a2,b1,b2


def Sum(number_1,number_2):    
    carry = 0
    result = ''
    
    while len(number_1) != 0:
        calc = int(number_1[-1]) + int(number_2[-1]) + carry        
        result = str(calc%10) + result       
        carry = int(calc/10)    
        number_1 = number_1[:-1]
        number_2 = number_2[:-1]

    if carry != 0:
        result = str(carry) + result
    return result



def Sub(number_1,number_2):
    carry = 0
    result = ''
    aux = 0
    if number_2 > number_1 :
        number_1,number_2 = number_2,number_1        
    
    if len(number_2) == 1:
        result = str(int(number_1[-1]) - int(number_2[-1]))
    else:
        while len(number_1) !=0 :
                    if number_2[-1] > number_1[-1]:                        
                        aux = int(number_1[-1]) + 10  - carry             
                        aux = aux - int(number_2[-1])
                        carry = 1
                        result = str(aux) + result
                        number_1 = number_1[:-1]
                        number_2 = number_2[:-1]

                    elif number_2[-1] == '0' and number_1[-1] == '0' and carry > 0:
                        aux = (int(number_1[-1]) + 10) - carry         
                        result = str(aux) + result
                        number_1 = number_1[:-1]
                        number_2 = number_2[:-1]

                    else:
                        if carry > 0 and number_2[-1] == number_1[-1]:
                            aux = int(number_1[-1]) + 10  - carry             
                            aux = aux - int(number_2[-1])
                            carry = 1
                            result = str(aux) + result
                            number_1 = number_1[:-1]
                            number_2 = number_2[:-1]
                        else:
                            aux = int(number_1[-1]) - int(number_2[-1]) - carry
                            carry = 0
                            result = str(aux) + result        
                            number_1 = number_1[:-1]
                            number_2 = number_2[:-1]   
                       
    return result


if __name__ == "__main__":
    
    if len(sys.argv)<2:
    
        print("\n\nFormato de entrada inválido!")
        print("Por favor, adicione dois número após a chamada do programa:\n")
        print("Ex: py Karatsuba 7 39\n")
        sys.exit(1)
        
    else:
        number_A = sys.argv[1]
        number_B = sys.argv[2]

    x = int(Karatsuba(number_A,number_B))
    print(str(x))
   