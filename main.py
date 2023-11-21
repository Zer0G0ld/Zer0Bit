# Author : Zer0 | CodeOpen
# Project: Link Shortener
# Language: Python
import pyshorteners
import requests

def cut_link(url, custom_alias=None):
    # Construir a URL para API git.io
    gitio_url = "https://git.io"
    data = {'url': url, 'code': custom_alias} if custom_alias else {'url': url}
    
    # fazer uma requisição POST para encontrar a URL
    response = requests.post(gitio_url, data=data)
    
    # Verificar se a requisição foi bem sucedida
    if response.status_code == 201:
        cut_link = response.headers['Location']
        return cut_link
    else:
        print(f"Erro ao encurtar a URL. Código de status: {response.status_code}")

url_original = str(input("Link : "))
custom_alias = str(input("Deseja fornecer um nome personalizado para o link? "))

link_cut = cut_link(url_original, custom_alias)

if link_cut:
    print(f"URL Original : {url_original}")
    print(f"URL Encurtada : {link_cut}")