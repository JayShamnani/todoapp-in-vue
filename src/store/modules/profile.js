const state = {
  profileState: [],
  fProfileState: [],
};
const getters = {
  Profilestore: (state) => state.profileState,
  UserProfilestore: (state) => state.fProfileState,
};
const actions = {
  async addProfile({ commit }, Profile) {
    const res = await fetch(
      process.env.VUE_APP_API_ENDPOINT + "api/addprofile",
      {
        method: "POST",
        headers: {
          "Content-type": "application/json",
        },
        body: JSON.stringify(Profile),
      }
    );
    const jsonres = await res.json();
    commit("addProfile", jsonres);
  },
  async checkLogin({ commit }) {
    const res = await fetch(
      process.env.VUE_APP_API_ENDPOINT + "api/checkprofile"
    );
    const jsonres = await res.json();
    commit("checkLogin", jsonres);
  },
  async profileLogin({ commit }, profiledata) {
    const res = await fetch(
      process.env.VUE_APP_API_ENDPOINT + "api/profilelogin",
      {
        method: "POST",
        headers: {
          "Content-type": "application/json",
        },
        body: JSON.stringify(profiledata),
      }
    );
    const jsonres = await res.json();
    commit("profileLogin", jsonres);
  },

  async checkUsername({ commit }, username) {
    const res = await fetch(
      process.env.VUE_APP_API_ENDPOINT + "api/checkusername",
      {
        method: "POST",
        headers: {
          "Content-type": "application/json",
        },
        body: JSON.stringify(username),
      }
    );
    const resjson = await res.json();
    commit("checkUsername", resjson);
  },

  async fetchProfileInfo({ commit }, username) {
    const res = await fetch(
      process.env.VUE_APP_API_ENDPOINT + `api/getprofile/${username}`
    );
    const rjson = await res.json();
    commit("fetchProfileInfo", rjson);
  },

  async logoutuser({ commit }) {
    const res = await fetch(process.env.VUE_APP_API_ENDPOINT + "api/logout");
    const jres = await res.json();

    commit("logoutuser", jres);
  },
};
const mutations = {
  addProfile: (state) => state,
  fetchProfileInfo: (state, rjson) => (state.fProfileState = rjson),
  checkLogin: (state, jsonres) => (state.profileState = jsonres),
  profileLogin: (state, jsonres) => (state.profileState = jsonres),
  checkUsername: (state, resjson) => (state.profileState = resjson),
  logoutuser: (state) => state,
};
export default {
  state,
  getters,
  actions,
  mutations,
};
