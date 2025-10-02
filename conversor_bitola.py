import tkinter as tk

tabela_bitola = {
    28: {"espessura": 0.43, "peso_m2": 3.44},
    26: {"espessura": 0.50, "peso_m2": 4.00},
    24: {"espessura": 0.61, "peso_m2": 4.88},
    23: {"espessura": 0.68, "peso_m2": 5.49},
    22: {"espessura": 0.76, "peso_m2": 6.10},
    21: {"espessura": 0.84, "peso_m2": 6.71},
    20: {"espessura": 0.91, "peso_m2": 7.32},
    19: {"espessura": 1.06, "peso_m2": 8.54},
    18: {"espessura": 1.21, "peso_m2": 9.76},
    17: {"espessura": 1.37, "peso_m2": 10.98},
    16: {"espessura": 1.52, "peso_m2": 12.21},
    15: {"espessura": 1.71, "peso_m2": 13.73},
    14: {"espessura": 1.90, "peso_m2": 15.26},
    13: {"espessura": 2.28, "peso_m2": 18.81},
    12: {"espessura": 2.66, "peso_m2": 21.36},
}

def calcular_chapa():
    try:
        bitola = int(entry_bitola.get())
        largura = float(entry_largura.get())
        comprimento = float(entry_comprimento.get())
        valor_kg = float(entry_valor_kg.get())
    except:
        label_resultado.config(text="Preencha todos os campos corretamente.")
        return

    if bitola not in tabela_bitola:
        label_resultado.config(text="Bitola inválida.")
        return

    espessura = tabela_bitola[bitola]["espessura"]
    peso_m2 = tabela_bitola[bitola]["peso_m2"]

    area = largura * comprimento
    peso = area * peso_m2
    total = peso * valor_kg

    resultado = (
        f"Bitola {bitola} → Espessura {espessura:.2f} mm\n"
        f"Área: {area:.3f} m²\n"
        f"Peso: {peso:.2f} kg\n"
        f"Valor total: R$ {total:.2f}"
    )

    label_resultado.config(text=resultado)

janela = tk.Tk()
janela.title("Calculadora de Chapa de Aço")

janela.bind("<Return>", lambda event: calcular_chapa())

tk.Label(janela, text="Bitola:").grid(row=0, column=0)
entry_bitola = tk.Entry(janela)
entry_bitola.grid(row=0, column=1)

tk.Label(janela, text="Largura (m):").grid(row=1, column=0)
entry_largura = tk.Entry(janela)
entry_largura.grid(row=1, column=1)

tk.Label(janela, text="Comprimento (m):").grid(row=2, column=0)
entry_comprimento = tk.Entry(janela)
entry_comprimento.grid(row=2, column=1)

tk.Label(janela, text="Valor por kg (R$):").grid(row=3, column=0)
entry_valor_kg = tk.Entry(janela)
entry_valor_kg.grid(row=3, column=1)

btn_calcular = tk.Button(janela, text="Calcular", command=calcular_chapa)
btn_calcular.grid(row=4, column=0, columnspan=2)

label_resultado = tk.Label(janela, text="Preencha os campos e clique em Calcular")
label_resultado.grid(row=5, column=0, columnspan=2)

janela.mainloop()
