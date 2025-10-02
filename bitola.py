import tkinter as tk

densidade = 7850

tabela_bitola = {
    28: 0.40,
    26: 0.50,
    24: 0.61,
    23: 0.68,
    22: 0.76,
    21: 0.84,
    20: 0.91,
    19: 1.06,
    18: 1.21,
    17: 1.37,
    16: 1.52,
    15: 1.71,
    14: 1.90,
    13: 2.28,
    12: 2.66,
    11: 3.04,
    10: 3.42,
    9: 3.80,
    8: 4.18,
    7: 4.55,
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

    espessura_mm = tabela_bitola[bitola]
    espessura_m = espessura_mm / 1000
    area = largura * comprimento
    volume = area * espessura_m
    peso = volume * densidade
    total = peso * valor_kg

    resultado = (
        f"Bitola {bitola} → Espessura {espessura_mm:.2f} mm\n"
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