from flask import Blueprint, render_template


# Instantiate Flask blueprint
blueprint = Blueprint(name="main_controller", import_name=__name__)

@blueprint.route("/")
def index():
	"""
	Returns index.html for root endpoint
	"""
	return render_template("index.html")

