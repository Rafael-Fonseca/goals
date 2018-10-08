'''*********************************************************************************************************************
**                 Neste arquivo estão todas as funções usadas na interface do projeto Goals                          **
*********************************************************************************************************************'''


def ask_string(msg, error_msg="A sentença inserida é inválida!"):

    sentence = input(msg).lower().strip()

    if not sentence.isalpha():
        print(error_msg)
        return ask_string(msg)

    return sentence


def ask_numeric_string(msg, error_msg="A sentença inserida é inválida!"):

    sentence = input(msg)
    if not sentence.isnumeric():
        print(error_msg)
        return ask_numeric_string(msg)

    return sentence


def ask_positive_int(msg, error_msg="Valor inválido!"):

    try:
        number = int(input(msg))
        if number < 0:
            print(error_msg)
            return ask_positive_int(msg)

        return number

    except ValueError:
        print(error_msg)
        return ask_positive_int(msg)


def show_menu(listOptions, exitMsg = "0. Sair"):
    print("------------------------------------------------\n"
          "|                      MENU                    |\n"
          "------------------------------------------------")

    for msg in range(0, len(listOptions)):
        print("---", str(msg+1)+".", listOptions[msg])

    print("---", exitMsg)

    selection = ask_positive_int("---\n--- Digite a opção desejada: ")

    if selection > len(listOptions):
        input("Opção inválida!, pressione qualquer tecla para continuar: ")
        return show_menu(listOptions)

    return str(selection)


# Esta função printa as opções do usuário ANTES DE EFETUAR LOGIN
def show_login_options():
    list_options = ["Cadastrar", "Logar", "Esqueci minha senha"]
    option = show_menu(list_options)
    return option


# Esta função printa as opções do usuário APÓS EFETUAR LOGIN
def show_menu_options():
    list_options = ["Incluir Meta", "Editar Metas", "Acompanhamento Diário",
                    "Rotina", "Revisão de Resultados", "Perfil"]
    option = show_menu(list_options, "0. Retornar ao menu inicial")
    return option
