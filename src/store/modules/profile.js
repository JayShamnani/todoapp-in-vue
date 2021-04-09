const state = {
  accessToken: 0,
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
      process.env.VUE_APP_API_ENDPOINT + "api/createuser",
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
    var profileToken = "";
    if (localStorage.getItem("accessToken") === null) {
      profileToken = null;
      const errobject = {
        Results: false,
        Profile: 0,
      };
      commit("checkLogin", errobject);
    } else {
      profileToken = "Token " + localStorage.getItem("accessToken");
      const res = await fetch(
        process.env.VUE_APP_API_ENDPOINT + "api/checkprofile",
        {
          headers: {
            Authorization: profileToken,
          },
        }
      );
      const jsonres = await res.json();
      commit("checkLogin", jsonres);
    }
  },
  // Logining user in
  async profileLogin({ commit }, profiledata) {
    const res = await fetch(
      process.env.VUE_APP_API_ENDPOINT + "api/api-token-auth",
      {
        method: "POST",
        headers: {
          "Content-type": "application/json",
        },
        body: JSON.stringify(profiledata),
      }
    );
    const jsonres = await res.json();
    localStorage.setItem("accessToken", jsonres.token);
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
  async logoutuser({ commit }, username) {
    const res = await fetch(
      process.env.VUE_APP_API_ENDPOINT + "api/drf-token-delete",
      {
        method: "POST",
        headers: {
          "Content-type": "application/json",
        },
        body: JSON.stringify(username),
      }
    );
    const jres = await res.json();
    localStorage.removeItem("accessToken");

    commit("logoutuser", jres);
  },
};
const mutations = {
  addProfile: (state) => state,
  fetchProfileInfo: (state, rjson) => (state.fProfileState = rjson),
  checkLogin: (state, jsonres) => (
    (state.profileState = jsonres), (state.accessToken = jsonres.token)
  ),
  profileLogin: (state, jsonres) => (state.profileState = jsonres),
  checkUsername: (state, resjson) => (state.profileState = resjson),
  logoutuser: (state, jres) => (state.profileState = jres),
};
export default {
  state,
  getters,
  actions,
  mutations,
};
