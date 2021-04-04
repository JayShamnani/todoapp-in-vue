<template>
  <div>
    <Header />
    <LoginComp />
    <Footer />
  </div>
</template>

<script>
import Header from "../components/Header";
import LoginComp from "../components/LoginComp";
import Footer from "../components/Footer";
export default {
  name: "login",
  components: {
    Header,
    LoginComp,
    Footer,
  },
};
</script>
