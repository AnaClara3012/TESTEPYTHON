
alunos = []

while True:
    print("\n===== SISTEMA DE CADASTRO DE ALUNOS =====")
    print("1 - Cadastrar aluno")
    print("2 - Listar todos os alunos")
    print("3 - Pesquisar aluno por nome")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome do aluno: ")
        idade = input("Digite a idade do aluno: ")
        curso = input("Digite o curso do aluno: ")

        aluno = {"nome": nome, "idade": idade, "curso": curso}
        alunos.append(aluno)
        print(f"✅ Aluno {nome} cadastrado com sucesso!")

    elif opcao == "2":
        if len(alunos) == 0:
            print("⚠ Nenhum aluno cadastrado ainda.")
        else:
            print("\n--- LISTA DE ALUNOS ---")
            for i, aluno in enumerate(alunos, 1):
                print(f"{i}. Nome: {aluno['nome']} | Idade: {aluno['idade']} | Curso: {aluno['curso']}")

    elif opcao == "3":
        busca = input("Digite o nome do aluno que deseja pesquisar: ")
        encontrado = False
        for aluno in alunos:
            if aluno["nome"].lower() == busca.lower():
                print(f"🎓 Aluno encontrado: Nome: {aluno['nome']} | Idade: {aluno['idade']} | Curso: {aluno['curso']}")
                encontrado = True
                break
        if not encontrado:
            print("⚠ Aluno não encontrado.")

    elif opcao == "4":
        print("👋 Saindo do sistema... Até mais!")
        break

    else:
        print("❌ Opção inválida! Tente novamente.")
