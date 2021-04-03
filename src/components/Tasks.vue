<template>
  <div class="tasks">
    <div
      @dblclick="togglereminder(items.taskid)"
      v-for="items in Taskstore"
      :key="items.id"
      :class="[items.reminder ? 'taskreminder' : 'task', 'task']"
    >
      <div class="taskheading">{{ items.taskhead }}</div>
      <div class="taskbody">{{ items.taskbody }}</div>
      <div class="taskauthor">{{ items.taskauthor }}</div>
    </div>
  </div>
  <addTask @addTask="addTask" />
</template>

<script>
import { mapGetters, mapActions } from "vuex";
import addTask from "../components/addTask";

export default {
  name: "Tasks",
  components: {
    addTask,
  },
  data() {
    return {
      tasks: [],
    };
  },

  computed: mapGetters(["Taskstore"]),

  methods: {
    ...mapActions(["fetchtasks"]),
    togglereminder(id) {
      this.tasks = this.tasks.map((tasks) =>
        tasks.id === id ? { ...tasks, reminder: !tasks.reminder } : tasks
      );
    },
    addTask(newTask) {
      this.Taskstore.push(newTask);
    },
  },
  created() {
    this.fetchtasks();
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
