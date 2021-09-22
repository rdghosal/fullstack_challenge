from flask.json import jsonify
from flask import Blueprint
from api.services.forms import get_supervisors

# Instantiate controller as Flask controller.
blueprint = Blueprint(name="forms_controller", import_name=__name__)

@blueprint.route("/api/supervisors")
def supervisors():
	return jsonify(get_supervisors())

