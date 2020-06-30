
import requests

class Lord:
    # Não precisa de chave de autenticação
    def request_api_book(self):
        response = requests.get(f'https://the-one-api.herokuapp.com/v1/book')
        
        if(response.status_code == 200):
            return response.json()
        else:
            return response.status_code

    # Precisa de autenticação
    def request_api(self):
        endpoint = 'character'
        api_token = 'xxxxxxx'
        api_url_base = f'https://the-one-api.herokuapp.com/v1/{endpoint}'
        
        headers = {'Content-Type': 'application/json',
           'Authorization': 'Bearer {0}'.format(api_token)}

        response = requests.get(api_url_base, headers=headers)
            
        if(response.status_code == 200):
            return response.json()
        else:
            return response.status_code

    def show_list_book(self):
        data = self.request_api_book()       
        print(data)

    def show_list_caracter(self):
        data = self.request_api()        
        print(data.keys()) #mostra as chaves do dicionário

        for x in data['docs']:
            print(x['name'], x['race'])

lord = Lord()
#lord.show_list_book()
lord.show_list_caracter()

