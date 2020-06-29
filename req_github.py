
import requests, json

class RepositoryGitHub:

    def __init__(self, user):
        self.user = user

    def request_api(self):
        response = requests.get(f'https://api.github.com/users/{self.user}/repos')

        if (response.status_code == 200):
            return response.json()
        else:
            return response.status_code


    def show_reposity(self):
        data = self.request_api()
        if(type(data) is not int):
            for i in range(len(data)):
                print(f'Reposity: {data[i]["name"]}\nOwner: {data[i]["owner"]["login"]}\n')
                
        else:
            print(data)

    def show_keys(self):
        lista_dict = self.request_api()

        if(type(lista_dict) is not int):
            print(lista_dict[0].keys()) 
        else:
            print('Not Found')   
            

user = RepositoryGitHub('torvalds')
user.show_reposity()
#user.show_keys()

