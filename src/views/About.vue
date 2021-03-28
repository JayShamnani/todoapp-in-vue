<template>
  <div>
    <Header />
    <div class="about">
      <h1>About</h1>
      <p>This is simple To Do Application</p>
      <h2>Technical Specifications</h2>
      <h3>Frontend:</h3>
      <h6>Vue, Bootstrap</h6>
      <h3>Backend:</h3>
      <h6>Django, DRF(REST API)</h6>
      <h3>Version Control:</h3>
      <h6>Git, GitHub</h6>
      <h3>Vue</h3>
      <h6>Vue 3.0.0, Vue Router 4.0.0, Vuex 3.6.2</h6>
      <h3>Bootstrap</h3>
      <h6>4.5.2</h6>
      <h3>Django</h3>
      <h6>Django</h6>
    </div>
    <Footer />
  </div>
</template>

<script>
import Header from "@/components/Header";
import Footer from "@/components/Footer";
export default {
  name: "about",
  components: {
    Header,
    Footer,
  },
};
</script>

<style scoped>
.about {
  color: #ffffff;
  padding: 70px;
}
</style>
