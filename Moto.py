from Veiculo import Veiculo 

class Moto(Veiculo):
    def __init__(self, placa):
        super().__init__(placa)
        self.tipo = 'moto'