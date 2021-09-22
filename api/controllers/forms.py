import json
from flask.json import jsonify
from flask import Blueprint, request
from flask.templating import render_template
from api.services.forms import get_supervisors, is_valid_form

# Instantiate controller as Flask controller.
blueprint = Blueprint(name="forms_controller", import_name=__name__)

@blueprint.route("/api/supervisors")
def supervisors():
	"""
	Returns a sorted list of supervisors retrieved from a separate API.
	"""
	return jsonify({"supervisors":get_supervisors()})


@blueprint.route("/api/submit", methods=["POST"])
def submit():
	"""
	Accepts form submission and returns response depending on whether POST contents pass validation.
	"""
	form_data = request.form
	if is_valid_form(form_data):
		print(form_data)
	else:
		return render_template("error.html", code=400, message="One or more of the following fields was missing: First Name, Last Name, Supervisor.")


