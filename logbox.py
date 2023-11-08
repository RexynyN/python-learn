import tkinter as tk
from tkinter.scrolledtext import ScrolledText

def adicionar_mensagem():
    mensagem = entry.get()
    log_box.insert(tk.END, mensagem + "\n")
    entry.delete(0, tk.END)

# Cria a janela principal
janela = tk.Tk()
janela.title("Log Box")

# Cria a caixa de log
log_box = ScrolledText(janela, height=10, width=50)
log_box.pack()

# Cria a entrada de texto
entry = tk.Entry(janela, width=50)
entry.pack()

# Cria o botão para adicionar a mensagem
botao = tk.Button(janela, text="Adicionar", command=adicionar_mensagem)
botao.pack()

# Inicia o loop principal da janela
janela.mainloop()