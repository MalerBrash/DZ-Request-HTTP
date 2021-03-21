# from pprint import pprint
import requests

names = ('Hulk', 'Captain America', 'Thanos')
token = '<'your token'>'

def getRequests(token, name):
    link = "https://superheroapi.com/api/"
    url = link + token + '/search/' + name
    response = requests.get(url)
    if response.status_code != 200:
       print('Неудача')
    return response.json()

if __name__ == '__main__':
    val_intelligence = {}
    for name in names:
        f = getRequests(token, name)
        for k, v in f.items():
            if k == 'results':
                for k, v in v[0].items():
                    if k == 'name':
                        val_int = v
                    if k == 'powerstats':
                        for k, v in v.items():
                            if k == 'intelligence':
                                val_intelligence[val_int] = v

    print(f'Cамый умный супергерой: {max(val_intelligence)}.') ############  DZ 1


class YaUploader:
    def __init__(self, token: str):
        self.token = token


    def _get_upload_link(self, file_path):
        up_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = {'Content-Type': 'application/json', 'Authorization': 'OAuth {}'.format(self.token)}
        params = {'path': file_path, 'overwrite': 'true'}
        response = requests.get(up_url, headers=headers, params=params)
        return response.json()


    def upload_file_yd(self, file_path: str, file_name: str):
        """Метод загруджает файл file_path на яндекс диск"""
        href = self._get_upload_link(file_path=file_path).get('href', '')
        response = requests.put(href, data=open(file_name, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print('Файл записан на Яндекс Диск')


if __name__ == '__main__':
    uploader = YaUploader('<'your token'>')
    uploader.upload_file_yd('More.jpg', 'More.jpg')######################### DZ 2




