#arquivo usado para transformar a pasta em pacote
#sempre executado ao importar o pacote


import PySimpleGUI as sg
from PySimpleGUI import WIN_CLOSED
from carbonmail.list_editor import view

class List_Editor():
    def __init__(self, email_sender):
        self.window = None
        self.ems = email_sender
        # acima iniciando uma nova janela vazia

     #função para criar uma janela   
    def instantiate(self):
          if self.window == None:
              self.window = view.get_window()

    def enable_window(self):
        self.instantiate()
        # window = view.get_window()

        while True:
          event, values = self.window.read()

          if event in (WIN_CLOSED, "-Back-"):
             self.window.close()
             self.window = None
             self.ems.unhide_window()
             break 
        #enquanto for verdade execute para identificar qualquer clique evento e tambem valores dos campos para atualizar banco 
         # se o evento ou clique for igual ao fechar, feche a janela, pare o programa
         
        if event =='-Send-':
            title = values['-Title-']
            content = values['-Content-']

            sg.Popup(f"O Titulo é: {title}\n O Conteudo é: {content}", title='E-mail')

         
    # função para fechar a janela
    def close_window(self):
        if self.window is not None:
            self.window.close()


     #ocultar uma janela
    def hide_window(self):
        if self.window is not None:
            self.window.hide()
    
    #desocultar uma janela
    def unhide_window(self):
        if self.window is not None:
            self.window.UnHide()