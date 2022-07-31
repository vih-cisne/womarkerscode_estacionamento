import functools
from Vaga import Vaga
from Carro import Carro
from Moto import Moto

### Os prints de testes estão o final desse arquivo

class Estacionamento:
    def __init__(self, qtd_vagas, qtd_vagas_de_moto , qtd_vagas_de_carro ):
        self.qtd_vagas = qtd_vagas
        self.vagas_de_moto = [Vaga(x,'moto') for x in range(qtd_vagas_de_moto)]
        self.vagas_de_carro = [ Vaga(x,'carro') for x in range(qtd_vagas_de_moto, qtd_vagas_de_carro+qtd_vagas_de_moto)]
        self.carros_para_vaga = []
        self.motos_para_vaga = []
        self.total_vagas_livres_carro = qtd_vagas_de_carro
        self.total_vagas_livres_moto = qtd_vagas_de_moto

    def receber_veiculo(self,veiculo):
        if(veiculo.tipo == 'carro'):
            return estacionamento.estacionar_carro(veiculo)
        elif(veiculo.tipo == 'moto'):
            return estacionamento.estacionar_moto(veiculo)

    def despedir_veiculo(self,veiculo):
        if(veiculo.tipo == 'carro'):
            return self.remover_carro(veiculo)
            
        elif(veiculo.tipo == 'moto'):
            return self.remover_moto(veiculo)

    def atualizar_qtd_vagas_moto_livres(self):
        self.total_vagas_livres_moto = functools.reduce(lambda a, b: a+1 if b.livre else a, self.vagas_de_moto,0)

    def atualizar_qtd_vagas_carro_livres(self):
        self.total_vagas_livres_carro = functools.reduce(lambda a, b: a+1 if b.livre else a, self.vagas_de_carro,0)

    def estacionar_carro(self,carro):
        self.carros_para_vaga.append(carro)

        if(self.total_vagas_livres_carro > 0):
            for index, vaga in enumerate(self.vagas_de_carro):
                if vaga.livre == True:
                    break
                #index -1 se não encontrado (segunda verificação)?
            self.vagas_de_carro[index].ocupar(carro)
            self.carros_para_vaga.pop(0)
            #self.total_vagas_livres_carro -= 1
            #poderia simplesmente ir atualizando a quantidade de vagas ao estacionar e retirar veiculo usando +=1 ou -=1 mas usei os métodos para praticar
            self.atualizar_qtd_vagas_carro_livres()
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
                
            self.vagas_de_moto[index].ocupar(moto)
            self.motos_para_vaga.pop(0)
            self.atualizar_qtd_vagas_moto_livres()
            return index  

        elif(self.total_vagas_livres_carro > 0):
            for index, vaga in enumerate(self.vagas_de_carro):
                if vaga.livre == True:
                    break

            self.vagas_de_carro[index].ocupar(moto)
            self.motos_para_vaga.pop(0)
            self.atualizar_qtd_vagas_carro_livres()
            return index

        else:
            print(f'Desculpa, não há vagas disponíveis no momento.')
            self.motos_para_vaga.pop(0)

    def remover_carro(self,carro):
        self.vagas_de_carro[carro.id_vaga_estacionado].desocupar(carro)
        self.atualizar_qtd_vagas_carro_livres()

    def remover_moto(self,moto):
        if(moto.id_vaga_estacionado >= len(self.vagas_de_moto)):
            self.vagas_de_carro[moto.id_vaga_estacionado].desocupar(moto)
            self.atualizar_qtd_vagas_carro_livres()
        else:
            self.vagas_de_moto[moto.id_vaga_estacionado].desocupar(moto)
            self.atualizar_qtd_vagas_moto_livres()

    # estado_estacionamento segue a mesma ideia do metodo __str__ ? retornando dados sobre o estacionamento
    #def estado_estacionamento():

    def __str__(self):
        self.atualizar_qtd_vagas_moto_livres()
        self.atualizar_qtd_vagas_carro_livres()
        return f'Estacionamento - vagas livres de carro: {self.total_vagas_livres_carro} - vagas livres de moto: {self.total_vagas_livres_moto} - total vagas livres: {self.total_vagas_livres_carro + self.total_vagas_livres_moto} '


estacionamento = Estacionamento(4,1,3)
carro1 = Carro('###111')
print(estacionamento)
carro1.estacionar(estacionamento)
print(estacionamento)

carro2 = Carro('###222')
carro2.estacionar(estacionamento)


moto1 = Moto('***111')
print(moto1)
print(estacionamento.vagas_de_moto[0])
moto1.estacionar(estacionamento)
print(moto1)
print(estacionamento.vagas_de_moto[0])

moto2 = Moto('***222')
moto2.estacionar(estacionamento)

moto3 = Moto('***333')
moto3.estacionar(estacionamento)

carro2.sair_da_vaga(estacionamento)


carro3 = Carro('###333')
carro3.estacionar(estacionamento)






#testes com metodos de listas

#print(sum(map(lambda x : 1 if x.livre else 0, estacionamento.vagas_de_carro)))
#print(functools.reduce(lambda a, b: a+1 if b.livre else a, estacionamento.vagas_de_carro,0))
















    




