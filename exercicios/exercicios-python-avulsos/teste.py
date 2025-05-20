# Programa de Lista de Compras com Interface
import math
import tkinter as tk
from tkinter import simpledialog, messagebox

class ListaDeComprasApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Lista de Compras")

        self.lista_de_compras = []

        self.label = tk.Label(master, text="Bem-vindo à Lista de Compras!")
        self.label.pack()

        self.btn_adicionar = tk.Button(master, text="Adicionar Item", command=self.adicionar_item)
        self.btn_adicionar.pack()

        self.btn_exibir = tk.Button(master, text="Exibir Lista", command=self.exibir_lista)
        self.btn_exibir.pack()

        self.btn_calcular = tk.Button(master, text="Calcular Subtotal e Valor Total", command=self.calcular_subtotal_e_total)
        self.btn_calcular.pack()

        self.btn_retirar = tk.Button(master, text="Retirar Item", command=self.retirar_item)
        self.btn_retirar.pack()

        self.btn_sair = tk.Button(master, text="Sair", command=self.master.destroy)
        self.btn_sair.pack()

    def formatar_nome(self, nome):
        return nome.capitalize()

    def adicionar_item(self):
        item = simpledialog.askstring("Adicionar Item", "Digite o nome do item:")
        item_formatado = self.formatar_nome(item)

        preco = float(simpledialog.askstring("Adicionar Item", "Digite o preço do item:").replace(',', '.'))
        quantidade = float(simpledialog.askstring("Adicionar Item", "Digite a quantidade desejada:"))
        quantidade = math.floor(quantidade)

        subtotal = preco * quantidade
        self.lista_de_compras.append({"item": item_formatado, "preco": preco, "quantidade": quantidade, "subtotal": subtotal})
        messagebox.showinfo("Adicionar Item", f"{quantidade} {item_formatado}(s) foram adicionados à lista por R${subtotal:.2f}.")

    def calcular_subtotal_e_total(self):
        subtotal_total = sum(item['subtotal'] for item in self.lista_de_compras)
        valor_total = subtotal_total
        messagebox.showinfo("Subtotal e Valor Total", f"Subtotal da Lista de Compras: R${subtotal_total:.2f}\nValor total da Lista de Compras: R${valor_total:.2f}")

    def exibir_lista(self):
        lista_texto = "\nLista de Compras:\n"
        for i, item in enumerate(self.lista_de_compras, start=1):
            lista_texto += f"{i}. {item['quantidade']} {item['item']}(s) por R${item['subtotal']:.2f} cada\n"
        messagebox.showinfo("Exibir Lista", lista_texto)

    def retirar_item(self):
        lista_texto = "\nLista de Compras:\n"
        for i, item in enumerate(self.lista_de_compras, start=1):
            lista_texto += f"{i}. {item['quantidade']} {item['item']}(s) por R${item['subtotal']:.2f} cada\n"

        escolha = simpledialog.askinteger("Retirar Item", f"{lista_texto}\nDigite o número do item que deseja retirar ou 0 para cancelar:")
        if escolha is not None:
            index = escolha - 1
            if 0 <= index < len(self.lista_de_compras):
                quantidade_retirar = float(simpledialog.askstring("Retirar Item", "Digite a quantidade que deseja retirar:").replace(',', '.'))
                quantidade_atual = self.lista_de_compras[index]['quantidade']

                if quantidade_retirar >= quantidade_atual:
                    del self.lista_de_compras[index]
                    messagebox.showinfo("Retirar Item", "Item removido completamente da lista.")
                else:
                    self.lista_de_compras[index]['quantidade'] -= quantidade_retirar
                    self.lista_de_compras[index]['subtotal'] -= self.lista_de_compras[index]['preco'] * quantidade_retirar
                    messagebox.showinfo("Retirar Item", f"{quantidade_retirar} {self.lista_de_compras[index]['item']}(s) retirado(s) da lista.")
            else:
                messagebox.showwarning("Retirar Item", "Número do item inválido. Nenhum item foi removido.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ListaDeComprasApp(root)
    root.mainloop()