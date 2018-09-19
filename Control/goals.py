'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
**                                  Uniceub -- LTP 1 -- Professor: Caio                                              **                              
**             Alunos: Rafael Abreu Fonseca RA: 21700439 e Rafael de Oliveira Brilhante                              **
**                                                                                                                   **
**      Proposta do projeto: Usar os nossos conhecimentos em software para ajudar pessoas a atingirem seus objetivos **
**  e por consequência diminuir a quantidade de seres humanos frustados com a vida.                                  **
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
from Control.goals_controller import *
from View.goals_view import *
from Model.goals_model import *


firstOption = {"0": close, "1": sign_up, "2": login, "3": forgot_password}  # TODO: Todas estas funções, são de controle
menuOptions = {"0": close, "1": add_goal, "2": edit_goals, "3": daily_monitoring,
               "4": routine, "5": review_results, "6": profile}

loginOption = show_login_options()  # Guarda em loginOption o retorno da função de visão chamada
# ToDo: Try Catch na linha abaixo pois a mesma pode gerar uma KeyError
firstOption[loginOption]()  # Chama a função de controle selecionada pelo usuário através do dicionário de funções

chosenOption = "The option has not been chosen yet"  # Garante a entrada no while
while chosenOption != "0":  # Define a condição de saída
    chosenOption = show_menu_options()  # Guarda em chosenOption o retorno da função de visão chamada
    # ToDo: Try Catch na linha abaixo pois a mesma pode gerar uma KeyError
    menuOptions[chosenOption]()  # Chama a função de controle selecionada pelo usuário através do dicionário de funções
