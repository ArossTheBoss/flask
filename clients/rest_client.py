import requests
import json


class RequestBase():
    def __init__(self, base_url):
        self.base_url = base_url
        self.headers = {'Content-Type': 'application/json'}

    def post(self, payload=None, path=None, params=None, custom_headers=None, custom_url=None):
        full_url = self.base_url + '/'
        headers = self.headers
        data = payload

        if path:
            full_url = self.base_url + '/' + path

        if custom_headers:
            headers = custom_headers

        if headers['Content-Type'] == 'application/json':
            data = json.dumps(payload)

        if custom_url:
            full_url = custom_url

        response = requests.post(url=full_url,
                                 data=data,
                                 params=params,
                                 headers=headers,
                                 timeout=5,
                                 verify=False)
        return response

    def get(self, path=None, data=None, params=None, custom_headers=None, custom_url=None):
        full_url = self.base_url + '/'
        headers = self.headers

        if path:
            full_url = self.base_url + '/' + path

        if custom_headers:
            headers = custom_headers

        if custom_url:
            full_url = custom_url

        response = requests.get(url=full_url,
                                data=data,
                                params=params,
                                headers=headers,
                                timeout=5,
                                verify=False)
        return response

    def delete(self, path=None, data=None, params=None, custom_headers=None, custom_url=None):
        full_url = self.base_url + '/'
        headers = self.headers

        if path:
            full_url = self.base_url + '/' + path

        if custom_headers:
            headers = custom_headers

        if custom_url:
            full_url = custom_url

        response = requests.get(url=full_url,
                                data=data,
                                params=params,
                                headers=headers,
                                timeout=5,
                                verify=False)
        return response
