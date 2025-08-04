try: 
    idade = int(input("Informe a sua idade: "))
    print(f'Sua idade daqui a 10 anos sera: {idade + 10}')
except ValueError:
    print("Erro: Favor digitar um número!")