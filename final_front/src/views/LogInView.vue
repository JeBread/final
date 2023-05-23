<template>
  <div class="login-page">
    <!-- Main -->
    <div
      class="container pt-24 md:pt-36 mx-auto flex flex-wrap flex-col md:flex-row items-center"
    >
      <!-- Left Col -->
      <div
        class="flex flex-col w-full xl:w-2/5 justify-center lg:items-start overflow-y-hidden"
      >
        <h1
          class="my-4 text-3xl md:text-5xl text-white opacity-75 font-bold leading-tight text-center md:text-left"
        >
          Main
          <span
            class="bg-clip-text text-transparent bg-gradient-to-r from-green-400 via-pink-500 to-purple-500"
          >
            Hero Message
          </span>
          to sell yourself!
        </h1>
        <p
          class="leading-normal text-base md:text-2xl mb-8 text-center md:text-left"
        >
          Sub-hero message, not too long and not too short. Make it just right!
        </p>
        <!-- 로그인 form -->
        <form
          class="bg-gray-900 opacity-75 w-full shadow-lg rounded-lg px-8 pt-6 pb-8 mb-4"
          @submit.prevent="login"
        >
          <div class="mb-4">
            <label
              class="block text-blue-300 py-2 font-bold mb-2"
              for="username"
            >
            </label>
            <input
              class="shadow appearance-none border rounded w-full p-3 text-gray-700 leading-tight focus:ring transform transition hover:scale-105 duration-300 ease-in-out"
              type="text"
              id="username"
              placeholder="Name"
              v-model="username"
            /><br />

            <label
              class="block text-blue-300 py-2 font-bold mb-2"
              for="password"
            >
            </label>
            <input
              class="shadow appearance-none border rounded w-full p-3 text-gray-700 leading-tight focus:ring transform transition hover:scale-105 duration-300 ease-in-out"
              type="password"
              id="password"
              placeholder="Password"
              v-model="password"
            />
            <div class="flex items-center justify-between pt-4">
              <input
                class="bg-gradient-to-r from-purple-800 to-green-500 hover:from-pink-500 hover:to-green-500 text-white font-bold py-2 px-4 rounded focus:ring transform transition hover:scale-105 duration-300 ease-in-out"
                type="submit"
                value="logIn"
              />
            </div>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "LogInView",
  data() {
    return {
      username: null,
      password: null,
    };
  },
  methods: {
    login() {
      const username = this.username;
      const password = this.password;

      const payload = {
        username,
        password,
      };

      this.$store.dispatch("login", payload);
    },
  },
};
</script>

<style>
.login-page {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
}
</style>
