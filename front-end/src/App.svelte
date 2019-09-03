<script>
	import Navigation from './Navigation.svelte';
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
	<div class="row">
		<div class="col-sm-12">
			<!--[Tabs]-->
			<dir>
				<ul class="nav nav-pills mb-3" id="pills-tab" role="tablist">
					<li class="nav-item">
						<a
							class="nav-link active"
							id="pills-all-tab"
							data-toggle="pill"
							href="#pills-all"
							role="tab"
							aria-controls="pills-all"
							aria-selected="true">
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
							aria-selected="false">
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
							aria-selected="false">
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
							aria-selected="false">
							Development
						</a>
					</li>
				</ul>
				<div class="tab-content" id="pills-tabContent">
					<div
						class="tab-pane fade show active"
						id="pills-all"
						role="tabpanel"
						aria-labelledby="pills-all-tab">
						...all data
					</div>
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
			</dir>
		</div>
	</div>
</div>
