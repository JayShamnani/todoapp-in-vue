<template>
  <div>
    <Header />
    <SignUp />
    <Footer />
  </div>
</template>

<script>
import Header from "../components/Header";
import SignUp from "../components/SignUp";
import Footer from "../components/Footer";
export default {
  name: "signup",
  components: {
    Header,
    SignUp,
    Footer,
  },
};
</script>
