from mysql.connector import connect

def executar_biblioteca():
    # cadastrar_livro()
    # apagar_livro()
    # editar_livro()
    listar_livros()

def cadastrar_livro():
    nome = input("Digite o nome do livro: ")
    quantidade = input("Digite a quantidade de paginas: ")

    conexao = connect(
        host="127.0.0.1",
        port="3306",
        user="root",
        password="rootlipe",
        database="biblioteca",
    )

    cursor = conexao.cursor()

    sql = "INSERT INTO livros (nome, quantidade_paginas) VALUES (%s, %s)"
    dados = (nome, quantidade)

    cursor.execute(sql, dados)

    conexao.commit()

    cursor.close()

    conexao.close()

    print("Livro cadastrado com sucesso")


def apagar_livro():
    listar_livros()

    id = input("Digite o id que deseja apagar: ")

    conexao = connect(
        host="127.0.0.1",
        port="3306",
        user="root",
        password="rootlipe",
        database="biblioteca",
    )

    cursor = conexao.cursor()

    sql = "DELETE FROM livros WHERE id = %s"
    dados = (id,)
    cursor.execute(sql, dados)
    conexao.commit()

    linas_afetadas = cursor.rowcount
    if linas_afetadas == 0:
        print("ID informado inexistente, tente novamente")
    else:
        print("Categoria apagada com sucesso")

    cursor.close()
    conexao.close()


def editar_livro():
    listar_livros()

    id = input("Digite o id que deseja editar: ")
    nome = input("Digite o nome do livro: ")
    quantidade = input("Digite a quantidade de paginas: ")

    conexao = connect(
        host="127.0.0.1",
        port="3306",
        user="root",
        password="rootlipe",
        database="biblioteca",
    )
    cursor = conexao.cursor()

    sql = "UPDATE livros SET nome = %s, quantidade_paginas = %s WHERE id = %s"
    dados = (nome, quantidade, id)

    cursor.execute(sql, dados)

    conexao.commit()

    cursor.close()
    conexao.close()


def listar_livros():
    conexao = connect(
        host="127.0.0.1",
        port="3306",
        user="root",
        password="rootlipe",
        database="biblioteca",
    )
    cursor = conexao.cursor()

    cursor.execute("SELECT id, nome, quantidade_paginas FROM livros")

    registros = cursor.fetchall()

    cursor.close()
    conexao.close()

    for registro in registros:
        id = registro[0]
        nome = registro[1]
        paginas = str(registro[2])
        print(f"ID: {id:<5}  NOME: {nome:<40}  PAGINAS: {paginas:<5}")