import Vue from "vue";
import Vuex from "vuex";

import axios from "axios";
import createPersistedState from "vuex-persistedstate";
import router from "../router";

const API_URL = "http://127.0.0.1:8000";

Vue.use(Vuex);

export default new Vuex.Store({
  plugins: [createPersistedState()],
  state: {
    movies: [],
    token: null,
    articles: [],
  },
  getters: {
    isLogin(state) {
      return state.token ? true : false;
    },
  },
  mutations: {
    GET_MOVIES(state, movies) {
      state.movies = movies;
      console.log(movies);
    },
    GET_ARTICLES(state, articles) {
      state.articles = articles;
    },
    SAVE_TOKEN(state, token) {
      state.token = token;
      router.push({ name: "MovieView" });
    },
    DEL_TOKEN(state) {
      state.token = null;
      router.push({ name: "LoginView" });
    },
    GET_QUIZ(state, quiz) {
      state.quiz = quiz;
      console.log(JSON.parse(quiz.correct));
    },
  },
  actions: {
    getMovies(context) {
      axios({
        method: "get",
        url: `${API_URL}/movies/`,
      })
        .then((res) => {
          context.commit("GET_MOVIES", res.data);
        })
        .catch((err) => {
          console.log(err);
        });
    },
    getArticles(context) {
      axios({
        method: "get",
        url: `${API_URL}/community/`,
      })
        .then((res) => {
          context.commit("GET_ARTICLES", res.data);
        })
        .catch((err) => {
          console.log(err);
        });
    },

    signUp(context, payload) {
      const username = payload.username;
      const password1 = payload.password1;
      const password2 = payload.password2;
      console.log(username, password1, password2);

      axios({
        method: "post",
        url: `${API_URL}/rest-auth/signup/`,
        data: {
          username,
          password1,
          password2,
        },
      })
        .then((res) => {
          context.commit("SAVE_TOKEN", res.data.key);
        })
        .catch((err) => {
          console.log(err);
        });
    },
    login(context, payload) {
      const username = payload.username;
      const password = payload.password;

      axios({
        method: "post",
        url: `${API_URL}/rest-auth/login/`,
        data: {
          username,
          password,
        },
      })
        .then((res) => {
          context.commit("SAVE_TOKEN", res.data.key);
        })
        .catch((err) => {
          console.log(err);
        });
    },
    logout(context) {
      context.commit("DEL_TOKEN");
    },
    getQuiz(context) {
      axios({
        method: "get",
        url: `${API_URL}/movies/ostQuiz/`,
      })
        .then((res) => {
          context.commit("GET_QUIZ", res.data);
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
  modules: {},
});
