
import requests, json

class Meme:

    def request_api(self):
        response = requests.get(f'https://api.imgflip.com/get_memes')
        
        if(response.status_code == 200):
            return response.json()

        else:
            return response.status_code

    def show_meme(self):
        data = self.request_api()    
        print(data['data']['memes'])


meme = Meme()
meme.show_meme()



