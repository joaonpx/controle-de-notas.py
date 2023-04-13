grades = []

option = -1

while option != 0:
    print("\n----------------------------- MENU -----------------------------\n")
    print("1 - Inserir nota \n2 - Excluir nota \n3 - Exibir notas \n4 - Calcular média \n0 - Sair")

    option = int(input("\nEscolha uma opção: "))

    # 1 opção
    if option == 1:
        print("\n------------------------- INSERIR NOTA -------------------------\n")

        # adicionando nota a lista
        grades.append(input("Digite a nota: "))
    
    # 2 opção
    elif option == 2:
        print("\n--------------------- EXCLUIR NOTA ----------------------\n")

        # verificando se existem notas na lista
        if len(grades) > 0:
          print("Notas:\n")

          # exibindo todas as notas com índice
          for grade in grades:
            print(f"[{grades.index(grade)}]: {grade}")

          print("\nÍNDICE = NÚMERO QUE ESTÁ DENTRO DE []")
          
          gradePosition = input(f"\nDigite o índice da nota que deseja excluir ou ALL para exluir todas as notas: ")

          # verificando se o úsuario quer excluir todas ou só uma nota
          if gradePosition.upper() == "ALL":
            # armazenando a quantidade de notas antes de excluir
            gradesAmount = len(grades)

            # excluindo todas as notas
            grades.clear()
          
            print(f"\nTodas as {gradesAmount} notas foram excluídas com sucesso! 🎉")
          else:
            # deletando a nota escolhida
            del grades[int(gradePosition)]

            print("\nNota excluída com sucesso! 🎉")
        else:
          print("Nenhuma nota cadastrada! \nSelecione a opção 1 para inserir uma nova nota.")
    
    # 3 opção
    elif option == 3:
        print("\n------------------------- NOTAS -------------------------\n")

        # verificando se existem notas na lista
        if len(grades) > 0:
          # exibindo total de notas
          print(f"Notas cadastradas: {len(grades)}\n")

          # exibindo todas as notas com índice
          for grade in grades:
            print(f"{grades.index(grade)}: {grade}")
        else:
          print("Nenhuma nota cadastrada! \nSelecione a opção 1 para inserir uma nova nota.")

    # 4 opção
    elif option == 4:
        print("\n------------------------- MÉDIA -------------------------\n")

        # verificando se existem notas na lista
        if len(grades) > 0:
          # calculando média
          average = sum(grades) / len(grades)

          # exibindo média
          print(f"A média é de: {average}")
        else:
          print("Nenhuma nota cadastrada! \nSelecione a opção 1 para inserir uma nova nota.")