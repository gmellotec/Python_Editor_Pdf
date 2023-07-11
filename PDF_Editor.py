import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askdirectory
import PyPDF2 as pyf
from pathlib import Path

def selecionar_arquivo_sep():
    caminho_arquivo_sep = askopenfilename(title='Selecione um Arquivo PDF')
    var_caminhoarquivo.set(caminho_arquivo_sep)

    if caminho_arquivo_sep:
        label_caminhoarquivo['text'] = f'{caminho_arquivo_sep}'

def selecionar_arquivo1():
    caminho_arquivo1 = askopenfilename(title='Selecione um Arquivo PDF')
    var_caminhoarquivo1.set(caminho_arquivo1)

    if caminho_arquivo1:
        label_arquivo1['text'] = f'{caminho_arquivo1}'

def selecionar_arquivo2():
    caminho_arquivo2 = askopenfilename(title='Selecione um Arquivo PDF')
    var_caminhoarquivo2.set(caminho_arquivo2)

    if caminho_arquivo2:
        label_arquivo2['text'] = f'{caminho_arquivo2}'

def selecionar_pasta_destino_sep():
    caminho_pasta_destino = askdirectory(title='Selecione uma Pasta')
    var_caminhopastadestino_sep.set(caminho_pasta_destino)

    if caminho_pasta_destino:
        label_caminhopastadestino_sep['text'] = f'{caminho_pasta_destino}'

def selecionar_pasta_destino_mesc():
    caminho_pasta_destino = askdirectory(title='Selecione uma Pasta')
    var_caminhopastadestino_mesc.set(caminho_pasta_destino)

    if caminho_pasta_destino:
        label_caminhopastadestino_mesc['text'] = f'{caminho_pasta_destino}'

def separar_paginas():
    nome_arquivo = var_caminhoarquivo.get()
    arquivo_pdf = pyf.PdfReader(nome_arquivo)

    nome_pastadestino = var_caminhopastadestino_sep.get()

    i = 1
    for pagina in arquivo_pdf.pages:
        arquivo_novo = pyf.PdfWriter()
        arquivo_novo.add_page(pagina)

        with Path(f'{nome_pastadestino}/Pagina {i}.pdf').open(mode='wb') as arquivo_final:
            arquivo_novo.write(arquivo_final)
            i += 1

    if arquivo_final:
        label_mensagem_separar['text'] = 'Arquivo Editado com Sucesso!'
        label_mensagem_separar['bg'] = '#008000'


def mesclar_arquivos():
    pdf_mesclado = pyf.PdfMerger()

    nome_arquivo1 = var_caminhoarquivo1.get()
    arquivo1 = nome_arquivo1

    nome_arquivo2 = var_caminhoarquivo2.get()
    arquivo2 = nome_arquivo2

    nome_pastadestino = var_caminhopastadestino_mesc.get()

    pdf_mesclado.append(arquivo1)
    pdf_mesclado.append(arquivo2)

    with Path(f'{nome_pastadestino}/Arquivo_Mesclado.pdf').open(mode='wb') as arquivo_final:
        pdf_mesclado.write(arquivo_final)

    if arquivo_final:
        label_mensagem_mesclar['text'] = 'Arquivo Editado com Sucesso!'
        label_mensagem_mesclar['bg'] = '#008000'

def resetar():
    label_caminhoarquivo['text'] = "Nenhum Arquivo Selecionado"

    label_arquivo1['text'] = "Arquivo 1 NÃO Selecionado"

    label_arquivo2['text'] = "Arquivo 2 NÃO Selecionado"

    label_caminhopastadestino_sep['text'] = "Nenhuma Pasta Selecionada"

    label_caminhopastadestino_mesc['text'] = "Nenhuma Pasta Selecionada"

    label_mensagem_separar['text'] = ""
    label_mensagem_separar['bg'] =  '#4682B4'

    label_mensagem_mesclar['text'] = ""
    label_mensagem_mesclar['bg'] = '#4682B4'


