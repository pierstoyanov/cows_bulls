<script>
	import { Button } from 'sveltestrap';

	let secretNumber;

	async function generateSecretNumber () {
		const result = await fetch('/getSN');
		secretNumber = await result.json()
	}
	generateSecretNumber()


	let name = 'Cows and Bulls';

	function onSubmit (ev) {
		ev.preventDefault()
		console.log(secretNumber)
	}

</script>

<main>
	<div class="container">
		<h1>Wellcome to {name}!</h1>
		{secretNumber}
		<form id="user-unput" on:submit={onSubmit}>
			<input type="number" value="Your number:">
			<Button color='danger'>Enter</Button>
		</form>

	</div>
</main>


<style>

</style>