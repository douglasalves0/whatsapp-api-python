from utils.LoadYml import moorseUrl, moorseToken, moorseIntegration

import requests
import json

class MoorseLoginAPI:

    def getToken(email, password):
        body = {'login': email, 'senha': password}
        header = {"Accept": "application/json", "Content-Type": "application/json"}
        response = requests.request("POST", moorseUrl + "oauth/login", json=body, headers=header)
        return json.loads(response.text)
