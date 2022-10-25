from HashTable import *

CarroGuardado = HashTable()

def inserirVeic():
        placa=input('Informe a placa do veículo: ').upper()
        #conferir se o veículo informado já existe
        if placa in CarroGuardado._slots:
          x = CarroGuardado.get(placa)
          print(f'Um veículo com essa placa já se encontra no estacionamento na vaga: {x}')
        else:
          modelo = input('Informe Modelo e Cor do Veículo: ').upper()
          CarroGuardado.put(placa, modelo)
          print('Veículo estacionado')
          
          #guardar informacoes do veiculo estacionado em estacionamento-dados.txt
          with open('estacionamento-dados.txt', 'a') as arquivo:
              arquivo.write(f'\n{placa} /{modelo}')

def vagaVeic():
    placa=input('Informe a placa do veículo: ').upper()
    if placa in CarroGuardado._slots:
        x = CarroGuardado.get(placa)
        print(f'O veículo está na vaga: {x}')
    else:
        print('Veículo não encontrado')

def sair():
    placa=input('Informe a placa do veículo: ').upper()
    if placa in CarroGuardado._slots:
        x = CarroGuardado.get(placa)
        del CarroGuardado._slots[x]
        del CarroGuardado._valores[x]
        print(f'Veículo retirado, a vaga {x} agora está disponivel')
        
        #removendo veiculo do estacionamento-dados.txt
        with open('estacionamento-dados.txt', 'r+') as f:
            new_f = f.readlines()
            f.seek(0)
            for line in new_f:
                if placa not in line:
                    f.write(line)
            f.truncate()
    else: print('Veículo não encontrado!')

#a função testes adiciona alguns veículos para que o programa já comece com o estacionamento em uso.
def testes():
    ler_veics = open('estacionamento-dados.txt', 'r')
    for linha in ler_veics:
        if linha != '\n':
            key_model = linha.split('/')
            key = key_model[0].rstrip()
            valor= key_model[1].rstrip()
            CarroGuardado.put(key, valor)
    ler_veics.close()

testes()
while True:
    print('\n(1) Estacionar Veículo\n(2) Checar localizacao de um veículo\n(3) Sair do estacionamento\n(4) Checar situação do estacionamento\n(5) Fechar')
    x = int(input('Escolha uma opção: '))
    if x == 1: inserirVeic() 
    elif x == 2: vagaVeic()
    elif x == 3: sair()
    elif x==4: print(CarroGuardado)
    elif x== 5: break
    else: print('Digite uma opção válida')