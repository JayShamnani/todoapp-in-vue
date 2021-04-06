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
    const jsonres = await res.json();
    commit("addProfile", jsonres);
  },
  async checkLogin({ commit }) {
    const res = await fetch("api/checkprofile");
    const jsonres = await res.json();
    commit("checkLogin", jsonres);
  },
  async profileLogin({ commit }, profiledata) {
    const res = await fetch("api/profilelogin", {
      method: "POST",
      headers: {
        "Content-type": "application/json",
      },
      body: JSON.stringify(profiledata),
    });
    const jsonres = await res.json();
    commit("profileLogin", jsonres);
  },

  async checkUsername({ commit }, username) {
    const res = await fetch("api/checkusername", {
      method: "POST",
      headers: {
        "Content-type": "application/json",
      },
      body: JSON.stringify(username),
    });
    const resjson = await res.json();
    commit("checkUsername", resjson);
  },
};
const mutations = {
  addProfile: (state) => state,
  checkLogin: (state, jsonres) => (state.profileState = jsonres),
  profileLogin: (state, jsonres) => (state.profileState = jsonres),
  checkUsername: (state, resjson) => (state.profileState = resjson),
};
export default {
  state,
  getters,
  actions,
  mutations,
};
