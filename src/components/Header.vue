<template>
    <div class="header">
        <div class="logo">
            <router-link to="/" class="btn btn-secondary">To Do App</router-link></div>
        <div class="buttons">

            <router-link to="/" class="btn btn-outline-primary">Home</router-link>
            <router-link to="/login" class="btn btn-outline-success">Login</router-link>
            <router-link to="/about" class="btn btn-outline-info">About</router-link>
        </div>
    </div>
</template>

<script>
export default {
    name: 'Header'
}
</script>

<style scoped>
.header{
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px;
    color: #FFFFFF;
    background-color: #1F1B24;
    margin-bottom: 10px;
}

.buttons{
    width: 50%;
    display: flex;
    justify-content: space-around;
}
</style>