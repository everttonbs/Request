
import requests, json

class Meme:

    def request_api(self):
        response = requests.get(f'https://api.imgflip.com/get_memes')
        
        if(response.status_code == 200):
            return response.json()

        else:
            return response.status_code

    def show_list_meme(self):
        data = self.request_api()           

        for meme_name in data['data']['memes']:
            print(meme_name['name'])


meme = Meme()
meme.show_list_meme()

