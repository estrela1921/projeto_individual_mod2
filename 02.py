# Função para cadastrar um candidato
def cadastrar_candidato():
    print("=== Cadastro de Candidato ===")
    nome = input("Nome do candidato(a): ")
    nota_entrevista = float(input("Nota da entrevista: "))
    nota_teste_teorico = float(input("Nota do teste teórico: "))
    nota_teste_pratico = float(input("Nota do teste prático: "))
    nota_soft_skills = float(input("Nota da avaliação de Soft Skills:"))

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

        compatibilidade = abs(candidato['Entrevista'] - nota_entrevista) + abs(
            candidato['Teste Teórico'] - nota_teorico) + abs(candidato['Teste Prático'] - nota_pratico) + abs(
            candidato['Soft Skills'] - nota_soft_skills)

        if compatibilidade <= 8:  # Defina seu próprio limite de compatibilidade
            candidatos_compativeis.append(candidato)
    if candidatos_compativeis:
        print("Candidatos compatíveis:")
        for candidato in candidatos_compativeis:
            notas_formatadas = f"e{candidato['Entrevista']:.0f}_t{candidato['Teste Teórico']:.0f}_p{candidato['Teste Prático']:.0f}_s{candidato['Soft Skills']:.0f}"
            print(f"\n{candidato['Nome']}: {notas_formatadas}")

    else:
        print("Nenhum candidato compatível encontrado.")

    # Código para calcular a similaridade (você pode adicionar essa parte se necessário)

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

# Inicialização de variáveis com candidatos e seus resultados
candidato1 = {
    'Nome': 'Roberta',
    'Entrevista': 5.0,
    'Teste Teórico': 10.0,
    'Teste Prático': 8.0,
    'Soft Skills': 8.0
}

candidato2 = {
    'Nome': 'Angelina',
    'Entrevista': 6.0,
    'Teste Teórico': 9.0,
    'Teste Prático': 7.0,
    'Soft Skills': 7.0
}

candidato3 = {
    'Nome': 'Giuseppe',
    'Entrevista': 4.0,
    'Teste Teórico': 8.0,
    'Teste Prático': 9.0,
    'Soft Skills': 9.0
}

candidato4 = {
    'Nome': 'Luiggi',
    'Entrevista': 7.0,
    'Teste Teórico': 7.0,
    'Teste Prático': 6.0,
    'Soft Skills': 6.0
}

candidato5 = {
    'Nome': 'Gilberto',
    'Entrevista': 8.0,
    'Teste Teórico': 6.0,
    'Teste Prático': 5.0,
    'Soft Skills': 5.0
}

# Adicione os candidatos iniciais à lista de candidatos
candidatos.extend([candidato1, candidato2, candidato3, candidato4, candidato5])

# Loop principal do programa
programa_rodando = True
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


    
    
   

   
