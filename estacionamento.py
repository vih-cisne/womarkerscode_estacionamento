
class Vaga:
    def __init__(self, id, tipo):
        self.placa = None
        self.livre = True
        self.__id = id
        self.tipo = tipo
    
    @property
    def id(self):
        return self.__id

    def ocupar(self,veiculo):
        self.livre = False
        self.placa = veiculo.placa

        mensagem_adicional = ''

        if(veiculo.tipo != self.tipo):
            mensagem_adicional = f'Não haviam mais vagas para {veiculo.tipo} disponíveis, por isso, estacionamos em uma vaga de {self.tipo}'
            
        print(f'Sucesso! {veiculo.tipo} de placa {veiculo.placa} estacionado(a) na vaga de número {self.id}.', mensagem_adicional)

    def desocupar(self, veiculo):
        self.livre = True
        self.placa = None

        print('Volte sempre!')

    
class Veiculo:
    def __init__(self, placa):
        self.__placa = placa
        self.estacionado = False
        self.tipo = 'Veiculo'

    @property
    def placa(self):
        return self.__placa

    def estacionar(self, estacionamento):
        if(self.tipo == 'carro'):
            vaga = estacionamento.estacionar_carro(self)
            if(vaga != None):
                self.id_vaga_estacionado = vaga
                self.estacionado = True 
        elif(self.tipo == 'moto'):
            vaga = estacionamento.estacionar_moto(self)
            if(vaga != None):
                self.id_vaga_estacionado = vaga
                self.estacionado = True  

    def sair_da_vaga(self):
        if(self.tipo == 'carro'):
            estacionamento.remover_carro(self)
            
            self.id_vaga_estacionado = None 
            self.estacionado = False
        elif(self.tipo == 'moto'):
            estacionamento.remover_moto(self)

            self.id_vaga_estacionado = None
            self.estacionado = False


class Carro(Veiculo):
    def __init__(self, placa):
        super().__init__(placa)
        self.tipo = 'carro'

class Moto(Veiculo):
    def __init__(self, placa):
        super().__init__(placa)
        self.tipo = 'moto'



class Estacionamento:
    def __init__(self, qtd_vagas, qtd_vagas_de_moto, qtd_vagas_de_carro):
        self.qtd_vagas = qtd_vagas
        #self.qtd_vagas_de_moto = qtd_vagas_de_moto
        #self.qtd_vagas_de_carro = qtd_vagas_de_carro
        self.vagas_de_moto = [Vaga(x,'moto') for x in range(qtd_vagas_de_moto)]
        self.vagas_de_carro = [Vaga(x,'carro') for x in range(qtd_vagas_de_moto, qtd_vagas_de_carro+qtd_vagas_de_moto)]
        #self.vagas = self.vagas_de_moto + self.vagas_de_carro
        self.carros_para_vaga = []
        self.motos_para_vaga = []
        self.total_vagas_livres_carro = qtd_vagas_de_carro
        self.total_vagas_livres_moto = qtd_vagas_de_moto

    #@carro_para_vaga.setter
        #def carros_para_vaga(self,carro):
         #   self.carro_para_vaga.append()
          #  self.estacionar_carro(carro)

    def estacionar_carro(self,carro):
        self.carros_para_vaga.append(carro)

        if(self.total_vagas_livres_carro > 0):
            for index, vaga in enumerate(self.vagas_de_carro):
                if vaga.livre == True:
                    break
                #index -1 se não encontrado (segunda verificação)?
            self.total_vagas_livres_carro -= 1
            self.carros_para_vaga.pop(0)
            self.vagas_de_carro[index].ocupar(carro)
            return index    

        else:
            print(f'Desculpa, não há vagas disponíveis no momento.')
            self.carros_para_vaga.pop(0)

    
    def estacionar_moto(self,moto):
        self.motos_para_vaga.append(moto)

        if(self.total_vagas_livres_moto > 0):
            for index, vaga in enumerate(self.vagas_de_moto):
                if vaga.livre == True:
                    break
                
            self.total_vagas_livres_moto -= 1
            self.motos_para_vaga.pop(0)
            self.vagas_de_moto[index].ocupar(moto)
            return index  

        elif(self.total_vagas_livres_carro > 0):
            for index, vaga in enumerate(self.vagas_de_carro):
                if vaga.livre == True:
                    break

            self.total_vagas_livres_carro -= 1
            self.motos_para_vaga.pop(0)
            self.vagas_de_carro[index].ocupar(moto)
            return index

        else:
            print(f'Desculpa, não há vagas disponíveis no momento.')
            self.motos_para_vaga.pop(0)

    def remover_carro(self,carro):
        self.total_vagas_livres_carro += 1
        self.vagas_de_carro[carro.id_vaga_estacionado].desocupar(carro)

    def remover_moto(self,moto):
        if(moto.id_vaga_estacionado >= len(self.vagas_de_moto)):
            self.total_vagas_livres_carro += 1
            self.vagas_de_carro[moto.id_vaga_estacionado].desocupar(moto)
        else:
            self.total_vagas_livres_moto += 1
            self.vagas_de_moto[moto.id_vaga_estacionado].desocupar(moto)


    #def estado_estacionamento():

    # def __str__(self):
        #return f"{self.name} is {self.age} years old"


estacionamento = Estacionamento(4,1,3)
carro1 = Carro('###111')
carro1.estacionar(estacionamento)

carro2 = Carro('###222')
carro2.estacionar(estacionamento)


moto1 = Moto('***111')
moto1.estacionar(estacionamento)

moto2 = Moto('***222')
moto2.estacionar(estacionamento)

moto3 = Moto('***333')
moto3.estacionar(estacionamento)

carro2.sair_da_vaga()

carro3 = Carro('###333')
carro3.estacionar(estacionamento)













    




