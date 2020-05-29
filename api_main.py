import flask
from apispec import APISpec
from flask import Blueprint, Flask, jsonify
from flasgger import Swagger
from services.service_tester import ServiceTester

app = flask.Flask(__name__)

zephyr = Blueprint('zephyr', __name__)
service_prefix = '/zephyr/'


app.register_blueprint(zephyr, url_prefix=service_prefix)


spec = APISpec(
    title='Test service',
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
            "endpoint": f"{service_prefix}api_spec",
            "route": f"{service_prefix}api_spec.json",
            "rule_filter": lambda rule: True,  # all in
            "model_filter": lambda tag: True,  # all in
        }
    ],
    "static_url_path": f"{service_prefix}flasgger_static",
    # "static_folder": "static",  # must be set by user
    "swagger_ui": True,
    "specs_route": service_prefix
}

swagger = Swagger(app, template=spec.to_dict(), config=swagger_config)


@app.route('/', methods=['GET'])
def home():
    """GET endpoint to fetch test case details for a given Test Case ID.
    ---
    tags:
      - zephyr test service to see how this works
    parameters:
      - name: test_param
        in: path
        type: string
        string: 'Enter Query Param here'
        required: true
        default: 'Testing'
    responses:
      200:
        description: Tester service details
    """
    service = ServiceTester('https://chroniclingamerica.loc.gov')
    resp = service.rest_client.get(path='/search/pages/results/', params={'format': 'json','proxtext': 'fire'})
    return jsonify(resp.json())


if __name__ == "__main__":
    # zephyr.add_url_rule("/", 'test', home)
    zephyr.add_url_rule('zephyr/<zephyr_key>', 'zephyr', home)
    app.run(debug=True)
