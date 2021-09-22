(async function renderDropdownItems() {

	try {
		const dropdown = document.getElementById("supervisor-dropdown");
		const data = await fetchSupervisors();
		const supervisors = await data["supervisors"];
		await supervisors.forEach(supervisor => {
			const option = document.createElement("option");
			option.textContent = supervisor;
			option.value = supervisor;
			dropdown.appendChild(option);
		});
	}
	catch(error) {
		window.alert(`An error has occured.\n${error}`);
	}

})();

async function fetchSupervisors() {
	try {
		const response = await fetch("/api/supervisors");
		return response.json();
	}
	catch (error) {
		return error;
	}
}