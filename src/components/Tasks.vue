<template>
  <div class="tasks">
    <div
      @dblclick="togglereminder(items.id)"
      v-for="items in tasks"
      :key="items.id"
      :class="[items.reminder ? 'task-reminder' : 'task', 'task']"
    >
      <div class="taskheading">{{ items.task }}</div>
      <div class="taskbody">{{ items.body }}</div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Tasks",
  data() {
    return {
      tasks: [
        {
          id: 1,
          task: "Task 1",
          body: "Appoitment with Doctor",
          reminder: true,
        },
        {
          id: 2,
          task: "Task 2",
          body: "Appoitment with Doctor",
          reminder: true,
        },
        {
          id: 3,
          task: "Task 3",
          body: "Appoitment with Doctor",
          reminder: true,
        },
        {
          id: 4,
          task: "Task 4",
          body: "Appoitment with Doctor",
          reminder: false,
        },
        {
          id: 5,
          task: "Task 5",
          body: "Appoitment with Doctor",
          reminder: true,
        },
        {
          id: 6,
          task: "Task 6",
          body: "Appoitment with Doctor",
          reminder: false,
        },
        {
          id: 7,
          task: "Task 7",
          body: "Appoitment with Doctor",
          reminder: true,
        },
        {
          id: 8,
          task: "Task 8",
          body: "Appoitment with Doctor",
          reminder: true,
        },
      ],
    };
  },
  methods: {
    togglereminder(id) {
      this.tasks = this.tasks.map((tasks) =>
        tasks.id === id ? { ...tasks, reminder: !tasks.reminder } : tasks
      );
    },
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
