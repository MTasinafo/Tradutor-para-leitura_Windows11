Clipboard Translator (EN → PT)

Aplicação desktop leve em Python que monitora automaticamente o conteúdo da área de transferência (clipboard), traduz textos do inglês para o português e exibe o resultado em uma janela flutuante temporária.

Overview

O Clipboard Translator foi desenvolvido para agilizar a leitura de conteúdos em inglês, oferecendo tradução automática e imediata sempre que um novo texto é copiado.

A aplicação opera continuamente em segundo plano, detectando alterações no clipboard e exibindo a tradução em uma interface minimalista.

Features

Monitoramento automático do clipboard

Tradução automática de inglês (EN) para português (PT)

Interface gráfica leve com Tkinter

Janela sempre visível (topmost)

Fechamento automático após 5 segundos

Estrutura simples e de fácil modificação

Tech Stack

Python 3.x

Tkinter (GUI nativa do Python)

Pyperclip (clipboard access)

Googletrans (tradução automática)

__________________Installation:
1. Install Python

Ubuntu/Debian:

sudo apt install python3 python3-pip

________________________2. Install Dependencies:
pip install pyperclip googletrans==4.0.0-rc1


Recomendado utilizar googletrans==4.0.0-rc1 para maior estabilidade.

Usage

____________Execute o script:

python3 Translator.py


A aplicação iniciará o monitoramento automático do clipboard.

Sempre que um novo texto em inglês for copiado, a tradução será exibida no canto inferior esquerdo da tela.

How It Works

O programa verifica o conteúdo do clipboard a cada 0.5 segundos.

___________________________________Caso detecte um novo texto não vazio:

Envia o conteúdo para o serviço de tradução.

Exibe o resultado em uma janela flutuante.

A janela é automaticamente fechada após 5 segundos.

O processo continua em loop até interrupção manual.

_____________Configuration
___________________Alterar idioma de destino

_________________Modifique:

translator.translate(texto_clipboard, src='en', dest='pt')


Exemplo para espanhol:

dest='es'

Alterar tempo de exibição da janela
root.after(5000, root.destroy)


O valor está em milissegundos (5000 = 5 segundos).

_________Limitations:

Requer conexão com a internet.

Utiliza googletrans, que não é uma API oficial do Google.

Pode sofrer instabilidades se houver muitas requisições consecutivas.

A detecção de idioma é fixa (configurada como inglês).

________Possible Improvements:

Detecção automática de idioma

Configuração via arquivo .env ou .json

Ícone na system tray

Transformação em serviço de background

Empacotamento como executável (PyInstaller)

Interface de configurações

______________License:

Este projeto pode ser utilizado para fins educacionais e pessoais.
