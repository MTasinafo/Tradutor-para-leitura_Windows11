import time
import tkinter as tk
import pyperclip
from googletrans import Translator

# Configura o tradutor
translator = Translator()

# Texto anterior no clipboard
ultimo_texto = ""

# Função para mostrar a tradução em uma janelinha
def mostrar_traducao(texto):
    root = tk.Tk()
    root.overrideredirect(True)  # Remove bordas
    root.attributes('-topmost', True)  # Sempre na frente
    root.geometry(f"400x100+10+{root.winfo_screenheight() - 150}")  # Canto inferior esquerdo

    label = tk.Label(root, text=texto, font=("Arial", 12), wraplength=380, justify="left", bg="black", fg="white")
    label.pack(fill="both", expand=True)

    # Fecha automaticamente após 5 segundos
    root.after(5000, root.destroy)
    root.mainloop()

while True:
    try:
        texto_clipboard = pyperclip.paste()

        # Só processa se for novo texto e for em inglês (detecção simples)
        if texto_clipboard != ultimo_texto and texto_clipboard.strip():
            ultimo_texto = texto_clipboard

            try:
                traducao = translator.translate(texto_clipboard, src='en', dest='pt').text
                mostrar_traducao(traducao)
            except Exception as e:
                print(f"Erro na tradução: {e}")

        time.sleep(0.5)

    except KeyboardInterrupt:
        break
