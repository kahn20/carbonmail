#este arquivo é onde estará todas as funções
#ele é quem coordena este pacote, gerenciador


def initialize():
    from carbonmail.email_sender import Email_Sender

    ems = Email_Sender()
    ems.enable_window()
