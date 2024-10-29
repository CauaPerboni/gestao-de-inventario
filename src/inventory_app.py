import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QListWidget, QLabel, QMessageBox
from inventory_manager import add_product as db_add_product, get_product, update_product, delete_product, create_table

class InventoryApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.create_database()

    def create_database(self):
        create_table()

    def initUI(self):
        self.setWindowTitle('Gerenciamento de Estoque')
        self.setGeometry(100, 100, 400, 400)

        layout = QVBoxLayout()

        # Campos para entrada de dados
        self.name_input = QLineEdit(self)
        self.name_input.setPlaceholderText('Nome do Produto')
        
        self.description_input = QLineEdit(self)
        self.description_input.setPlaceholderText('Descrição do Produto')

        self.quantity_input = QLineEdit(self)
        self.quantity_input.setPlaceholderText('Quantidade')
        
        self.price_input = QLineEdit(self)
        self.price_input.setPlaceholderText('Preço')

        layout.addWidget(self.name_input)
        layout.addWidget(self.description_input)
        layout.addWidget(self.quantity_input)
        layout.addWidget(self.price_input)

        # Botão para adicionar produto
        self.add_button = QPushButton('Adicionar Produto', self)
        self.add_button.clicked.connect(self.add_product)
        layout.addWidget(self.add_button)

        # Lista para mostrar produtos
        self.product_list = QListWidget(self)
        self.product_list.itemClicked.connect(self.load_selected_product)
        layout.addWidget(self.product_list)

        # Botões para atualizar e remover produtos
        self.update_button = QPushButton('Atualizar Produto', self)
        self.update_button.clicked.connect(self.update_product)
        layout.addWidget(self.update_button)

        self.delete_button = QPushButton('Remover Produto', self)
        self.delete_button.clicked.connect(self.delete_product)
        layout.addWidget(self.delete_button)

        self.setLayout(layout)
        self.load_products() 

    def add_product(self):
        name = self.name_input.text()
        description = self.description_input.text()
        quantity = self.quantity_input.text()
        price = self.price_input.text()

        try:
            db_add_product(name, description, int(quantity), float(price))
            self.load_products()
            self.clear_inputs()
        except ValueError:
            self.show_error("Por favor, insira valores válidos para quantidade e preço.")

    def load_products(self):
        self.product_list.clear()
        products = get_product()
        for product in products:
            self.product_list.addItem(f"{product[0]}: {product[1]} - {product[2]} (Quantidade: {product[3]}, Preço: R$ {product[4]})")

    def load_selected_product(self, item):
        product_details = item.text().split(': ')[0]
        product_id = int(product_details)

        product = get_product(product_id)
        if product:
            self.name_input.setText(product[1])
            self.description_input.setText(product[2])
            self.quantity_input.setText(str(product[3]))
            self.price_input.setText(str(product[4]))

    def update_product(self):
        selected_item = self.product_list.currentItem()
        if selected_item:
            product_id = int(selected_item.text().split(': ')[0])
            name = self.name_input.text()
            description = self.description_input.text()
            quantity = self.quantity_input.text()
            price = self.price_input.text()

            try:
                update_product(product_id, name, description, int(quantity), float(price))
                self.load_products()
                self.clear_inputs()
            except ValueError:
                self.show_error("Por favor, insira valores válidos para quantidade e preço.")
        else:
            self.show_error("Selecione um produto para atualizar.")

    def delete_product(self):
        selected_item = self.product_list.currentItem()
        if selected_item:
            product_id = int(selected_item.text().split(': ')[0])
            delete_product(product_id)
            self.load_products()
            self.clear_inputs()
        else:
            self.show_error("Selecione um produto para remover.")

    def clear_inputs(self):
        self.name_input.clear()
        self.description_input.clear()
        self.quantity_input.clear()
        self.price_input.clear()

    def show_error(self, message):
        QMessageBox.critical(self, "Erro", message)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = InventoryApp()
    ex.show()
    sys.exit(app.exec_())
