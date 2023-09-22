from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
# from parserJogo import ParserJogo
# from sendEmail import SendEmail
from selenium.common.exceptions import NoSuchElementException

from parser_anuncio import ParserAnuncio

filtro_valor = None

filtro = input("Quer aplicar um filtro de valor (S = sim, N = não): ")

if filtro == "S" or filtro == "s":
    filtro_valor = int(input("Quanto vc tem no bolso? "))

options = webdriver.ChromeOptions()
options.add_argument("--headless=new")

navegador = webdriver.Chrome(options=options)
# navegador = webdriver.Chrome()  # PARA VER O NEVEGADOR

navegador.get('https://www.hotms.com.br/acompanhantes-campo-grande-ms')
sleep(10)

anuncios_parser = []
anuncios = navegador.find_elements(By.CLASS_NAME, "bloco1")
for anuncio in anuncios:
    try:
        link = anuncio.find_element(By.TAG_NAME, 'a')
        link_anuncio = anuncio.find_element(
            By.TAG_NAME, 'a').get_attribute('href')
        link.click()
        parser = ParserAnuncio(navegador.page_source, filtro_valor)
        parser = parser.get_images()
        parser["link_anuncio"] = link_anuncio
        print(parser)
        anuncios_parser.append(parser)
        print("------------------------------------------------------")
        sleep(5)
        navegador.back()
    except Exception as error:
        linkAnuncio = anuncio.find_element(
            By.TAG_NAME, 'a').get_attribute('href')
        print(linkAnuncio)
        print(error)
    except KeyboardInterrupt:
        print("Finalizado pelo usuario")

print(anuncios_parser)
