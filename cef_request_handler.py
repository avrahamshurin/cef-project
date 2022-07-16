import json
import requests

class CefRequestHandler():
    CEF_URL = 'https://aicalliance.org/ajax/ceta_funds.php'
    HEADER_PATH = 'data\\request_headers.json'
    DATA_PATH = 'data\\request_data.json'

    def __init__(self):
        self.headers = self.__get_json(self.HEADER_PATH)
        self.data = self.__get_json(self.DATA_PATH)

    def __get_json(self, file_path):
        with open(file_path) as request_data_json:
            return json.load(request_data_json)
    
    def make_request(self):
        return requests.post(self.CEF_URL, headers=self.headers, json=self.data)


