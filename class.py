from abc import ABC, abstractmethod

class Pessoa(ABC):
  def __init__ (self, nome, telefone):
    self.nome = nome
    self.telefone = telefone
    
  @abstractmethod
  def receberNotificacao(self):
    pass

class Usuaria(Pessoa):
  def 
  
