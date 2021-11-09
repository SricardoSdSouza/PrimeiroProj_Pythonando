from Models import *
from DAO import *
from datetime import datetime

class ControllerCategoria:
    def cadastraCategoria(self, novaCategoria):
        #criando uma variavel par saber sa acategoria ja existe
        existe = False
        x = DaoCategoria.ler()
        for i in x:
            if i.categoria == novaCategoria:
                existe = True
        if not existe:
            DaoCategoria.salvar(novaCategoria)
            print('Categoria cadastrada com sucesso!!!')
        else:
            print('A categoria que deseja cadastrar já existe ')

    def removerCategoria(self, categoriaRemover):
        x = DaoCategoria.ler()
        cat = list(filter(lambda x: x.categoria == categoriaRemover, x))

        if len(cat) <= 0:
            print('A Categoria que deseja Excluir não existe')
        else:
            for i in range(len(x)):
                # Foi removido somente da memoria RAM
                if x[i].categoria == categoriaRemover:
                    del x[i]
                    break
            print('A Categoria removida com sucesso :) !')
            #Removendo do arquivo
            with open('categoria.txt', 'w') as arq:
                for i in x:
                    arq.writelines(i.categoria)
                    arq.writelines('\n')


class ControllerProduto:
    pass

#a = ControllerCategoria()
#a.cadastraCategoria('Congelados')