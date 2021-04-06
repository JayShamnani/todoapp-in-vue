const state = {
  taskstate: [],
  newtask: [],
};
const getters = {
  Taskstore: (state) => state.taskstate,
};
const actions = {
  async fetchtasks({ commit }, taskuser) {
    const res = await fetch(`/api/tasks/${taskuser}`);
    const jsondata = await res.json();
    commit("fetchtasks", jsondata);
  },

  async addTask({ commit }, newtask) {
    const res = await fetch("/api/taskcreate", {
      method: "POST",
      headers: {
        "Content-type": "application/json",
      },
      body: JSON.stringify(newtask),
    });
    const jsonres = await res.json();

    commit("addTask", jsonres);
  },

  async toggleReminder({ commit }, UpdatedTask) {
    const res = await fetch(`/api/taskupdate/${UpdatedTask.taskid}`, {
      method: "POST",
      headers: {
        "Content-type": "application/json",
      },
      body: JSON.stringify(UpdatedTask),
    });
    const jsonres = await res.json();
    commit("toggleReminder", jsonres);
  },
  async deleteTask({ commit }, Task) {
    const res = await fetch(`/api/taskdelete/${Task.taskid}`, {
      method: "DELETE",
      headers: {
        "Content-type": "application/json",
      },
    });
    const jsonres = await res.json();
    commit("deleteTask", jsonres);
  },
};
const mutations = {
  fetchtasks: (state, tasks) => (state.taskstate = tasks),
  addTask: (state, task) => state.newtask.unshift(task),
  toggleReminder: (state) => state,
  deleteTask: (state) => state,
};
export default {
  state,
  getters,
  actions,
  mutations,
};
