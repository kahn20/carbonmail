#É onde fica o codigo para a interface grafica
# tudo que existir de visual vai ficar aqui
#principalmente aqui o pysimplegui


import PySimpleGUI as sg

#window ==> Janela
#layout ==> o que vai mostra na janela
#       ==> é uma Lista de Listas
#      cada sublista é uma "linha" da Janela
#      cada Elemento é um componente visual

lista = ['Administrador', 'Alunos']

def get_layout():
    layout = [
        [
            sg.Text("Selecione seu codigo"),
            sg.In(),
            sg.FileBrowse(
                "Selecione o seu código", file_types=(("Código Python", " *.py")
                            ,)
            ),
        ],
        [
            sg.Text("Selecione a lista de destinatários"),
            sg.Combo(lista, default_value =lista[1]),
        ],
        [
            sg.Text("Insira o Título: "),
            sg.In(key="-Title-"),
        ],
        [
            sg.Text("Insira o conteudo do E-mail: "),
            sg.MLine(key="-Content-"),
        ],
        [
            sg.Button("Enviar", key="-Send-"),
            sg.Button("Gerenciar Lista", key="-ListEditor-"),
        ],
    ]

    return layout

def get_window():
    return sg.Window("Teste de Janela Vitao", get_layout())