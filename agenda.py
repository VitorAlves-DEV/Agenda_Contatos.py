# Agenda de Contatos
def adicionar_contato(contatos):
    contato = {
        "nome": "",
        "telefone": "",
        "email": "",
        "favorito": False
    }

    print("\nAdicionar contato")
    contato["nome"] = input("Nome: ")
    contato["telefone"] = input("Telefone: ")
    contato["email"] = input("Email: ")
    return contato

def listar_contatos(contatos):
    if not contatos:
        print("Nenhum contato cadastrado.")
    else:
        print("\nContatos cadastrados:")
        for nome, info in contatos.items():
            print(f"Nome: {nome}, Telefone: {info['telefone']}, Email: {info['email']}, Favorito: {'Sim' if info['favorito'] else 'Não'}")

def editar_contato(contatos):
    nome = input("Digite o nome do contato a ser editado: ")
    if nome in contatos:
        print("Editando contato:")
        contatos[nome]["nome"] = input("Novo nome: ")
        contatos[nome]["telefone"] = input("Novo telefone: ")
        contatos[nome]["email"] = input("Novo email: ")
        print("Contato editado com sucesso!")
    else:
        print("Contato não encontrado.")

def marcar_favorito(contatos):
    nome = input("Digite o nome do contato a ser marcado como favorito: ")
    if nome in contatos:
        contatos[nome]["favorito"] = True
        print("Contato marcado como favorito!")
    else:
        print("Contato não encontrado.")

def desmarcar_favorito(contatos):
    nome = input("Digite o nome do contato a ser desmarcado como favorito: ")
    if nome in contatos:
        contatos[nome]["favorito"] = False
        print("Contato desmarcado como favorito!")
    else:
        print("Contato não encontrado.")

def listar_favoritos(contatos):
    favoritos = {nome: info for nome, info in contatos.items() if info["favorito"]}
    if not favoritos:
        print("Nenhum contato favorito.")
    else:
        print("Contatos favoritos:")
        for nome, info in favoritos.items():
            print(f"Nome: {nome}, Telefone: {info['telefone']}, Email: {info['email']}")

contatos = {}

while True:
    print("\nAgenda de Contatos")
    print("1. Adicionar contato")
    print("2. Listar contatos cadastrados")
    print("3. Editar contato")
    print("4. Marcar contato como favorito")
    print("5. Desmarcar contato como favorito")
    print("6. Listar contatos favoritos")
    print("7. Sair")

    escolha = input("Escolha uma opção 1-7: ")
    if escolha == "1":
        contato = adicionar_contato(contatos)
        if contato is not None:
            contatos[contato["nome"]] = contato
            print("Contato adicionado com sucesso!")
    elif escolha == "2":
        listar_contatos(contatos)
    elif escolha == "3":
        editar_contato(contatos)
    elif escolha == "4":
        marcar_favorito(contatos)
    elif escolha == "5":
        desmarcar_favorito(contatos)
    elif escolha == "6":
        listar_favoritos(contatos)
    elif escolha == "7":
        print("\nSaindo da agenda...")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
    