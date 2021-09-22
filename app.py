from api import create_app


if __name__ == "__main__":
	# Create app and run
	app = create_app()
	app.run(debug=True)

