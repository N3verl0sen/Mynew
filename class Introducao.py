class Introducao:
    def __init__(self, nome, profissao, interesses):
        self.nome = nome
        self.profissao = profissao
        self.interesses = interesses

    def se_apresentar(self):
        apresentacao = f"Olá, meu nome é {self.nome}.\n"
        apresentacao += f"Eu sou {self.profissao}.\n"
        apresentacao += "Meus interesses incluem:\n"
        for interesse in self.interesses:
            apresentacao += f"- {interesse}\n"
        return apresentacao

# Dados do usuário
nome = "n3verl0sen"
profissao = "desenvolvedor de jogos"
interesses = ["desenvolvimento de jogos", "programação", "aprender novas tecnologias"]

# Criação do objeto de introdução
minha_introducao = Introducao(nome, profissao, interesses)

# Exibindo a apresentação
print(minha_introducao.se_apresentar())
