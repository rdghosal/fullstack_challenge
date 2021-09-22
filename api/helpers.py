from flask import render_template


def render_error(message, code=400):
	"""
	Insert an error message to an html page and render to client.
	"""
	return render_template("error.html", code=code, message=message), code
	
