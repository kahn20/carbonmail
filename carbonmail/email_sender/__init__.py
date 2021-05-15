#arquivo usado para transformar a pasta em pacote
#sempre executado ao importar este pacote

import PySimpleGUI as sg
from PySimpleGUI import WIN_CLOSED
from carbonmail.email_sender import view
from carbonmail.list_editor.manager import initialize as init_list_editor

#classe de objetos email_sender
class Email_Sender():
    def __init__(self):
        self.window = None
        #iniciando uma nova janela vazia

     #função para criar uma janela   
    def instantiate(self):
        if self.window == None:
             self.window = view.get_window()

    def enable_window(self):
        self.instantiate()
        # window = view.get_window()

        while True:
           event, values = self.window.read()

           if event == WIN_CLOSED:
               self.close.window()
               break 
        #enquanto for verdade execute para identificar qualquer clique evento e tambem valores dos campos para atualizar banco 
         # se o evento ou clique for igual ao fechar, feche a janela, pare o programa
         
           if event =='-Send-':
                 title = values['-Title-']
                 content = values['-Content-']

                 sg.Popup(
                      f"O Titulo é: {title}\n O Conteudo é: {content}",
                       title='E-mail',)

                     #abrir uma nova tela
           if event == '-ListEditor-':
                self.hide_window()
                init_list_editor(self)


    # função para fechar a janela
    def close_window(self):
        if self.window is not None:
            self.window.Close()


     #ocultar uma janela
    def hide_window(self):
        if self.window is not None:
            self.window.Hide()
    
    #desocultar uma janela
    def unhide_window(self):
        if self.window is not None:
            self.window.UnHide()