class Veiculo:
    def __init__(self, placa):
        self.__placa = placa
        self.estacionado = False
        self.tipo = 'veiculo'

    @property
    def placa(self):
        return self.__placa

    def estacionar(self, estacionamento):
        
        vaga = estacionamento.receber_veiculo(self)
        if(vaga != None):
            self.id_vaga_estacionado = vaga
            self.estacionado = True   

    def sair_da_vaga(self, estacionamento):
        
        estacionamento.despedir_veiculo(self)
            
        self.id_vaga_estacionado = None 
        self.estacionado = False