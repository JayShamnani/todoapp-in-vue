<template>
  <div>
    <Header />
    <div>
      <Tasks />
      <AddTask />
    </div>
    <Footer />
  </div>
</template>

<script>
import Header from "../components/Header";
import Footer from "../components/Footer";
import Tasks from "../components/Tasks";
import AddTask from "../components/addTask";

export default {
  name: "Home",
  components: {
    Header,
    Footer,
    Tasks,
    AddTask,
  },
};
</script>
