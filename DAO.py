from Models import *


class DaoCategoria:
    
    @classmethod
    def salvar(cls, categoria):
        with open('categoria.txt', 'a') as arq:
            arq.writelines(categoria)
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('categoria.txt', 'r') as arq:
            cls.categoria = arq.readlines()

        # retirando o \n do print
        cls.categoria = list(map(lambda x: x.replace('\n', ''), cls.categoria))

        catg = []
        for i in cls.categoria:
            catg.append(Categoria(i))
        #print(cls.categoria)
        return catg


class DaoVenda:
    @classmethod
    def salvar(cls, venda: Venda):
        with open('venda.txt', 'a') as arq:
            arq.writelines(venda.itensVendido.nome + "|" + venda.itensVendido.preco + "|" +
                           venda.itensVendido.categoria + "|" + venda.vendedor + "|" + venda.comprador + "|" +
                           str(venda.qtdoVendida) + "|" + venda.data)
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('venda.txt', 'r') as arq:
            cls.venda = arq.readlines()

        # retirando o \n do print
        cls.venda = list(map(lambda x: x.replace('\n', ''), cls.venda))
        # retirando o pip para criar uma lista de itens vendidos
        cls.venda = list(map(lambda x: x.split('|'), cls.venda))

        vendidos = []
        for i in cls.venda:
            vendidos.append(Venda(Produtos(i[0], i[1], i[2]), i[3], i[4], i[5], i[6]))

        return vendidos


class DaoEstoque:
    @classmethod
    def salvar(cls, produto: Produtos, quantidade):
        with open('estoque.txt', 'a') as arq:
            arq.writelines(produto.nome + "|" + produto.preco + "|" +
                           produto.categoria + "|" + str(quantidade))
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('estoque.txt', 'r') as arq:
            cls.estoque = arq.readlines()

        cls.estoque = list(map(lambda x: x.replace('\n', ''), cls.estoque))
        cls.estoque = list(map(lambda x: x.split('|'), cls.estoque))
        est = []

        if len(cls.estoque) > 0:
            for i in cls.estoque:
                est.append(Estoque(Produtos(i[0], i[1], i[2], i[3])))

        return est


class DaloFornecedor:
    @classmethod
    def salvar(cls, fornecedor :Fornecedor):
        with open('fornecedores.txt','a') as arq:
            arq.writelines(fornecedor.nome + "|" + fornecedor.cnpf + "|" + fornecedor.telefone
                           + "|" + fornecedor.categoria)
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('fornecedores.txt', 'r') as arq:
            cls.fornecedores = arq.readlines()

        cls.fornecedores = list(map(lambda x: x.replace('\n', ''), cls.fornecedores))
        cls.fornecedores = list(map(lambda x: x.split('|'), cls.fornecedores))

        forn = []
        for i in cls.fornecedores:
            forn.append(Fornecedor(i[0], i[1], i[2], i[3]))

        return forn


class DaoPessoa:
    @classmethod
    def salvar(cls, pessoas: Pessoa):
        with open('clientes.txt', 'a') as arq:
            arq.writelines(pessoas.nome + "|" + pessoas.telefone + "|" , pessoas.cpf
                           + "|" + pessoas.email + "|" + pessoas.endereco)
            arq.writelines('\n')

        cls.clientes = list(map(lambda x: x.replace('\n', ''), cls.clientes))
        cls.clientes = list(map(lambda x: x.split('|'), cls.clientes))

        clientes = []

        for i in cls.clientes:
            clientes.append(Pessoa(i[0], i[1], i[2], i[3], i [4]))

        return clientes

class DaoFuncionario:
    @classmethod
    def salvar(cls, funcionario : Funcionario):
        with open('funcionarios.txt', 'a') as arq:
            arq.writelines(funcionario.clt + "|" + funcionario.nome + "|" + funcionario.telefone
                           + "|" + funcionario.cpf + "|" + funcionario.email + "|" + funcionario.endereco)
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('funcionarios.txt', 'r') as arq:
            cls.funcionarios = arq.readlines()
        # retirando o \n do print
        cls.funcionarios = list(map(lambda x: x.replace('\n', ''), cls.funcionarios))
        # retirando o pip para criar uma lista de itens vendidos
        cls.funcionarios = list(map(lambda x: x.split('|'), cls.funcionarios))

        funcionario = []
        for i in cls.funcionarios:
            funcionario.append(Funcionario(i[0], i[1], i[2], i[3], i[4], i[5]))

        return funcionario

    

