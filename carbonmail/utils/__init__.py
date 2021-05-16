#arquivo usado para transformar a pasta em pacote
#sempre executado ao importar o pacote

import PySimpleGUI as sg


def inner_element_space(width=100):
    #senão for informado a largura o padrão é 100
    return[sg.Text(" " * width, font=("Arial",1))]
        #uma caixa de texto que multiplica espaço vazio ' ' 
        # pelo tamanho do width, sendo assim 100 ou quanto vier de atributos, espaços vazios
        # na font o menor possivel 
        
