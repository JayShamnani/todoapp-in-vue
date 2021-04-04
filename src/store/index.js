import { createStore } from "vuex";
import taskstores from "./modules/task";
import Profilestore from "./modules/profile";

export default createStore({
  state: {},
  mutations: {},
  actions: {},
  modules: {
    taskstores,
    Profilestore,
  },
});
