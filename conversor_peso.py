import tkinter as tk

def calcular(event=None):
    try:
        peso_metro = float(entry_peso_metro.get())
    except:
        peso_metro = 0

    try:
        metros = float(entry_metros.get())
    except:
        metros = 0

    try:
        peso_desejado = float(entry_peso.get())
    except:
        peso_desejado = 0

    resultado = ""

    if metros > 0 and peso_metro > 0:
        total_kg = metros * peso_metro
        resultado = f"Peso total: {total_kg:.2f} kg"
    elif peso_desejado > 0 and peso_metro > 0:
        metros_necessarios = peso_desejado / peso_metro
        resultado = f"{metros_necessarios:.2f} metros"
    else:
        resultado = "Preencha valores válidos para calcular."

    label_resultado.config(text=resultado)

janela = tk.Tk()
janela.title("Conversor Kg/Metro")

janela.bind("<Return>", calcular)

tk.Label(janela, text="Peso por metro (kg/m):").grid(row=0, column=0)
entry_peso_metro = tk.Entry(janela)
entry_peso_metro.grid(row=0, column=1)

tk.Label(janela, text="Quantidade de metros:").grid(row=1, column=0)
entry_metros = tk.Entry(janela)
entry_metros.grid(row=1, column=1)

tk.Label(janela, text="Peso desejado (kg):").grid(row=2, column=0)
entry_peso = tk.Entry(janela)
entry_peso.grid(row=2, column=1)

btn_calcular = tk.Button(janela, text="Calcular", command=calcular)
btn_calcular.grid(row=3, column=0, columnspan=2)

label_resultado = tk.Label(janela, text="")
label_resultado.grid(row=4, column=0, columnspan=2)

janela.mainloop()
