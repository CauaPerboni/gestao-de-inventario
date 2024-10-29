import tkinter as tk
from tkinter import messagebox
from inventory_manager import add_product
from report_generator import generate_report

def add_product_to_inventory():
    """Função para adicionar um produto ao estoque."""
    name = entry_name.get()
    description = entry_description.get()
    quantity = entry_quantity.get()
    price = entry_price.get()
    min_stock = entry_min_stock.get()

    if not name or not description or not quantity or not price or not min_stock:
        messagebox.showwarning("Aviso", "Por favor, preencha todos os campos.")
        return

    try:
        quantity = int(quantity)
        price = float(price)
        min_stock = int(min_stock)
        add_product(name, description, quantity, price, min_stock)
        messagebox.showinfo("Sucesso", "Produto adicionado com sucesso!")
        clear_entries()
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores válidos para quantidade, preço e mínimo de estoque.")

def clear_entries():
    """Limpa os campos de entrada."""
    entry_name.delete(0, tk.END)
    entry_description.delete(0, tk.END)
    entry_quantity.delete(0, tk.END)
    entry_price.delete(0, tk.END)
    entry_min_stock.delete(0, tk.END)

def generate_report_and_notify():
    """Gera um relatório e notifica o usuário."""
    report_file = 'estoque_relatorio'
    generate_report('database/sales_report.db', report_file)
    messagebox.showinfo("Relatório Gerado", f"Relatório gerado com sucesso: {report_file}.csv e {report_file}.pdf")

def run_app():
    """Executa a interface do usuário."""
    global entry_name, entry_description, entry_quantity, entry_price, entry_min_stock

    window = tk.Tk()
    window.title("Gerenciador de Estoque")

    tk.Label(window, text="Nome do Produto").grid(row=0, column=0)
    entry_name = tk.Entry(window)
    entry_name.grid(row=0, column=1)

    tk.Label(window, text="Descrição").grid(row=1, column=0)
    entry_description = tk.Entry(window)
    entry_description.grid(row=1, column=1)

    tk.Label(window, text="Quantidade").grid(row=2, column=0)
    entry_quantity = tk.Entry(window)
    entry_quantity.grid(row=2, column=1)

    tk.Label(window, text="Preço").grid(row=3, column=0)
    entry_price = tk.Entry(window)
    entry_price.grid(row=3, column=1)

    tk.Label(window, text="Mínimo em Estoque").grid(row=4, column=0)
    entry_min_stock = tk.Entry(window)
    entry_min_stock.grid(row=4, column=1)

    tk.Button(window, text="Adicionar Produto", command=add_product_to_inventory).grid(row=5, column=0, columnspan=2)
    tk.Button(window, text="Gerar Relatório", command=generate_report_and_notify).grid(row=6, column=0, columnspan=2)

    window.mainloop()
