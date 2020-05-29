from clients import rest_client


class ServiceTester:
    def __init__(self, base_url):
        self.base_url = 'https://chroniclingamerica.loc.gov'
        self.rest_client = rest_client.RequestBase(base_url)

    def test(self, path, params):
        self.rest_client.get(path=path, params=params)
