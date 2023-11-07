import requests

def verificar_site(url):
    
        response = requests.get(url)
        if response.status_code == 200:
            print(f'O site {url} está funcionando corretamente.')
        else:
            print(f'Não foi possível acessar o site {url}')


url = 'http://pudim.com.br/'
verificar_site(url)