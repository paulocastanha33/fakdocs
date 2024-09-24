# Instalar a biblioteca Faker
# pip3 install Faker
from faker import Faker
import random

# Função para gerar um CPF válido (baseado no algoritmo de validação de CPF)
# Fonte:https://www.vivaolinux.com.br/script/Validador-e-gerador-de-CPF-em-Python#:~:text=Duas%20fun%C3%A7%C3%B5es%20em%20Python%2C%20uma,que%20gera%20um%20CPF%20v%C3%A1lido.&text=from%20random%20import%20randint%20def,d%C3%ADgitos%20if%20len(cpf)%20!%3D
def gerar_cpf():
    def calcular_digito(digs):
        soma = sum([v * (len(digs)+1-i) for i, v in enumerate(digs)])
        digito = 11 - (soma % 11)
        return digito if digito < 10 else 0

    base_cpf = [random.randint(0, 9) for _ in range(9)]
    digito1 = calcular_digito(base_cpf)
    digito2 = calcular_digito(base_cpf + [digito1])
    cpf = ''.join(map(str, base_cpf)) + str(digito1) + str(digito2)
    return f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'

# Criar o objeto Faker com localidade do Brasil
fake = Faker('pt_BR')

# Função para gerar os dados fictícios
def gerar_informacoes_ficticias():
    nome_completo = fake.name()
    cpf = gerar_cpf()
    email = fake.email()
    endereco = fake.address()
    telefone = fake.phone_number()

    # Exibição estruturada dos dados
    print(f"{'-'*30}")
    print(f"Nome Completo: {nome_completo}")
    print(f"CPF: {cpf}")
    print(f"E-mail: {email}")
    print(f"Endereço: {endereco}")
    print(f"Telefone: {telefone}")
    print(f"{'-'*30}")

# Função principal para o loop de repetição
def main():
    while True:
        gerar_informacoes_ficticias()
        opcao = input("Deseja gerar novamente? (s para sim, n para não): ").lower()
        if opcao != 's':
            print("Saindo...")
            break

# Execução do programa
if __name__ == "__main__":
    main()
