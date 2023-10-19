menu1_print = "1 - Cadastro de candidato \n 2 - Verificar Compatibilidade de Candidatos \n 3 - Remover Candidato \n "
menu2_print = "4 - Ver Candidatos Cadastrados \n 5 - Voltar ao Menu Anterior \n 6 - Encerrar Programa \n "
'Por favor, insira a opção desejada:'
# Função para cadastrar um candidato
def cadastrar_candidato():
    print("=== Cadastro de Candidato ===")
    nome = input("Nome do candidato(a): ")
    nota_entrevista = float(input("Nota da entrevista: "))
    nota_teste_teorico = float(input("Nota do teste teórico: "))
    nota_teste_pratico = float(input("Nota do teste prático: "))
    nota_soft_skills = float(input("Nota da avaliação de Soft Skills: "))

    candidato = {
        'Nome': nome,
        'Entrevista': nota_entrevista,
        'Teste Teórico': nota_teste_teorico,
        'Teste Prático': nota_teste_pratico,
        'Soft Skills': nota_soft_skills
    }

    candidatos.append(candidato)
    print("Candidato cadastrado com sucesso!")

# Função para verificar a compatibilidade dos candidatos
def verificar_compatibilidade():
    nota_entrevista = float(input("Nota da entrevista: "))
    nota_teorico = float(input("Nota do teste teórico: "))
    nota_pratico = float(input("Nota do teste prático: "))
    nota_soft_skills = float(input("Nota da avaliação de Soft Skills: "))

    candidatos_compativeis = []

    for candidato in candidatos:
        if (
            nota_entrevista <= candidato['Entrevista']
            and nota_teorico <= candidato['Teste Teórico']
            and nota_pratico <= candidato['Teste Prático']
            and nota_soft_skills <= candidato['Soft Skills']
        ):
            candidatos_compativeis.append(candidato)

    if candidatos_compativeis:
        print("Os candidatos abaixo são compatíveis:")
        for candidato in candidatos_compativeis:
            nome = candidato['Nome']
            nota_entrevista_candidato = candidato['Entrevista']
            nota_teorico_candidato = candidato['Teste Teórico']
            nota_pratico_candidato = candidato['Teste Prático']
            nota_soft_skills_candidato = candidato['Soft Skills']
            notas = f"e{nota_entrevista_candidato}_t{nota_teorico_candidato}_p{nota_pratico_candidato}_s{nota_soft_skills_candidato}"
            print(f"Nome: {nome}, Notas: {notas}")
    else:
        print("Nenhum candidato compatível encontrado.")





# Função para remover um candidato com base no nome
def remover_candidato():
    nome = input("Digite o nome do candidato que deseja remover: ")
    global candidatos
    for candidato in candidatos:
        if candidato['Nome'] == nome:
            candidatos.remove(candidato)
            print(f"{nome} foi removido com sucesso.")
            return
    print(f"Candidato com o nome {nome} não encontrado.")

# Função para listar todos os candidatos cadastrados
def ver_candidatos_cadastrados():
    if not candidatos:
        print("Nenhum candidato cadastrado.")
        return
    print("Candidatos Cadastrados:")
    for candidato in candidatos:
        print(f"Nome: {candidato['Nome']}, Entrevista: {candidato['Entrevista']}, Teórico: {candidato['Teste Teórico']}, Prático: {candidato['Teste Prático']}, Soft Skills: {candidato['Soft Skills']}")

# Função para voltar ao menu anterior (não faz nada)
def voltar_ao_menu_anterior():
    return

# Função para encerrar o programa
def encerrar_programa():
    global programa_rodando
    programa_rodando = False
    print("Programa encerrado.")

# Inicialização de variáveis
candidatos = []
programa_rodando = True

# Loop principal do programa
while programa_rodando:
    print("\n=== Menu ===")
    print("1 - Cadastro de Candidato")
    print("2 - Verificar Compatibilidade de Candidatos")
    print("3 - Remover Candidato")
    print("4 - Ver Candidatos Cadastrados")
    print("5 - Voltar ao Menu Anterior")
    print("6 - Encerrar Programa")

    opcao = input("Por favor, insira a opção desejada: ")

    if opcao == "1":
        cadastrar_candidato()
    elif opcao == "2":
        verificar_compatibilidade()
    elif opcao == "3":
        remover_candidato()
    elif opcao == "4":
        ver_candidatos_cadastrados()
    elif opcao == "5":
        voltar_ao_menu_anterior()
    elif opcao == "6":
        encerrar_programa()
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
