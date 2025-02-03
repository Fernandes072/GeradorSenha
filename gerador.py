import argparse
from unidecode import unidecode
import string

def lettersToCharacters(password): # Substitui letras por caracteres especiais
    characters = {'a': '@', 'e': '&', 'S': '$', 's': '$', 'E': '3', 'H': '#', 'i': '!', 
                  'A': '4', 'B': '8', 'O': '0', 'X': '%', 'Z': '2', 'u': '-', 'U': '_'}
    result = ""
    for letter in password:
        if letter in characters: # Verifica se a letra é uma chave no dicionário characters
            result += characters[letter] # Adiciona o valor da chave no resultado
        else:
            result += letter
    return result

def removePair(password): # Remove palavras de posição par
    password = password.split(" ")
    password = password[0::2] # Começa do índice 0 e pula de 2 em 2
    password = " ".join(password) # Junta as palavras colocando um espaço entre elas
    return password

def removeOdd(password): # Remove palavras de posição ímpar
    password = password.split(" ")
    password = password[1::2] # Começa do índice 1 e pula de 2 em 2
    password = " ".join(password) # Junta as palavras colocando um espaço entre elas
    return password

def upperLowerCase(password): # Alterna maiúsculas e minúsculas
    i = 0
    result = ""
    for letter in password:
        if i % 2 == 0:
            result += letter.upper()
        else:
            result += letter.lower()
        i += 1
    return result

def removeMiddle(password):
    password = password.split(" ")
    result = []
    for word in password:
        result.append(word[0] + word[-1]) # Pega a primeira e a última letra da palavra
    password = " ".join(result) # Junta as palavras colocando um espaço entre elas
    return password

def numberWord(password):
    result = password.split(" ")
    n = 0
    for i in range((len(result) - 1), -1, -1): # Vai da última palavra até a primeira
        if n == 10:
            n = 0
        result[i] = str(n) + result[i] # Adiciona o número no início da palavra
        n += 1
    password = " ".join(result) # Junta as palavras colocando um espaço entre elas
    return password

def passwordLength(password, size): # Ajuste do tamanho da senha
    if len(password) < size:
        raise Exception("Texto insuficiente para gerar a senha")
    result = ""
    for i in range(size):
        result += password[i]
    return result

def generatePassword(text, parameters, size): # Gera a senha
    parameters = parameters.split(" ") # Separa os parâmetros
    password = unidecode(text) # Remove acentos
    password = password.translate(str.maketrans("", "", string.punctuation)) # Remove pontuação
    for parameter in parameters:
        if parameter == "1":
            password = lettersToCharacters(password)
        elif parameter == "2":
            password = removePair(password)
        elif parameter == "3":
            password = removeOdd(password)
        elif parameter == "4":
            password = upperLowerCase(password)
        elif parameter == "5":
            password = removeMiddle(password)
        elif parameter == "6":
            password = numberWord(password)
    password = password.replace(" ", "")
    password = passwordLength(password, int(size))
    return password

def arguments(): # Pega os argumentos passados pelo terminal
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--text", required=False, default="")
    parser.add_argument("-p", "--parameters", required=False, default="")
    parser.add_argument("-s", "--size", required=False, default="")

    args = parser.parse_args()
    if len(args.text) < 1: # Verifica se o texto foi informado
        raise Exception("Texto não informado")
    if len(args.parameters) < 1: # Verifica se os parâmetros foram informados
        raise Exception("Parâmetros não informados")
    if len(args.size) < 1: # Verifica se o tamanho da senha foi informado
        raise Exception("Tamanho da senha não informado")
    return parser.parse_args()

def main():
    try:
        args = arguments()
        text = args.text # Texto para formar a senha
        parameters = args.parameters # Parâmetros para formar a senha
        size = args.size # Tamanho da senha

        print("Texto:", text)
        print("Parâmetros:", parameters)
        print("Tamanho:", size)
        print("Senha:", generatePassword(text, parameters, size))
    except Exception as e:
        print("Erro:", e)


# 1 - Substitui letras por caracteres especiais
# 2 - Remove palavras de posição par
# 3 - Remove palavras de posição ímpar
# 4 - Alterna maiúsculas e minúsculas
# 5 - Remove o meio das palavras
# 6 - Coloca um número no início de cada palavra

# python gerador.py -t "Transformers é uma franquia cinematográfica de ficção científica baseada na linha de brinquedos homônima criada pela Hasbro. Desde sua estreia, em 2007, a série tem sido distribuída pela Paramount Pictures e DreamWorks." -p "5 6 2 1" -s "8"
if __name__ == '__main__':
    main()