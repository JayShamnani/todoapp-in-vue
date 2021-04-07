<template>
  <div class="fixedheader">
    <div class="header">
      <div class="logo">
        <router-link to="/" class="btn btn-secondary">To Do App</router-link>
      </div>
      <div class="buttons">
        <router-link to="/" class="btn btn-outline-primary">Home</router-link>
        <router-link
          v-if="Profilestore.Results"
          :to="Profilestore.Profile"
          class="btn btn-outline-success"
          >Account</router-link
        >
        <router-link v-else to="/login" class="btn btn-outline-success"
          >login</router-link
        >
        <router-link to="/about" class="btn btn-outline-info"
          >About</router-link
        >
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "Header",
  computed: mapGetters(["Profilestore"]),
};
</script>

<style scoped>
.fixedheader {
  position: fixed;
  top: 0%;
  width: 100%;
}
.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px;
  color: #ffffff;
  background-color: #121212;
  margin-bottom: 10px;
}

.buttons {
  width: 60%;
  display: flex;
  justify-content: space-around;
}
</style>
