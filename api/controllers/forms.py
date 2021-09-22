from enum import Enum
from flask.json import jsonify
import requests
from flask import Blueprint, make_response

# Instantiate controller as Flask controller.
blueprint = Blueprint(name="forms_controller", import_name=__name__)

class SupervisorField(Enum):
	JURISDICTION = 1
	LAST_NAME = 2
	FIRST_NAME = 3


@blueprint.route("/api/supervisors")
def get_supervisors():
	# GET supervisor list from client-specified URL.
	response = requests.get("https://o3m5qixdng.execute-api.us-east-1.amazonaws.com/api/managers")

	supervisors_str = []

	# Convert json to list.
	supervisors = list(response.json())

	# Filter out supervisors with numerical jurisdictions.
	supervisors = filter_numerical(supervisors)

	# Sort supervisors according to jurisdiction, lastName, firstName.
	supervisors = sort_supervisors(supervisors \
		, [get_field_as_str(SupervisorField.JURISDICTION) \
			, get_field_as_str(SupervisorField.LAST_NAME) \
			, get_field_as_str(SupervisorField.FIRST_NAME)])

	return jsonify(supervisors)


def get_field_as_str(field):
	"""
	Maps enum value for SupervisorField to its corresponding str version.
	"""
	field_str = ""
	if field == SupervisorField.JURISDICTION:
		field_str = "jurisdiction"
	elif field == SupervisorField.LAST_NAME:
		field_str = "lastName"	
	elif field == SupervisorField.FIRST_NAME:
		field_str = "firstName"

	return field_str


def filter_numerical(supervisors):
	"""
	Returns a list containing those supervisors whose `jurisdiction` field is non-numerical.
	"""
	filtered = []
	for s in supervisors:
		if not s[get_field_as_str(SupervisorField.JURISDICTION)].isnumeric():
			filtered.append(s)
	return filtered


def sort_supervisors(supervisors, field_list):
	"""
	Recursive function to organize according to an ordered list of field names
	"""
	sorted_sups = []

	# Base case -> Access field and sort supervisors list.
	if len(field_list) == 1:
		print(supervisors)
		supervisors = sorted(supervisors, key=lambda s: s[field_list[0]])
		print(supervisors)
		return supervisors

	# If not base case,  create a hash table and sort each row.
	else:
		memo = {}
		for s in supervisors:
			k = s[field_list[0]]
			if memo.get(k) == None:
				memo[k] = []
			temp = memo[k]
			temp.append(s)
			memo[k] = temp

		# Access keys in alphabetical order.
		keys = memo.keys()
		keys = sorted(keys)

		# Sort each row in the hash table, appending each item therein to the sorted list.
		for key in keys:
			memo[key] = sort_supervisors(memo[key], field_list[1:])
			for sup in memo[key]:
				sorted_sups.append(sup)

		return sorted_sups

