class HashTable:
    def __init__(self):
        self._tamanho = 200
        self._slots = [None] * self._tamanho
        self._valores = [None] * self._tamanho
    
    def hashfunction(self, chave, tamanho): 
        sum = 0 
        for pos in range(len(chave)):
            sum = sum+ord(chave[pos])*(pos+1)
        return sum%tamanho
    
    def rehash(self, oldhash, tamanho): #trata colisões de objetos com mesmo hash
        return (oldhash+1)%tamanho

    def put(self, chave, valor):
        valor_hash = self.hashfunction(chave, len(self._slots))
        if self._slots[valor_hash] == None:
            self._slots[valor_hash] = chave
            self._valores[valor_hash] = valor
        else:
            if self._slots[valor_hash] == chave:
                self._valores[valor_hash] = valor #replace
            else:
                proximo_slot = self.rehash(valor_hash,len(self._slots))
                while self._slots[proximo_slot] != None and self._slots[proximo_slot] != chave:
                    proximo_slot = self.rehash(proximo_slot,len(self._slots))

            if self._slots[proximo_slot] == None:
                self._slots[proximo_slot]=chave
                self._valores[proximo_slot]=valor
            else:
                self._valores[proximo_slot] = valor #replace

    def get(self, chave): #return alterado pegar posicao-indice. antes era o valor. 
        slot_inicial = self.hashfunction(chave,len(self._slots))
        valor = None
        parar = False
        encontrou = False
        posicao = slot_inicial
        while self._slots[posicao] != None and not encontrou and not parar:
            if self._slots[posicao] == chave:
                encontrou = True
                valor = self._valores[posicao]
            else:
                posicao=self.rehash(posicao,len(self._slots))
                if posicao == slot_inicial:
                    parar = True
        return posicao

    def __getitem__(self,chave):
        return self.get(chave)
    def __setitem__(self,chave,valor):
        self.put(chave, valor)
    
    
    def __str__(self) -> str:
        posicao = 0
        vagas = self._tamanho
        result = "------Situação atual do estacionamento------\n            Vagas ocupadas:"
        while posicao < len(self._slots):
            if self._slots[posicao] != None:
                key_valor = f'\nVaga {posicao}: {self._slots[posicao]}: {self._valores[posicao]}'
                result += key_valor
                posicao+= 1
                vagas -= 1
            else:
                posicao +=1
        result += f'\n\nQuantidade de vagas disponiveis: {vagas}'
        return result
        