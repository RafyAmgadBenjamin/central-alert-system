<script>
	import Navigation from './Navigation.svelte';
	import Alerts from './components/Alerts.svelte';
	import axios from 'axios';

	let alerts;
	let formatedAlerts = '';
	const environments = {
		ALL: 'ALL',
		PROD: 'PRODUCTION',
		DEV: 'DEVELOPMENT',
		INFRA: 'INFRASTRUCTURE',
	};
	const services = {
		ALL: 'ALL',
		THREEBOT: 'THREEBOT',
		JUMPSCALE: 'JUMPSCALE',
		ZEROOS: 'ZEROOS',
	};
	const severity = {
		ALL: 'ALL',
		CRITICAL: 'CRITICAL',
		MAJOR: 'MAJOR',
		MINOR: 'MINOR',
		WARNING: 'WARNING',
		INDETERMINATE: 'INDETERMINATE',
	};
	const messageTypes = {
		ALL: 'ALL',
		ERROR: 'ERROR',
		INFORMATION: 'INFORMATION',
		WARNING: 'WARNING',
	};
	const status = { ALL: 'ALL', OPEN: 'OPEN', CLOSED: 'CLOSED' };
	let currentFilters = {
		service: services.ALL,
		messageType: messageTypes.ALL,
		status: status.ALL,
	};
	//Get Data from the API
	function updateAlerts(environment) {
		console.log('chosed environemnt', environment);
		axios
			.get('http://localhost:8080/api/alerts/get-alerts/' + environment)
			.then(function(response) {
				// handle success
				console.log('response in success', response.data.alerts);
				//convertToUpperCase(alerts,"severity")
				formatedAlerts = convertDataToUpperCase(response.data.alerts);
				filterAlerts(formatedAlerts);
				console.log('alerts after filtering', alerts);
				// response.data.alerts;
			})
			.catch(function(error) {
				// handle error
				console.log('error ', error);
			})
			.finally(function() {
				// always executed
			});
	}

	function updateFilters(selectedService, selectedMessageType, selectedState) {
		currentFilters = {
			service: selectedService,
			messageType: selectedMessageType,
			status: selectedState,
		};
		filterAlerts(formatedAlerts);
	}

	function convertDataToUpperCase(alerts) {
		for (let i = 0; i < alerts.length; i++) {
			alerts[i].severity = alerts[i].severity.toUpperCase();
			alerts[i].service = alerts[i].service.toUpperCase();
			alerts[i].status = alerts[i].status.toUpperCase();
			alerts[i].messageType = alerts[i].messageType.toUpperCase();
		}
		return alerts;
	}

	function filterAlerts(filteredAlerts) {
		if (currentFilters.service != services.ALL)
			filteredAlerts = filteredAlerts.filter(singelAlert => {
				return singelAlert.service == currentFilters.service;
			});
		if (currentFilters.messageType != messageTypes.ALL)
			filteredAlerts = filteredAlerts.filter(singelAlert => {
				return singelAlert.messageType == currentFilters.messageType;
			});
		if (currentFilters.status != status.ALL)
			filteredAlerts = filteredAlerts.filter(singelAlert => {
				return singelAlert.status == currentFilters.status;
			});
		alerts = filteredAlerts;
	}
</script>

<style>

</style>

<div>
	<Navigation />
</div>

