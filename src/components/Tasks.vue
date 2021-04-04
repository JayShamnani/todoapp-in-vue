<template>
  <div class="tasks">
    <div
      v-for="items in Taskstore"
      :key="items.taskid"
      @dblclick="togglereminder(items)"
      :class="[
        items.tasknull
          ? 'task-null'
          : [items.taskreminder ? 'task-reminder' : 'none', 'task'],
      ]"
    >
      <div class="taskheading">{{ items.taskhead }}</div>
      <div class="taskbody">{{ items.taskbody }}</div>
      <div class="delete">
        <div class="taskauthor">{{ items.taskauthor }}</div>
        <i @click="deletetask(items)" class="far fa-trash-alt"></i>
      </div>
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
    ...mapActions(["fetchtasks", "toggleReminder"]),
    togglereminder(id) {
      id.taskreminder = !id.taskreminder;
      const updatedTask = {
        taskid: id.taskid,
        taskhead: id.taskhead,
        taskbody: id.taskbody,
        taskreminder: id.taskreminder,
        taskauthor: id.taskauthor,
      };
      this.toggleReminder(updatedTask);
    },
    addTask(newTask) {
      this.Taskstore.push(newTask);
    },
    deletetask(id) {
      id.tasknull = true;
    },
  },
  created() {
    this.fetchtasks();
  },
};
</script>

<style scoped>
.delete {
  display: flex;
  justify-content: space-between;
}
.delete i {
  cursor: pointer;
}
.task-null {
  display: none;
  transition: 3s ease;
}
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
  user-select: none;
  border-left: solid 10px rgba(0, 0, 0, 0);
  transition: 0.3s ease;
}
.task-reminder {
  border-left: solid 10px green;
  transition: 0.3s ease;
}
.taskheading {
  font-size: 30px;
  font-weight: 600;
}
</style>
