#este arquivo é onde estará todas as funções
#ele é quem coordena este pacote, gerenciador

def initialize(email_sender):
    from carbonmail.list_editor import List_Editor

    ems = List_Editor(email_sender)
    ems.enable_window()