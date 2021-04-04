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
        />
      </div>

      <div class="col-sm-10">
        <label class="col-4">Name</label>
        <input class="col-7" type="text" name="Name" placeholder="Tony Stark" />
      </div>

      <div class="col-sm-10">
        <label class="col-4">Email</label>
        <input
          class="col-7"
          type="email"
          name="Username"
          placeholder="me@example.com"
        />
      </div>

      <div class="col-sm-10">
        <label class="col-4">Password</label>
        <input
          class="col-7"
          type="password"
          name="Password"
          placeholder="password"
        />
      </div>
      <div class="col-sm-10 align-items-center loginbtn">
        <label>Already a Member ?</label>
        <button class="btn btn-light">Login</button>
      </div>
      <div class="buttons col-sm-6">
        <button type="button" class="btn btn-success">Submit</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "LoginForm",
};
</script>

<style scoped>
.container label {
  text-align: right;
  color: #fff;
}
.container {
  padding-top: 70px;
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
