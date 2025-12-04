from mysql.connector import connect

def executar():
    #criar_categoria()
    # listar_categorias()
    # editar_categoria()
    apagar_categoria()
    print('Obrigado')

def criar_categoria():
    nome = input ("Digite o nome da nova categoiria: ")

    print("Abrindo conexão com banco de dados")

    # Abrir a conexão com o banco de dados
    conexao = connect(
        host="127.0.0.1",
        port="3306",
        user="root",
        password="rootlipe",
        database="mercado",
    )
    # Criando um cursor para poder executar comandos do banco de dados
    cursor = conexao.cursor()
    # Definir qual comando será executado
    sql = "INSERT INTO categorias (nome) VALUES (%s)"
    dados = (nome,)

    cursor.execute(sql, dados)

    # Confirmar o comando (concretizar o comando de insert)
    conexao.commit()

    # Fechar a conexao com o banco de dados do cursor
    cursor.close()

    print("Categoria criada com sucesso")

def listar_categorias():
    conexao = connect(
        host="127.0.0.1",
        port="3306",
        user="root",
        password="rootlipe",
        database="mercado",
    )
    cursor = conexao.cursor()
    
    cursor.execute("SELECT id, nome FROM categorias")

    registros = cursor.fetchall()

    cursor.close()
    conexao.close()

    for registro in registros:
        id = registro[0]
        nome = registro[1]
        print("ID:", id, "\tNOME:", nome)

def editar_categoria():
    listar_categorias()

    id = input("Digite o id que deseja editar: ")
    nome = input("Digite o novo nome: ")

    conexao = connect(
        host="127.0.0.1",
        port="3306",
        user="root",
        password="rootlipe",
        database="mercado",
    )
    cursor = conexao.cursor()
    
    sql = "UPDATE categorias SET nome=%s WHERE id = %s"
    dados = (nome, id)

    cursor.execute(sql, dados)

    conexao.commit()

    cursor.close()
    
    conexao.close()


def apagar_categoria():
    listar_categorias()

    id = input("Digite o id que deseja apagar: ")

    print("Abrindo conexão com banco de dados")
    conexao = connect(
        host="127.0.0.1",
        port="3306",
        user="root",
        password="rootlipe",
        database="mercado",
    )

    print("Conexao aberta com sucesso")
    cursor = conexao.cursor()

    print("Apagando categoria")
    sql = "DELETE FROM categorias WHERE id = %s"
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

    print("Categoria apagada com sucesso")
    
    