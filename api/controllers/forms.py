from flask.json import jsonify
from flask import Blueprint, request
from werkzeug.exceptions import HTTPException
from api.services.forms import get_supervisors, is_valid_form

# Instantiate controller as Flask controller.
blueprint = Blueprint(name="forms_controller", import_name=__name__)

@blueprint.route("/api/supervisors")
def supervisors():
	"""
	Returns a sorted list of supervisors retrieved from a separate API.
	"""
	return jsonify(get_supervisors())


@blueprint.route("/api/submit", methods=["POST"])
def submit():
	"""
	Accepts form submission and returns response depending on whether POST contents pass validation.
	"""
	form_data = request.form
	if is_valid_form(form_data):
		print(form_data)
	else:
		return HTTPException("Missing one or more of the following mandatory fields: First Name, Last Name, and/or Supervisor."), 400  	

