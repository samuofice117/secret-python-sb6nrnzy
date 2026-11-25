import negocio

while True: 
      print("\n1 - Cadastrar aluno")
      print("2 - Listar alunos")
      print("3-Sair")

      op = inpot("Escolha: ")

      if op == "1":
        nome=input("Escolha: ")
        print(negocio.casdastrar_aluno(nome))

      elif op == "2":
        lista = negocio.obter_alunos()
        print("Alunos:" , lista)

        elif op == "3":
          print ("Encerrando...")
          break