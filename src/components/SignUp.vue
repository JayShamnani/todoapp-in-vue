<template>
  <div class="container">
    <div class="row justify-content-center">
      <div class="col-sm-10">
        <label class="col-4">Username</label>
        <input
          class="col-7"
          type="text"
          name="Username"
          placeholder="Username"
          v-model="Username"
        />
      </div>

      <div class="col-sm-10">
        <label class="col-4">Name</label>
        <input
          class="col-7"
          v-model="Name"
          type="text"
          name="Name"
          placeholder="Tony Stark"
        />
      </div>

      <div class="col-sm-10">
        <label class="col-4">Password</label>
        <input
          class="col-7"
          v-model="Password"
          type="password"
          name="Password"
          placeholder="password"
        />
        <p style="color: #fff">One lowercase and uppercase letters required</p>
        <p style="color: #fff">8 characters minimum</p>
        <p style="color: #fff">One number and special character required</p>
      </div>
      <div class="col-sm-10 align-items-center loginbtn">
        <label>Already a Member ?</label>
        <router-link to="/login" class="btn btn-light">Login</router-link>
      </div>
      <div class="buttons col-sm-6">
        <button type="button" @click="onSubmit()" class="btn btn-success">
          Submit
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions } from "vuex";

export default {
  name: "LoginForm",
  data() {
    return {
      Username: "",
      Name: "",
      Password: "",
    };
  },
  methods: {
    ...mapActions(["addProfile"]),
    onSubmit() {
      const username = this.Username;
      const password = this.Password;
      if (username.match(/^[A-Za-z0-9_@.-]*$/)) {
        if (
          password.match(
            /^(?=.*[0-9])(?=.*[!@#$%^&*])[a-zA-Z0-9!@#$%^&*]{6,36}$/
          )
        ) {
          const UserProfile = {
            username: this.Username,
            name: this.Name,
            password: this.Password,
          };
          this.$emit("profileinfo", UserProfile);
          this.addProfile(UserProfile);
          this.$router.push({ name: "Home" });
        } else {
          alert("Password doesn't meet requirement");
        }
      } else {
        alert(
          this.Username +
            String(
              " is not allowed, only alphanumeric character with @._- are allowed"
            )
        );
      }
    },
  },
};
</script>

<style scoped>
.container label {
  text-align: right;
  color: #fff;
}
.container {
  padding-top: 70px;
  padding-bottom: 50px;
}
.buttons {
  margin-top: 5px;
  width: 100%;
  display: flex;
  justify-content: space-around;
}

.loginbtn {
  color: #fff;
  display: flex;
  margin: 8px 0px;
  justify-content: space-evenly;
}

.loginbtn button {
  padding: 5px;
}

input {
  background-color: #3c403c;
  color: #fff;
  border: none;
  border-radius: 5px;
  margin-top: 5px;
  /* padding: 3px; */
}

input[type="text"] {
  padding: 5px 10px;
}
input[type="email"] {
  padding: 5px 10px;
}
input[type="password"] {
  padding: 5px 10px;
}
</style>
