from bs4 import BeautifulSoup


class ParserAnuncio(object):
    def __init__(self, content, valor):
        self.content = content
        self.soap = BeautifulSoup(content, 'html.parser')
        self.valor_filtro = valor

    def get_images(self):
        try:
            # busca = self.soap.find_all(
            #     'div', attrs={'class': 'my-gallery'})
            busca = self.soap.find_all(
                'figure', attrs={'class': 'col-sm-2 col-xs-3'})
            images = []
            for image in busca:
                # figure = image.find(
                #     'figure', attrs={'class': 'col-sm-2 col-xs-3'})
                image_ = image.find('img')['src']
                images.append(image_)

            videos = []
            if self.soap.find("video"):
                for video in self.soap.find_all("video"):
                    video_link = video.find('source')["src"]
                    videos.append(video_link)

            valor = self.soap.find(
                'p', attrs={'class': 'disponivel text-center'}).text[7:].strip()

            if self.valor_filtro != None:
                if valor == 'A COMBINAR.' or float(valor.replace(',', '.')) > float(self.valor_filtro):
                    return {
                        "message": f"Muito carro pra vc!! {valor}",
                        "link_anuncio": ""
                    }

            nome = self.soap.find(
                'h2', attrs={'class': 'nome_artistico'}).text

            idade = self.soap.find(
                'p', attrs={'class': 'idade'}).text.strip()

            horarios = self.soap.find(
                'h4', attrs={'class': 'disponivel'}).text.strip()

            descricao = self.soap.find(
                'p', attrs={'class': 'descricao'}).text.strip()

            parser = {
                "imagens": images,
                "nome": nome,
                "idade": idade,
                "horarios": horarios,
                "valor": valor,
                "descricao": descricao,
                "videos": videos,
                "link_anuncio": ""
            }
            return parser
        except Exception as error:
            print(error)
            return error
        except KeyboardInterrupt:
            print("Interompido pelo usuario")
