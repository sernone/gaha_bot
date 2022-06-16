import json

class d2Config:
    def __init__(self):
        self.apiKey = self._configData('key')
        self.client_id = self._configData('client_id')

    def _configData(self, type):
        with open("./config.json", "r") as configFile:
            data = json.load(configFile)
            destinyConfig = data['d2']

        return destinyConfig[type]