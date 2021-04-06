<template>
  <div>
    <Header />
    <AccountComp />
    <Footer />
  </div>
</template>

<script>
import Header from "../components/Header";
import Footer from "../components/Footer";
import AccountComp from "../components/AccountComp";

export default {
  name: "Account",
  components: {
    Header,
    AccountComp,
    Footer,
  },
};
</script>
