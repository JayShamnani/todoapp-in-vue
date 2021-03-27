<template>
  <div>
	<Header />
	<div>
		<Tasks />
	</div>
	<Footer />
  </div>
</template>

<script>
import Header from "../components/Header";
import Footer from "../components/Footer";
import Tasks from "../components/Tasks";

export default {
  name: "Home",
  components: {
	Header,
	Footer,
	Tasks
  },
};
</script>