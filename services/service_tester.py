from clients import rest_client


class ServiceTester:
    def __init__(self, base_url='https://chroniclingamerica.loc.gov'):
        self.base_url = base_url
        self.rest_client = rest_client.RequestBase(base_url)

    def test(self, path, params):
        return self.rest_client.get(path=path, params=params)

    def get_tests_from_test_plan(self, test_plan_id):
        return {"TestPlanId": test_plan_id}
