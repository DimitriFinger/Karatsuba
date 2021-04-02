# Author : Dimitri da Silva Finger
# Projeto e Otimização de Algoritmos - 2021/1
# Pontifícia Universidade Católica do Rio Grande do Sul (PUC-RS)
# Algoritmo de Karatsuba

import sys

if __name__ == "__main__":
    
    if len(sys.argv)<2:
    
        print("\n\nFormato de entrada inválido!")
        print("Por favor, adicione dois número após a chamada do programa:\n")
        print("Ex: py Karatsuba 7 39\n")

        sys.exit(1)
    else:
        number_one = sys.argv[1]
        number_two = sys.argv[2]

   