janela = tk.Tk()
janela.title("PDF Editor")
janela.configure(bg='#4682B4')

### SEPARAR PDF'S
label_separarpdf = tk.Label(text="SEPARAR PAGINAS PDF", bg='black', fg='white')
label_separarpdf.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky='news')

var_caminhoarquivo = tk.StringVar()
button_selecionararquivo = tk.Button(text="Selecionar Arquivo", command=selecionar_arquivo_sep)
button_selecionararquivo.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
label_caminhoarquivo = tk.Label(text="Nenhum Arquivo Selecionado", bg='#4682B4')
label_caminhoarquivo.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky='news')

var_caminhopastadestino_sep = tk.StringVar()
button_selecionarpastadestino_sep = tk.Button(text="Selecionar Onde Salvar", command=selecionar_pasta_destino_sep)
button_selecionarpastadestino_sep.grid(row=3, column=0, columnspan=3, padx=10, pady=10)
label_caminhopastadestino_sep = tk.Label(text="Nenhuma Pasta Selecionada", bg='#4682B4')
label_caminhopastadestino_sep.grid(row=4, column=0, columnspan=3, padx=10, pady=10, sticky='news')

button_separarpaginas = tk.Button(text="Separar Páginas", command=separar_paginas)
button_separarpaginas.grid(row=5, column=0, columnspan=3, padx=10, pady=10)
label_mensagem_separar = tk.Label(text="", bg='#4682B4')
label_mensagem_separar.grid(row=6, column=0, columnspan=3, padx=10, pady=10)



### MESCLAR PDFS
label_mesclarpdf = tk.Label(text="MESCLAR ARQUIVOS PDF", bg='black', fg='white')
label_mesclarpdf.grid(row=7, column=0, columnspan=3, padx=10, pady=10, sticky='news')

var_caminhoarquivo1 = tk.StringVar()
button_arquivo1 = tk.Button(text='Selecionar Arquivo 1', command=selecionar_arquivo1)
button_arquivo1.grid(row=8, column=0, columnspan=2, padx=10, pady=10)
label_arquivo1 = tk.Label(text="Arquivo 1 NÃO Selecionado", bg='#4682B4')
label_arquivo1.grid(row=8, column=2, padx=10, pady=10, sticky='w')

var_caminhoarquivo2 = tk.StringVar()
button_arquivo2 = tk.Button(text='Selecionar Arquivo 2', command=selecionar_arquivo2)
button_arquivo2.grid(row=9, column=0, columnspan=2, padx=10, pady=10)
label_arquivo2 = tk.Label(text="Arquivo 2 NÃO Selecionado", bg='#4682B4')
label_arquivo2.grid(row=9, column=2, padx=10, pady=10, sticky='w')

var_caminhopastadestino_mesc = tk.StringVar()
button_selecionarpastadestino_mesc = tk.Button(text="Selecionar Onde Salvar", command=selecionar_pasta_destino_mesc)
button_selecionarpastadestino_mesc.grid(row=10, column=0, columnspan=3, padx=10, pady=10)
label_caminhopastadestino_mesc = tk.Label(text="Nenhuma Pasta Selecionada", bg='#4682B4')
label_caminhopastadestino_mesc.grid(row=11, column=0, columnspan=3, padx=10, pady=10, sticky='news')

button_mesclar = tk.Button(text="Mesclar", command=mesclar_arquivos)
button_mesclar.grid(row=12, column=0, columnspan=3, padx=10, pady=10)
label_mensagem_mesclar =  tk.Label(text="", bg='#4682B4')
label_mensagem_mesclar.grid(row=13, column=0, columnspan=3, padx=10, pady=10)

button_resetar = tk.Button(text="Resetar", command=resetar)
button_resetar.grid(row=14, column=2, padx=10, pady=10, sticky='e')


janela.mainloop()
