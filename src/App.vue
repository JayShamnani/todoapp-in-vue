<template>
  <div class="todoapp">
    <router-view />
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";

export default {
  name: "App",
  methods: {
    ...mapActions(["checkLogin"]),
  },
  computed: mapGetters(["Profilestore"]),
  created() {
    this.checkLogin();
  },
};
</script>
