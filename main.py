import requests
from pprint import pprint
#Задача 1
url = 'https://www.superheroapi.com/api.php/2619421814940190/search/'
superheroes_list = ['Hulk', 'Captain America', 'Thanos']
intelligence_dict = {}

def get_intelligence():
    for superhero in superheroes_list:
        superheroes_dict = requests.get(url + superhero).json()['results']
        intelligence_dict[superhero] = superheroes_dict[0]['powerstats']['intelligence']
    new_list = []
    for item in intelligence_dict:
        new_list.append(intelligence_dict[item])
    l = sorted(new_list)
    for item in intelligence_dict:
        if intelligence_dict[item] == l[-1]:
            res = item
        else:
            None
    pprint(f'Самый умный супергерой {res}')

if __name__ == '__main__':
    get_intelligence()

#Задача 2

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headres(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }
    def get_link(self, path_to_file):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headres()
        params = {'path': path_to_file, 'overwrite': 'true'}
        response = requests.get(upload_url, headers=headers, params=params)
        pprint(response.json())
        return response.json()

    def upload(self, file_path, filename):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        href = self.get_link(path_to_file=path_to_file).get('href', '')
        response = requests.put(href, data=open(filename, 'rd'))




if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = ""
    TOKEN = ""
    uploader = YaUploader(token=TOKEN)
    result = uploader.upload(path_to_file, filename='')