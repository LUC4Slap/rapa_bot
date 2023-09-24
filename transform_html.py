class TransformHtml(object):
    def __init__(self, anuncios):
        self.anuncios = anuncios
        self.no_orcamento = []
    
    def pegar_anucios_orcamentos(self):
        for anuncio in self.anuncios:
            if anuncio.get("message") != None:
                continue
            else:
                self.no_orcamento.append(anuncio)
    
    def transform_html(self):
        for item in self.no_orcamento:
            # print(self.return_img_html(item['imagens']))
            print(f'''
                Nome: {item['nome'].strip()}
                Idade: {item['idade'].strip()}
                Horario: {item['horarios'].strip()}
                valor: {item['valor'].strip()}
                descrição: {item['descricao'].strip()}
            ''')
            # print(item['imagens'])
            # print(item['nome'])
            # print(item['idade'])
    def return_img_html(self, images_array):
        images = ''
        for image in images_array:
            images += f"<img src='{image}' /><br/>"
        return images
            
teste = TransformHtml([{'imagens': ['https://www.hotms.com.br/assinante/_lib/file/img/anuncios/13279/64df8bc36e192.jpeg', 'https://www.hotms.com.br/assinante/_lib/file/img/anuncios/13279/64df8bc27817f.jpeg', 'https://www.hotms.com.br/assinante/_lib/file/img/anuncios/13279/64df8bbdca6f5.jpeg', 'https://www.hotms.com.br/assinante/_lib/file/img/anuncios/13279/64df8bbca879d.jpeg', 'https://www.hotms.com.br/assinante/_lib/file/img/anuncios/13279/64df8bbbb4a3c.jpeg', 'https://www.hotms.com.br/assinante/_lib/file/img/anuncios/13279/64df8bbad5e3e.jpeg', 'https://www.hotms.com.br/assinante/_lib/file/img/anuncios/13279/64df8bba1c049.jpeg', 'https://www.hotms.com.br/assinante/_lib/file/img/anuncios/13279/64df8bb9363e7.jpeg'], 'nome': '\nPROMOÇÃO DE RAPIDINHA ', 'idade': '19 Anos / Campo Grande MS \nMulher \nRef: 13279', 'horarios': 'Disponível: 50,00 15 min \n80,00 meia hr \n150,00 uma hr', 'valor': '50,00', 'descricao': 'DESCRIÇÃO: VALORES \n50,00 rapidinha 15 min\n80,00 meia hr \n150,00 uma hr', 'videos': [], 'link_anuncio': 'https://www.hotms.com.br/acompanhantes-campo-grande-ms/promoo-de-rapidinha-13279'}])
teste.pegar_anucios_orcamentos()
teste.transform_html()
                
                