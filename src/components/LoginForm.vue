<template>
    <div class="container">
        <div class="row justify-content-center">

        <div class="col-sm-10">
            <label class="col-4">Username</label>
            <input class="col-7" type="text" name="Username" placeholder="Username">
        </div>

        <div class="col-sm-10">
            <label class="col-4">Name</label>
            <input class="col-7" type="text" name="Name" placeholder="Tony Stark">
        </div>
        
        <div class="col-sm-10">
            <label class="col-4">Email</label>
            <input class="col-7" type="email" name="Username" placeholder="me@example.com">
        </div>

        <div class="col-sm-10">
            <label class="col-4">Password</label>
            <input class="col-7" type="password" name="Password" placeholder="password">
        </div>
        <div class="buttons col-sm-6">
        <button type="button" class="btn btn-success">Submit</button>
        </div>
        </div>
    </div>
</template>

<script>
export default {
    name:"LoginForm"
}
</script>

<style scoped>
.container label{
    text-align: center;
}
.buttons{
    width: 100%;
    display: flex;
    justify-content: space-around;
}
</style>