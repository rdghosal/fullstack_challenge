import os
from flask import Flask
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from .helpers import render_error
import api.controllers as controllers


def errorhandler(e):
	"""
	Handles HTTP and InternalServer errors.
	"""
	if not isinstance(e, HTTPException):
		e = InternalServerError()
	return render_error(e.name, e.code)


def create_app():
	"""
	Factory function for Flask app instance.
	"""
	# Instantiate app, passing path to html pages to constructor
	# and register controllers.
	app = Flask(__name__, template_folder="../client/html")
	app.register_blueprint(controllers.main.blueprint)
	app.register_blueprint(controllers.forms.blueprint)

	# Toggle dev/prod based on env variable.
	app.config["DEBUG"] = os.getenv("DEBUG") == "Y"

	# Ensure templates are auto-reloaded.
	app.config["TEMPLATES_AUTO_RELOAD"] = True
	app.config["CORS_HEADERS"] = "Content-Type"

	# Configure response headers.
	@app.after_request
	def after_request(response):
		response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
		response.headers["Expires"] = 0
		response.headers["Pragma"] = "no-cache"

		return response
	
	# Listen for errors.
	for code in default_exceptions:
		app.errorhandler(code)(errorhandler)

	return app

