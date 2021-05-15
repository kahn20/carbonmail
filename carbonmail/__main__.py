#arquivo principal (inicial) a ser executado.
#quando solicitamos o projeto (carbonmail) ele é o primeiro ao python executar
#nós usamos tambem para ser o ponto de entrada da aplicação

# importando arquivo view do email_sender
from carbonmail.email_sender.manager import initialize as init_sender

init_sender()
