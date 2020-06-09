from flask import jsonify

from services.service_tester import ServiceTester

# Make instance of service 1 time for whole file
service_tester = ServiceTester()

def get_test_plan(test_plan_id):
    """GET endpoint to fetch test plan details. This includes test cases (tests and its details)
    that are associated with a given TestPlan ID.
    ---
    tags:
      - zephyr
    parameters:
      - name: test_plan_id
        in: path
        type: string
        string: 'id-54108'
        required: true
        default: 'id-54108'
    responses:
      200:
        description: A list of test case keys added to the test plan
    """
    return jsonify(service_tester.get_tests_from_test_plan(test_plan_id))


# Move to its own view later
def get_test_plan_from_service_call():
    """GET endpoint to test the dummy service call to an active backend
    ---
    tags:
      - zephyr
    responses:
      200:
        description: resp from https://chroniclingamerica.loc.gov/search/pages/results/?format=json&proxtext=fire
    """
    resp = service_tester.test(path='/search/pages/results/', params={'format': 'json','proxtext': 'fire'})

    return jsonify(resp)