<!--[Container]-->
<div class="container">
	<!--[Title]-->
	<div class="m-3 text-center">
		<h1>Central Alert System</h1>
	</div>
	<!--[Filters]-->
	<div class="row">
		<div class="col-sm-12">
			<div class="d-flex justify-content-around">
				<!--[Services]-->
				<div class="dropdown">
					<button
						class="btn btn-light dropdown-toggle"
						type="button"
						id="dropdownMenuButton"
						data-toggle="dropdown"
						aria-haspopup="true"
						aria-expanded="false">
						Services
					</button>
					<div class="dropdown-menu" aria-labelledby="dropdownMenuButton">
						<a
							class="dropdown-item"
							href="#"
							on:click={() => updateFilters(services.ALL, currentFilters.messageType, currentFilters.status)}>
							All
						</a>
						<a
							class="dropdown-item"
							href="#"
							on:click={() => updateFilters(services.THREEBOT, currentFilters.messageType, currentFilters.status)}>
							ThreeBot
						</a>
						<a
							class="dropdown-item"
							href="#"
							on:click={() => updateFilters(services.JUMPSCALE, currentFilters.messageType, currentFilters.status)}>
							JumpScale
						</a>
						<a
							class="dropdown-item"
							href="#"
							on:click={() => updateFilters(services.ZEROOS, currentFilters.messageType, currentFilters.status)}>
							Zero OS
						</a>
					</div>
				</div>
				<!--[Message-Type]-->
				<div class="dropdown">
					<button
						class="btn btn-light dropdown-toggle"
						type="button"
						id="dropdownMenuButton"
						data-toggle="dropdown"
						aria-haspopup="true"
						aria-expanded="false">
						Message type
					</button>
					<div class="dropdown-menu" aria-labelledby="dropdownMenuButton">
						<a
							class="dropdown-item"
							href="#"
							on:click={() => updateFilters(currentFilters.service, messageTypes.ALL, currentFilters.status)}>
							All
						</a>
						<a
							class="dropdown-item"
							href="#"
							on:click={() => updateFilters(currentFilters.service, messageTypes.ERROR, currentFilters.status)}>
							Error
						</a>
						<a
							class="dropdown-item"
							href="#"
							on:click={() => updateFilters(currentFilters.service, messageTypes.INFORMATION, currentFilters.status)}>
							Information
						</a>
						<a
							class="dropdown-item"
							href="#"
							on:click={() => updateFilters(currentFilters.service, messageTypes.WARNING, currentFilters.status)}>
							Warning
						</a>

					</div>
				</div>
				<!--[Status]-->
				<div class="dropdown">
					<button
						class="btn btn-light dropdown-toggle"
						type="button"
						id="dropdownMenuButton"
						data-toggle="dropdown"
						aria-haspopup="true"
						aria-expanded="false">
						Status
					</button>
					<div class="dropdown-menu" aria-labelledby="dropdownMenuButton">
						<a
							class="dropdown-item"
							href="#"
							on:click={() => updateFilters(currentFilters.service, currentFilters.messageType, status.ALL)}>
							All
						</a>
						<a
							class="dropdown-item"
							href="#"
							on:click={() => updateFilters(currentFilters.service, currentFilters.messageType, status.OPEN)}>
							Open
						</a>
						<a
							class="dropdown-item"
							href="#"
							on:click={() => updateFilters(currentFilters.service, currentFilters.messageType, status.CLOSED)}>
							Closes
						</a>

					</div>
				</div>
			</div>
		</div>
	</div>
	<div class="row mt-4">
		<div class="col-sm-12">
			<!--[Tabs]-->
			<div>
				<ul class="nav nav-pills mb-3" id="pills-tab" role="tablist">
					<li class="nav-item">
						<a
							class="nav-link active"
							id="pills-all-tab"
							data-toggle="pill"
							href="#pills-all"
							role="tab"
							aria-controls="pills-all"
							aria-selected="true"
							on:click={() => updateAlerts(environments.ALL)}>
							All
						</a>
					</li>
					<li class="nav-item">
						<a
							class="nav-link"
							id="infra-profile-tab"
							data-toggle="pill"
							href="#pills-infra"
							role="tab"
							aria-controls="pills-infra"
							aria-selected="false"
							on:click={() => updateAlerts(environments.INFRA)}>
							Infrastructure
						</a>
					</li>
					<li class="nav-item">
						<a
							class="nav-link"
							id="pills-prod-tab"
							data-toggle="pill"
							href="#pills-prod"
							role="tab"
							aria-controls="pills-prod"
							aria-selected="false"
							on:click={() => updateAlerts(environments.PROD)}>
							Production
						</a>
					</li>
					<li class="nav-item">
						<a
							class="nav-link"
							id="pills-development-tab"
							data-toggle="pill"
							href="#pills-development"
							role="tab"
							aria-controls="pills-development"
							aria-selected="false"
							on:click={() => updateAlerts(environments.DEV)}>
							Development
						</a>
					</li>
				</ul>
				<div class="tab-content" id="pills-tabContent">
					<div
						class="tab-pane fade show active"
						id="pills-all"
						role="tabpanel"
						aria-labelledby="pills-all-tab" />
					<div
						class="tab-pane fade"
						id="pills-infra"
						role="tabpanel"
						aria-labelledby="pills-infra-tab">
						...infrastructure data
					</div>
					<div
						class="tab-pane fade"
						id="pills-prod"
						role="tabpanel"
						aria-labelledby="pills-prod-tab">
						...production data
					</div>
					<div
						class="tab-pane fade"
						id="pills-development"
						role="tabpanel"
						aria-labelledby="pills-development-tab">
						...Development data
					</div>
				</div>
			</div>

		</div>
	</div>
	<!--[Alerts]-->
	{#if alerts && alerts != ''}
		<!-- content here -->
		<div class="row">
			<div class="col-sm-12">
				<Alerts {alerts} />
			</div>
		</div>
	{/if}
</div>
