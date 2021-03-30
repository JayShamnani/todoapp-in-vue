<template>
  <div class="addTaskContainer">
    <div class="addTask">
      <form class="addForm">
        <div class="col-sm-12">
          <label class="col-4">Heading</label>
          <input class="col-7" type="text" v-model="head" name="head" />
        </div>
        <div class="col-sm-12">
          <label class="col-4">Task</label>
          <input class="col-7" type="text" v-model="body" name="body" />
        </div>
        <div class="col-sm-12">
          <label class="col-4">Reminder</label>
          <input type="checkbox" v-model="reminder" name="reminder" />
        </div>
      </form>
      <div class="addtaskBtn">
        <button class="btn btn-success">Add Task</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "addTask",
  data() {
    return {
      head: "",
      body: "",
      reminder: false,
    };
  },
};
</script>

<style scoped>
.addTaskContainer {
  padding-bottom: 50px;
  display: flex;
  justify-content: space-around;
  color: #fff;
}
.addTask {
  width: 80%;
  background: #121212;
  display: flex;
  flex-direction: column;
  align-items: center;
  border-radius: 10px;
  padding-top: 5px;
}

.addtaskBtn {
  padding: 5px;
}

.addForm {
  width: 100%;
  display: block;
  /* flex-direction: column; */
  padding: 5px;
}
form label {
  text-align: right;
}
form input {
  border: none;
  background-color: #3c403c;
  border-radius: 5px;
  color: #fff;
}
</style>
