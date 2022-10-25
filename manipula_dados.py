from HashTable import *

CarroGuardado = HashTable()

#escrever informacoes do veiculo estacionado em estacionamento-dados.txt
def escreve_carro(placa, modelo):
  with open('estacionamento-dados.txt', 'a') as arquivo:
      arquivo.write(f'\n{placa} /{modelo}')

    
#remover informacoes do veiculo estacionado em estacionamento-dados.txt
def remove_carro(placa):
  with open('estacionamento-dados.txt', 'r+') as f:
              new_f = f.readlines()
              f.seek(0)
              for line in new_f:
                  if placa not in line:
                      f.write(line)
              f.truncate()


def inserir_veiculo():
    placa=input('Informe a placa do veículo: ').upper()
          #conferir se o veículo informado já existe
    if placa in CarroGuardado._slots:
      x = CarroGuardado.get(placa)
      print(f'Um veículo com essa placa já se encontra no estacionamento na vaga: {x}')
    else:
      modelo = input('Informe Modelo e Cor do Veículo: ').upper()
      CarroGuardado.put(placa, modelo)
      print('Veículo estacionado')

    escreve_carro(placa, modelo) 

  
#checar vaga em que o veiculo esta estacionado
def checar_veic():
    placa=input('Informe a placa do veículo: ').upper()
    if placa in CarroGuardado._slots:
        x = CarroGuardado.get(placa)
        print(f'O veículo está na vaga: {x}')
    else:
        print('Veículo não encontrado')


def remover_veiculo():
    placa=input('Informe a placa do veículo: ').upper()
    if placa in CarroGuardado._slots:
        x = CarroGuardado.get(placa)
        del CarroGuardado._slots[x]
        del CarroGuardado._valores[x]
        print(f'Veículo retirado, a vaga {x} agora está disponivel')
        remove_carro(placa)  #removendo veiculo do estacionamento-dados.txt
  
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
