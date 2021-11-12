contatos_profissao1 = {'Yan': 'Advogado', 'Luis': 'Mordomo', 'Clara': 'Babá',
  'Victor': 'Desenvolvedor de Software'}

contatos_profissao = {'Robson': 'Bombeiro', 'Pedro': 'Programador', 'Ana': 'Design',
  'Marina': 'Freira'}

lista_telefonica = {}
def megadict(x, y):
    lista_telefonica = x | y
    return lista_telefonica

print(megadict(contatos_profissao1, contatos_profissao))

