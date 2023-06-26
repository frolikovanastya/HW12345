import requests
import os

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        file_name = os.path.basename(file_path)
        upload_url = f"https://cloud-api.yandex.net/v1/disk/resources/upload?path=/{file_name}&overwrite=true"
        with open(file_path, "rb") as file:
            response = requests.put(upload_url, headers={"Authorization": f"OAuth {self.token}"}, files={"file": file})
        response.raise_for_status()

 if __name__ == '__main__':
    path_to_file = input("Введите путь к файлу: ")
    token = input("Введите токен: ")
    uploader = YaUploader(token)
    uploader.upload(path_to_file)
    print("Файл успешно загружен на Яндекс.Диск!")