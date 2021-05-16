#É onde fica o codigo para a interface grafica
# tudo que existir de visual vai ficar aqui
#principalmente aqui o pysimplegui

from carbonmail.email_sender.view import get_window
import PySimpleGUI as sg
from carbonmail.utils import inner_element_space

lista = ['Administradores', 'Alunos']

def get_layout():

    frame_list = [
        inner_element_space(600),
        [
            sg.Text('Selecione a lista: '),
            sg.Combo(lista, default_value =lista[1], key ='-List-')
        ],
        [ 
            sg.Text('Criar uma lista: '),
            sg.In(key='-ListName-'),
            sg.Button('Criar', key='-Create-',size=(10,1)),
            #size é x e y = largura e altura do botao
        ],
        [ 
            sg.Button(
                'Deletar a Lista', 
                key='-Delete-', 
                size=(15, 1),
                pad=((5, 0) , (7, 7)),
                ),
            sg.Button(
                'Mostrar contatos ',
                key='-Contats -', 
                size=(15,1),
                pad=((5, 0) ,(7, 7)),
                ),
        ],
        inner_element_space(600),
    ]

    frame_import = [
        inner_element_space(600),
        [ 
            sg.Text(
            "Selecione o arquivo (CSV):", 
            tooltip="Cabeçalhos: name e email"
        ),
        sg.In(key='-CSV-'),
        sg.FileBrowse(
            "Selecionar",
            file_types=(("CSV", '*.csv'),),
            tooltip="Cabeçalhos: name e email",
            #tooltip uma ajuda para mostrar como inserir
        ),
        ],
        [ 
            sg.Button(
                "Importar Contatos",
                key='-Import-',
                size=(15,1),
                pad=((5,0), (7,7)),
            ),
        ],
        inner_element_space(600),
    ]
    
    frame_add = [
        inner_element_space(600),
        [ 
            sg.Text("Insira o nome:"),
            sg.In(key='-Name-')
        ],
        [ 
            sg.Text("Insira o email:"),
            sg.In(key='-Email-')
        ],
        [ 
            sg.Button(
                "Adicionar Contato",
                key='-Add-',
                size=(15,1),
                pad=((5, 0),(7, 7)),
            )
        ],
        inner_element_space(600),
    ]

    layout = [
        [sg.Frame('Configurações da Lista', frame_list, 
        element_justification='c')],
        [ 
            sg.Frame(
                "Importar Contatos",
                frame_import,
                element_justification='c'
            )
        ],
        [ 
            sg.Frame(
                "Adicinoar Contato",
                frame_add,
                element_justification='c',
            )
        ],
        [ 
            sg.Button(
                "Voltar",
                key='-Back-',
                size=(15,1),
                pad=((5, 0), (7, 7))
            )
        ],
        inner_element_space(650)
    ]

    return layout



def get_window():
    sg.theme("DarkBlue14")
    return sg.Window(
        'Editor de Lista', 
        get_layout(),
        element_justification='c',
        )