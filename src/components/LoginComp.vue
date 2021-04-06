<template>
  <div class="login container">
    <form class="col-md-12">
      <div>
        <label class="col-4">Username</label>
        <input v-model="username" type="text" class="col-8" />
      </div>
      <div>
        <label class="col-4">Password</label>
        <input v-model="password" type="password" class="col-8" />
      </div>
    </form>
    <div class="notauser">
      <label>Not a User ?</label>
      <router-link to="/signup" class="btn btn-outline-warning"
        >Sign Up</router-link
      >
    </div>
    <div class="subbutton">
      <button @click="onSubmitss()" class="btn btn-info">Submit</button>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";

export default {
  name: "LoginComp",
  computed: mapGetters(["Profilestore"]),
  data() {
    return {
      username: "",
      password: "",
    };
  },
  methods: {
    ...mapActions(["profileLogin"]),
    onSubmitss() {
      const profileData = {
        username: this.username,
        password: this.password,
      };
      this.profileLogin(profileData)
        .then(() => {
          if (this.Profilestore["Results"] === true) {
            this.$router.push({ name: "Home" });
          } else {
            throw this.Profilestore["Results"];
          }
        })
        .catch(() => {
          if (this.Profilestore["Results"] === "PasswordError") {
            alert("Password Error");
          } else {
            alert("User Does not Exists");
          }
        });
    },
  },
};
</script>

<style scoped>
.notauser {
  margin: 10px 0px;
  display: flex;
  justify-content: space-evenly;
}
.subbutton {
  margin: 8px 0px;
  display: flex;
  justify-content: center;
}
.login {
  padding-top: 80px;
  color: #fff;
}
form {
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  align-items: center;
}
input {
  background-color: #3c403c;
  color: #fff;
  border: none;
  border-radius: 5px;
  margin: 5px 0px;
}

input[type="text"] {
  padding: 5px 10px;
}
input[type="password"] {
  padding: 5px 10px;
}
</style>
