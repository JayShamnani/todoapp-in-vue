const state = {
  taskstate: [],
  newtask: [],
};
const getters = {
  Taskstore: (state) => state.taskstate,
};
const actions = {
  async fetchtasks({ commit }) {
    const res = await fetch("/api/tasklist");
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

  async toggleReminder(taskreminder) {
    const id = taskreminder.id;
    const res = await fetch(`/api/taskupdate/{}`);
    console.log(res, id);
  },
};
const mutations = {
  fetchtasks: (state, tasks) => (state.taskstate = tasks),
  addTask: (state, task) => state.newtask.unshift(task),
};
export default {
  state,
  getters,
  actions,
  mutations,
};
