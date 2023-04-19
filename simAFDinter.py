import tkinter as tk

def afd(Q, alfab, fTrans, q0, F, cadeia):
    qA = q0
    for i in cadeia:
        qA = fTrans[(qA, i)]
    return qA in F

def verificar_cadeia():
    cadeia = entrada_cadeia.get()
    resultado = afd(Q, alfab, tabela, 'q0', F, cadeia)
    if resultado:
        label_resultado.config(text='Cadeia Aceita')
    else:
        label_resultado.config(text='Cadeia Nao Aceita')

# Definindo as variáveis
Q = ['q0','q1','q2']
F = ['q1']
alfab = ['0','1']
tabela = {('q0','0'): 'q0',('q0','1'): 'q1',('q1','0'): 'q2',('q1','1'): 'q1',('q2','0'): 'q1',('q2','1'): 'q1'}

# Criando a janela
janela = tk.Tk()
janela.title('AFD')

# Criando os widgets
label_cadeia = tk.Label(janela, text='Insira uma cadeia:')
entrada_cadeia = tk.Entry(janela)
botao_verificar = tk.Button(janela, text='Verificar', command=verificar_cadeia)
label_resultado = tk.Label(janela, text='')

# Posicionando os widgets na janela
label_cadeia.grid(row=0, column=0)
entrada_cadeia.grid(row=0, column=1)
botao_verificar.grid(row=1, column=0, columnspan=2)
label_resultado.grid(row=2, column=0, columnspan=2)

# Iniciando a janela
janela.mainloop()
