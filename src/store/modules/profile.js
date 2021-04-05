const state = {
  profileState: [],
};
const getters = {
  Profilestore: (state) => state.profileState,
};
const actions = {
  async addProfile({ commit }, Profile) {
    const res = await fetch("api/addprofile", {
      method: "POST",
      headers: {
        "Content-type": "application/json",
      },
      body: JSON.stringify(Profile),
    });
    const jsonres = res.json();
    commit("addProfile", jsonres);
  },
  async checkLogin({ commit }) {
    const res = await fetch("api/checkprofile");
    const jsonres = await res.json();
    commit("checkLogin", jsonres);
  },
};
const mutations = {
  addProfile: (state) => state,
  checkLogin: (state, jsonres) => (state.profileState = jsonres),
};
export default {
  state,
  getters,
  actions,
  mutations,
};
