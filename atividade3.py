import random

class No:
    def _init_(self, valor):
      
        self.valor = valor
        self.esquerda = None
        self.direita = None

class ArvoreBinaria:
  
    def _init_(self):
        self.raiz = None
        self.quantidade = 0
    
    def inserir(self, valor):
      
      
        novo_no = No(valor)
        
        if self.raiz is None:
            self.raiz = novo_no
            
        else:
            atual = self.raiz
            while True:
              
              
                if valor < atual.valor:
                  
                    if atual.esquerda is None:
                        atual.esquerda = novo_no
                        break
                        
                    else:
                        atual = atual.esquerda
                        
                else:
                    if atual.direita is None:
                        atual.direita = novo_no
                        break
                    else:
                        atual = atual.direita
        self.quantidade += 1
    
    def quantidade_elementos(self):
        return self.quantidade
    
