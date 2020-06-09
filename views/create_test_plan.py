from flasgger import SwaggerView
from flask import request, jsonify

from schemas.zephyr_test_plan_obj import TestsReportSchema
from services.service_tester import ServiceTester


class CreateTestPlanView(SwaggerView):
    parameters = TestsReportSchema
    responses = {
        200: {
            'description': "A create test case response object",
        }
    }

    @staticmethod
    def post():
        """
        POST endpoint to create Test plan(s) for given name(s) and do corresponding associations
        ---
        tags:
          - zephyr, POST
        post:
          summary: Creates new Test Plan(s) in zephyr.
          consumes:
            - application/json
          responses:
            200:
              description: Test Case created. Test Case ID returned
        """
        data, errors = TestsReportSchema().load(request.get_json())
        # Test data for post
        # test_schema = {"test_plan_key": '100', "test_type": 'AUTOMATED', "test_case_params": "None"}
        # test_report_schema = {'test_details': test_schema, 'should_add_unexecuted_cases': False, "zephyr_env": "prod"}
        #'{"test_details": {"test_plan_key": "100", "test_type": "AUTOMATED", "test_case_params": "None"}, "should_add_unexecuted_cases": false, "zephyr_env": "prod"}'

        if errors:
            return jsonify({'error': errors}), 400
        # user service to make call to zephyr
        # response_body, response_code = zephyr(data=data).post_test_cases()
        new_data = data['should_add_unexecuted_cases'] = "CUSTOM UPDATED ON RESPONSE"
        return jsonify(data), 200
