import argparse
from unidecode import unidecode

def generatePassword(text, parameters): #Gera a senha
    parameters = parameters.split(" ") #Separa os parâmetros
    password = unidecode(text)
    for parameter in parameters:
        if parameter == "1":
            password = password.replace("a", "@")
        elif parameter == "2":
            password = password.replace("e", "&")
        elif parameter == "3":
            password = password.split(" ")
            password = password[0::2]
            password = " ".join(password)
        elif parameter == "4":
            password = password.split(" ")
            password = password[1::2]
            password = " ".join(password)
    return password

def arguments(): #Pega os argumentos passados pelo terminal
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--text", required=True)
    parser.add_argument("-p", "--parameters", required=True)
    return parser.parse_args()

def showParameters():
    print("1 - Substitui a por @")
    print("2 - Substitui e por &")
    print("3 - Remove palavras de posição par")
    print("4 - Remove palavras de posição ímpar")
    print()

def main():
    showParameters()
    args = arguments()
    text = args.text #Texto para formar a senha
    parameters = args.parameters #Parâmetros para formar a senha
    print("Texto: ", text)
    print("Parâmetros: ", parameters)
    print("Senha: ", generatePassword(text, parameters))

#python gerador.py -t "Texto usado para formar a senha" -p "1 2"
main()