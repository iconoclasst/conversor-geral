import tkinter as tk
from tkinter import messagebox

def calcular():
    try:
        valor_kg = float(entry_valor_kg.get())
    except:
        valor_kg = 0

    try:
        valor_un = float(entry_valor_un.get())
    except:
        valor_un = 0

    try:
        peso = float(entry_peso.get())
    except:
        peso = 0

    try:
        metro = float(entry_metro.get())
    except:
        metro = 0

    try:
        peso_metro = float(entry_peso_metro.get())
    except:
        peso_metro = 0

    try:
        unidade = int(entry_unidade.get())
    except:
        unidade = 0

    total = 0
    resultado = ""

    if peso > 0 and valor_kg > 0:
        total = peso * valor_kg
        resultado = f"Total por peso: R$ {total:.2f}"

    elif metro > 0 and peso_metro > 0 and valor_kg > 0:
        peso_total = metro * peso_metro
        total = peso_total * valor_kg
        resultado = f"Peso total: {peso_total:.2f} kg\nTotal por metro: R$ {total:.2f}"

    elif unidade > 0 and valor_un > 0:
        total = unidade * valor_un
        resultado = f"Total por unidade: R$ {total:.2f}"

    else:
        resultado = "Preencha pelo menos uma forma de cálculo válida."

    label_resultado.config(text=resultado)

janela = tk.Tk()
janela.title("Calculadora de Aço")

janela.bind("<Return>", lambda event: calcular())

tk.Label(janela, text="Peso (kg):").grid(row=0, column=0)
entry_peso = tk.Entry(janela)
entry_peso.grid(row=0, column=1)

tk.Label(janela, text="Metro (m):").grid(row=1, column=0)
entry_metro = tk.Entry(janela)
entry_metro.grid(row=1, column=1)

tk.Label(janela, text="Peso por metro (kg/m):").grid(row=2, column=0)
entry_peso_metro = tk.Entry(janela)
entry_peso_metro.grid(row=2, column=1)

tk.Label(janela, text="Unidade (un):").grid(row=3, column=0)
entry_unidade = tk.Entry(janela)
entry_unidade.grid(row=3, column=1)

tk.Label(janela, text="Valor por kg (R$):").grid(row=4, column=0)
entry_valor_kg = tk.Entry(janela)
entry_valor_kg.grid(row=4, column=1)

tk.Label(janela, text="Valor por unidade (R$):").grid(row=5, column=0)
entry_valor_un = tk.Entry(janela)
entry_valor_un.grid(row=5, column=1)

btn_calcular = tk.Button(janela, text="Calcular", command=calcular)
btn_calcular.grid(row=6, column=0, columnspan=2)

label_resultado = tk.Label(janela, text="Preencha os campos e clique em Calcular")
label_resultado.grid(row=7, column=0, columnspan=2)

janela.mainloop()
