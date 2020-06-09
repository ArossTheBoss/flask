"""The module contains functionality to register endpoints and run 'qatoolkit' 'xray' service."""
from apispec import APISpec
from flask import Blueprint, Flask, jsonify
from flasgger import Swagger


from views.get_test_plan import get_test_plan, get_test_plan_from_service_call
from views.create_test_plan import CreateTestPlanView
from helpers.custom_exception_template import CustomExceptionTemplate

zephyr = Blueprint('zephyr', __name__)
service_prefix = '/zephyr/'


@zephyr.errorhandler(CustomExceptionTemplate)
def handle_error(error):
    """
    Error handler for missing required field exception
    :param error: Exception to be returned
    :return: Error dict to be sent to client
    """
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


zephyr.add_url_rule('test-plans/<test_plan_id>', 'get_test_plan', get_test_plan)
zephyr.add_url_rule('test-plans/', 'get_test_plan_from_service_call', get_test_plan_from_service_call)
zephyr.add_url_rule('test-plans/', view_func=CreateTestPlanView.as_view('create_test_plan'), methods=['POST'])

app = Flask(__name__)
app.register_blueprint(zephyr, url_prefix=service_prefix)


spec = APISpec(
    title='Web Services - zephyr ',
    version='0.0.0',
    plugins=(
        'apispec.ext.flask',
        'apispec.ext.marshmallow',
    ),
)

swagger_config = {
    "headers": [
    ],
    "specs": [
        {
            "endpoint": f"{service_prefix}apispec_1",
            "route": f"{service_prefix}apispec_1.json",
            "rule_filter": lambda rule: True,  # all in
            "model_filter": lambda tag: True,  # all in
        }
    ],
    "static_url_path": f"{service_prefix}flasgger_static",
    # "static_folder": "static",  # must be set by user
    "swagger_ui": True,
    "specs_route": service_prefix
}


@app.route('/', methods=['GET'])
def home():
    return "<center><h1>Home Page</h1><p>This is the entry point to all the apps</p></center>"


swagger = Swagger(app, template=spec.to_dict(), config=swagger_config)

if __name__ == "__main__":
    app.run(host='localhost', threaded=True, port=5000)
