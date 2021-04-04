<template>
  <div class="login container">
      <form class="col-md-12">
          <div>
            <label class="col-4">Username</label>
            <input type="text" class="col-8">
          </div>
          <div>
            <label class="col-4">Password</label>
            <input type="password" class="col-8">
          </div>
          <div class="subbutton">
            <button class="btn btn-info">Submit</button>
          </div>
      </form>
  </div>
</template>

<script>
export default {
  name: "LoginComp",
};
</script>

<style>
.subbutton{
    margin: 5px 0px;
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
