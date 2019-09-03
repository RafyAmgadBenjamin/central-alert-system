<script>
	export let alerts;
	console.log('alerts in Alerts component', alerts);
</script>

<div>
	<div class="row">
		<!--[Tasks-Data]-->
		<div class="col-xs-12">
			<!-- content here -->
			<table class="table table-striped">
				<!--[Tasks-Data-Headers]-->
				<thead>
					<tr>
						<th scope="col">#</th>
						<th scope="col">Severity</th>
						<th scope="col">Status</th>
						<th scope="col">Last Receive Time</th>
						<th scope="col">Dupl.</th>
						<th scope="col">Environment</th>
						<th scope="col">Service</th>
						<th scope="col">Resource</th>
						<th scope="col">Event</th>
						<th scope="col">Value</th>
						<th scope="col">Text</th>
					</tr>
				</thead>
				<!--[Tasks-Data-Body]-->
				<tbody>

					<!-- content here -->
					{#each alerts as myAlert, i}
						<tr>
							<th scope="row">{i + 1}</th>
							<td>{myAlert.severity}</td>
							<td>{myAlert.status}</td>
							<td>{myAlert.lastReceivedTime}</td>
							<td>{myAlert.dupl}</td>
							<td>{myAlert.environment}</td>
							<td>{myAlert.service}</td>
							<td>{myAlert.resource}</td>
							<td>{myAlert.event}</td>
							<td>{myAlert.value}</td>
							<td>{myAlert.text}</td>
						</tr>
					{/each}
				</tbody>
			</table>
		</div>
	</div>
</div>
