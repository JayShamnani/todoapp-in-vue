const state = {
  taskstate: [],
};
const getters = {
  Taskstore: (state) => state.taskstate,
};
const actions = {
  async fetchtasks({ commit }) {
    const res = await fetch("/api/tasklist");
    const jsondata = await res.json();
    console.log(jsondata);

    commit("fetchtasks", jsondata);
  },
};
const mutations = {
  fetchtasks: (state, tasks) => (state.taskstate = tasks),
};
export default {
  state,
  getters,
  actions,
  mutations,
};
