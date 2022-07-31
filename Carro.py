from Veiculo import Veiculo 

class Carro(Veiculo):
    def __init__(self, placa):
        super().__init__(placa)
        self.tipo = 'carro'