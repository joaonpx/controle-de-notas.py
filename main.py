from grades import display

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

        gradesAmount = len(grades)

        # verificando se existem notas na lista
        if gradesAmount > 0:
          print(f"Notas cadastradas: {gradesAmount}\n")

          # exibindo todas as notas com índice
          display(grades)

          print("\nÍNDICE = NÚMERO QUE ESTÁ ENTRE []")
          
          gradeSelection = input(f"\nDigite o índice da nota que deseja excluir, ALL para exluir todas as notas ou CANCEL para cancelar: ")

          # verificando se o úsuario quer excluir todas ou só uma nota
          if gradeSelection.upper() == "ALL":
            # excluindo todas as notas
            grades.clear()
            
            print(f"\nTodas as notas foram excluídas com sucesso! 🎉")

          elif gradeSelection.upper() == "CANCEL":
            print(f"\nExclusão cancelada!")

          else:
            # deletando a nota escolhida
            del grades[int(gradeSelection)]

            print(f"\nNota excluída com sucesso! 🎉")
            
        else:
          print("Nenhuma nota cadastrada! \nSelecione a opção 1 para inserir uma nova nota.")
    
    # 3 opção
    elif option == 3:
        print("\n------------------------- NOTAS -------------------------\n")

        gradesAmount = len(grades)

        # verificando se existem notas na lista
        if gradesAmount > 0:
          # exibindo total de notas
          print(f"Notas cadastradas: {gradesAmount}\n")

          # exibindo todas as notas com índice
          display(grades)

        else:
          print("Nenhuma nota cadastrada! \nSelecione a opção 1 para inserir uma nova nota.")

    # 4 opção
    elif option == 4:
        print("\n------------------------- MÉDIA -------------------------\n")

        gradesAmount = len(grades)

        # verificando se existem notas na lista
        if gradesAmount > 0:
          # calculando média
          average = sum(grades) / gradesAmount

          # exibindo média
          print(f"A média é de: {average}")
        else:
          print("Nenhuma nota cadastrada! \nSelecione a opção 1 para inserir uma nova nota.")
    
    elif option > 4:
        print(f"\nOpção inválida! Tente novamente.")