<template>
  <div class="accountcontainer container">
    <div class="col-sm-10 justify-content-center">
      <div class="accountname">
        <h3>Name</h3>
        <h1>{{ Profilename }}</h1>
      </div>
      <div class="numberofposts">
        <h6>Username</h6>
        <h3>{{ Username }}</h3>
      </div>
      <div v-if="Profilestore.Profile !== 0" class="logout">
        <button class="btn btn-outline-danger" @click="logout">Logout</button>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
export default {
  name: "AccountComp",
  data() {
    return {
      Profilename: "",
      Username: "",
    };
  },
  computed: mapGetters(["Profilestore", "Taskstore", "UserProfilestore"]),
  methods: {
    ...mapActions(["fetchProfileInfo", "checkLogin", "logoutuser"]),
    logout() {
      const profiledict = {
        user: this.UserProfilestore[0].username,
      };
      this.logoutuser(profiledict).then(() => {
        this.$router.push({ name: "Home" }).then(() => {
          location.reload();
        });
      });
    },
  },
  created() {
    this.checkLogin().then(() => {
      if (this.Profilestore.Profile === 0) {
        alert("Your are not authorized to view this page");
        this.$router.push({ name: "Home" });
      } else {
        this.fetchProfileInfo(this.Profilestore.Profile).then(() => {
          this.Username = this.UserProfilestore[0].username;
          this.Profilename = this.UserProfilestore[0].name;
        });
      }
    });
  },
};
</script>

<style scoped>
.accountcontainer {
  padding-top: 70px;
  padding-bottom: 50px;
  color: #fff;
  width: 80%;
}
.accountdetails {
  display: flex;
  justify-content: space-between;
}

.accountname {
  padding: 20px 0px;
}
.logout {
  padding: 20px 0px;
}
</style>
