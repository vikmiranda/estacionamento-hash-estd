from HashTable import *
from manipula_dados import *

#MENU
while True:
    print('\n(1) Estacionar Veículo\n(2) Checar localizacao de um veículo\n(3) Sair do estacionamento\n(4) Checar situação do estacionamento\n(5) Fechar')
    x = int(input('Escolha uma opção: '))
    if x == 1: inserir_veiculo() 
    elif x == 2: checar_veic()
    elif x == 3: remover_veiculo()
    elif x==4: print(CarroGuardado)
    elif x== 5: break
    else: print('Digite uma opção válida')