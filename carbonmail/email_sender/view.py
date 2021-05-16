#É onde fica o codigo para a interface grafica
# tudo que existir de visual vai ficar aqui
#principalmente aqui o pysimplegui


import PySimpleGUI as sg
from carbonmail.utils import inner_element_space
#window ==> Janela
#layout ==> o que vai mostra na janela
#       ==> é uma Lista de Listas
#      cada sublista é uma "linha" da Janela
#      cada Elemento é um componente visual

lista = ['Administrador', 'Alunos']

def get_layout():

    frame_campaign = [ 
        inner_element_space(500),
        [ 
            sg.Text('Selecione o código'),
            sg.In(key='-Code-',
            size=(30,1)),
            sg.FileBrowse("Selecionar",
            file_types=(("Códigos Python", " *.py"),),
            ),
        ],
        [ 
            sg.Text("Selecione a lista de destinatários"),
            sg.Combo(lista, lista[1], key='-Lists-'),

        ],
        inner_element_space(500),
    ]
    frame_email = [ 
        inner_element_space(500),
        [sg.Text('Insira o titulo', font=('Helvetica 15'))],
        [sg.In(key='title-',size=(62, 1))],
        # tamanho de 62 para compensar os 2 que tera de scrool no content
        [sg.Text("Insira o Conteudo", font=('Helvetica 15'))],
        # apos o tamanho do mline tem 2pixels da barra de rolagem 
        [sg.MLine(key='-Content-', size=(60, 10))],
        inner_element_space(500),
    ]




    layout = [
        [ 
                sg.Frame('Configurações da Campanha',
                    frame_campaign,
                    element_justification='c',
                )
        ],
        [ 
            sg.Frame("Configurações de e-mail",
            frame_email,
            element_justification='c',
            ),
        ],
        [ 
            sg.Button("Enviar E-mail",
            key='-Send-',
            size=(15,1),
            pad=((10, 0),(10, 0)),
            ),
        
            sg.Button("Gerenciar Listas",
            key='-ListEditor-',
            size=(15,1),
            pad=((10, 0),(10, 0)),
            ),
        ],
        inner_element_space(500),
    
           
    ]

    return layout

def get_window():

    sg.theme("DarkBlue14")
    return sg.Window(
        'Enviador de E-mail', 
        get_layout(),
        element_justification='c',
    )



   