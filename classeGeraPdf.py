from fpdf import FPDF
from mod_cliente.clienteBD import Clientes
from mod_produto.produtoBD import Produtos
from mod_pedido.pedidoBD import Pedido
from datetime import datetime
# utilizado para tratar a imagem
import base64, re, os
from PIL import Image
from io import BytesIO

class PDF(FPDF):
    def header(self):
        self.image("media_files/batman.jpg", 10, 8, 20)
        self.set_font('arial', 'B', 15)
        self.cell(0, 5, 'Abc Bolinhas', 0, 1, 'C', 0)
        self.ln(5)
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, 'Página ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')

    def pdfClientes(self):
        pdf = PDF('L', 'mm', 'A4') # L paisagem, P retrato
        pdf.set_author("Abc Bolinhas")
        pdf.set_title('Clientes')
        pdf.alias_nb_pages() # mostra o numero da pagina no rodapé
        pdf.add_page()
        # mostra o cabeçalho
        pdf.set_font('arial', 'b', 12)
        pdf.cell(280, 5, 'Clientes', 0, 1, 'C', 0)
        pdf.set_font('arial', '', 6)
        pdf.cell(280, 4, "Emitido em: " + str(datetime.now()), 0, 1, 'R')
        pdf.ln(5)
        # monta tabela para mostrar os dados
        pdf.set_font('arial', 'B', 8)
        pdf.cell(10, 5, 'ID', 0, 0, 'L')
        pdf.cell(55, 5, 'Nome', 0, 0, 'L')
        pdf.cell(30, 5, 'Telefone', 0, 0, 'L')
        pdf.cell(50, 5, 'E-Mail', 0, 0, 'L')
        pdf.cell(25, 5, 'Login', 0, 0, 'L')
        pdf.cell(20, 5, 'Grupo', 0, 0, 'L')
        pdf.cell(90, 5, 'Endereço', 0, 1, 'L')
        # busca e mostra todos os clientes
        pdf.set_font('arial', '', 8)
        cliente = Clientes()
        res = cliente.selectALL()
        if res:
            for row in res:
                pdf.cell(10, 5, str(row[0]), 0, 0, 'L')
                pdf.cell(55, 5, str(row[1]), 0, 0, 'L')
                pdf.cell(30, 5, str(row[9]), 0, 0, 'L')
                pdf.cell(50, 5, str(row[10]), 0, 0, 'L')
                pdf.cell(25, 5, str(row[11]), 0, 0, 'L')
                pdf.cell(20, 5, str(row[13]), 0, 0, 'L')
                pdf.multi_cell(90, 5, "Rua: " + str(row[2]) + ", No: " + str(row[3]) + "\n" + str(row[6]) + "\n" + str(
                row[7]) + " - " + str(row[8]) + "\n" + str(row[5]) + "\nOBS: " + str(row[4]), '', 'L', 0) # LTRB

        # baixa o relatório criado
        pdf.output('pdfClientes.pdf')

    def pdfProdutos(self):
        pdf = PDF('P', 'mm', 'A4') # L paisagem, P retrato
        pdf.set_author("Abc Bolinhas")
        pdf.set_title('Produtos')
        pdf.alias_nb_pages() # mostra o numero da pagina no rodapé
        pdf.add_page()
        # mostra o cabeçalho
        pdf.set_font('arial', 'b', 12)
        pdf.cell(190, 5, 'Produtos', 0, 1, 'C', 0)
        pdf.set_font('arial', '', 6)
        pdf.cell(190, 4, "Emitido em: " + str(datetime.now()), 0, 1, 'R')
        pdf.ln(5)
        # monta tabela para mostrar os dados
        pdf.set_font('arial', 'B', 8)
        pdf.cell(10, 5, 'ID', 0, 0, 'L')
        pdf.cell(75, 5, 'Produto', 0, 0, 'L')
        pdf.cell(15, 5, 'Valor', 0, 0, 'L')
        pdf.cell(90, 5, 'Imagem', 0, 1, 'L')
        # busca e mostra todos os produtos
        pdf.set_font('arial', '', 8)
        produto = Produtos()
        res = produto.selectALL()
        if res:
            for row in res:
                pdf.cell(10, 5, str(row[0]), 0, 0, 'L')
                pdf.cell(75, 5, str(row[1]), 0, 0, 'L')
                pdf.cell(15, 5, str(row[2]), 0, 0, 'L')
                # converte de string base64 para imagem
                img = Image.open( BytesIO( base64.b64decode( re.sub('^data:image/.+;base64,', '', row[3]) ) ) )
                _auxNome = str(row[0]) + '.png'
                img.save(_auxNome, "PNG")
                # posiciona e mostra no pdf a imagem
                pdf.image(_auxNome, pdf.get_x(), pdf.get_y(), 40)
                pdf.ln(40)
                # remove a imagem gerada
                os.remove(_auxNome)
        # baixa o relatório criado
        pdf.output('pdfProdutos.pdf')

    def pdfPedidos(self):
        pdf = PDF('P', 'mm', 'A4') # L paisagem, P retrato
        pdf.set_author("Abc Bolinhas")
        pdf.set_title('Pedidos')
        pdf.alias_nb_pages() # mostra o numero da pagina no rodapé
        pdf.add_page()
        # mostra o cabeçalho
        pdf.set_font('arial', 'b', 12)
        pdf.cell(190, 5, 'Pedidos', 0, 1, 'C', 0)
        pdf.set_font('arial', '', 6)
        pdf.cell(190, 4, "Emitido em: " + str(datetime.now()), 0, 1, 'R')
        pdf.ln(5)
        pdf.set_font('arial', '', 30)
        pdf.ln(10)
        pdf.cell(190, 5, 'dá teus pulos e desenvolva!!!', 0, 1, 'C')
        # baixa o relatório criado
        pdf.output('pdfPedidos.pdf')
    
