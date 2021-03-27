<template>
<div>
    <Header />
    <LoginForm />
    <Footer />
    </div>
</template>

<script>
import Header from "../components/Header";
import LoginForm from "../components/LoginForm";
import Footer from "../components/Footer";
export default {
  name:"Login",
	components:{
		Header,
		LoginForm,
		Footer,
	}
}
</script>