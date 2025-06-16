import random
import string
#Gerador de Senha: Pergunta quais os requisitos para a senha, e evita provaveis padrões
def gerar_senha():
    #Inicio do codigo
    print("--- GERADOR DE SENHAS ---")
    #Perguntar o tamanho da senha desejada usando Try..Except
    try:
        tamanho = int(input("Digite o tamanho da senha: "))
    except ValueError:
        print("Entrada inválida, por favor digite um número inteiro.")
        return
        #Perguntar preferencias que o usuário quer na senha
    usar_maiusculas = input("Incluir letras maiúsculas? (S/N): ").lower() == 's'
    usar_numeros = input("Incluir numeros? (S/N): ").lower() == 's'
    usar_simbolos = input("Incluir simbolos? (S/N): ").lower() == 's'
    #Validar os caracteres, letras minusculas são obrigatórias
    caracteres_validos = string.ascii_lowercase
    if usar_maiusculas:
        caracteres_validos += string.ascii_uppercase
    if usar_numeros:
        caracteres_validos += string.digits
    if usar_simbolos:
        caracteres_validos += string.punctuation
    #Gerando senha
    senha_garantida = []
    caracteres_restantes = []
    #Adiciona um caractere garantido para cada opção
    if usar_maiusculas:
        senha_garantida.append(random.choice(string.ascii_uppercase))
    if usar_numeros:
        senha_garantida.append(random.choice(string.digits))
    if usar_simbolos:
        senha_garantida.append(random.choice(string.punctuation))
    #Adicionado o caractere minúsculo obrigatório
    senha_garantida.append(random.choice(string.ascii_lowercase))
    #calcula o que falta na senha
    tamanho_restante = tamanho - len(senha_garantida)
    #Preenche o resto da senha
    for _ in range(tamanho_restante):
        caracteres_restantes.append(random.choice(caracteres_validos))
    #Junta a lista com o resto
    senha_final_list = senha_garantida + caracteres_restantes
    #Embaralha a lista final novamente
    random.shuffle(senha_final_list)
    #Tranformar a lista de caracteres em uma string
    senha_final = "".join(senha_final_list)

    print("-"*35) #repete 35 vezes o '-'
    print(f"Sua nova senha é: {senha_final}")
    print("-"*35)
if __name__ == "__main__":
    gerar_senha()