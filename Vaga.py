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
            
        print(f'Sucesso! {veiculo.tipo.capitalize()} de placa {veiculo.placa} estacionado(a) na vaga de número {self.id}.', mensagem_adicional)

    def desocupar(self, veiculo):
        self.livre = True
        self.placa = None

        print(f'{veiculo.tipo.capitalize()} de placa {veiculo.placa} acabou de sair da vaga de número {self.id}')
    
    def __str__(self) -> str:

        mensagem_livre = ('não', 'sim')[self.livre]
        mensagem_placa = (f' - placa: {self.placa}','')[self.livre]
        return f'Vaga - nº: {self.id} - tipo: {self.tipo} - livre: {mensagem_livre} {mensagem_placa}'