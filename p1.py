import datetime

def main():
    
    options = {
        1: "Ver o status do sistema",
        2: "Exibir uma mensagem de saudação",
        3: "Mostrar a data e hora atuais",
        4: "Sair do programa",
       
    }
    
    while True:
       
        print("\nEscolha uma das seguintes opções:")
        for key, value in options.items():
            print(f"{key}: {value}")
        
        try:
         
            choice = int(input("Digite o número da sua escolha: "))
            
            if choice == 1:

                print("O sistema está funcionando corretamente.")

            elif choice == 2:
                print("Have a nice day!")

            elif choice == 3:
                now = datetime.datetime.now()

                print(f"A data e hora atuais são: {now}")
            elif choice == 4:
                print("Até logo!")

           
          
           
                 

                break
            else:
                print("Escolha inválida. Por favor, tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

if __name__ == "__main__":
    main()

