/* eslint-disable */
<template>
  <div class="tasks">
    <div
      @dblclick="togglereminder(items.taskid)"
      v-for="items in tasks"
      :key="items.taskid"
      :class="[items.reminder ? 'taskreminder' : 'task', 'task']"
    >
      <div class="taskheading">{{ items.taskhead }}</div>
      <div class="taskbody">{{ items.taskbody }}</div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Tasks",
  data() {
    return {
      tasks: [],
    };
  },

  methods: {
    togglereminder(id) {
      this.tasks = this.tasks.map((tasks) =>
        tasks.id === id ? { ...tasks, reminder: !tasks.reminder } : tasks
      );
    },
    async fetchtasks() {
      const res = await fetch("/api/tasklist");
      const data = await res.json();
      console.log(data[0]);
      return data;
    },
  },
  created() {
    this.tasks = this.fetchtasks();
  },
};
</script>

<style scoped>
.tasks {
  text-align: left;
  color: #ffffff;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding-bottom: 50px;
  padding-top: 70px;
}
.task {
  background: #121212;
  width: 80%;
  margin: 5px 0px;
  padding: 8px 20px;
  min-height: 50px;
  border-radius: 8px;
  cursor: pointer;
  user-select: none;
  border-left: solid 10px rgba(0, 0, 0, 0);
}
.task-reminder {
  border-left: solid 10px green;
}
.taskheading {
  font-size: 30px;
  font-weight: 600;
}
</style>
