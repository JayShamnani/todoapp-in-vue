<template>
	<div>
		<Header />
		<div class="about">
			<h1>This is an about page</h1>
		</div>
		<Footer />
	</div>
</template>

<script>

import Header from '@/components/Header'
import Footer from '@/components/Footer'
export default {
  name: 'about',
  components:{
    Header,
    Footer
  }
}
</script>
