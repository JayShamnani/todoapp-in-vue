const state = {
  profileState: [],
  fProfileState: [],
};
const getters = {
  Profilestore: (state) => state.profileState,
  UserProfilestore: (state) => state.fProfileState,
};
const actions = {
  // Sign up method
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
  // Checking user login
  async checkLogin({ commit }) {
    const res = await fetch(
      process.env.VUE_APP_API_ENDPOINT + "api/checkprofile"
    );
    const jsonres = await res.json();
    commit("checkLogin", jsonres);
  },
  // Logining user in
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
  // Checking username on sign up
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
  // for profile page
  async fetchProfileInfo({ commit }, username) {
    const res = await fetch(
      process.env.VUE_APP_API_ENDPOINT + `api/getprofile/${username}`
    );
    const rjson = await res.json();
    commit("fetchProfileInfo", rjson);
  },
  // Logining user out
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
