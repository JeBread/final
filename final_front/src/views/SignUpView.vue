<template>
  <div class="signup-page">
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
        <!-- 회원가입 form -->
        <form
          class="bg-gray-900 opacity-75 w-full shadow-lg rounded-lg px-8 pt-6 pb-8 mb-4"
          @submit.prevent="signUp"
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
              for="password1"
            >
            </label>
            <input
              class="shadow appearance-none border rounded w-full p-3 text-gray-700 leading-tight focus:ring transform transition hover:scale-105 duration-300 ease-in-out"
              type="password"
              id="password1"
              placeholder="Password"
              v-model="password1"
            /><br />

            <label
              class="block text-blue-300 py-2 font-bold mb-2"
              for="password2"
            >
            </label>
            <input
              class="shadow appearance-none border rounded w-full p-3 text-gray-700 leading-tight focus:ring transform transition hover:scale-105 duration-300 ease-in-out"
              type="password"
              id="password2"
              placeholder="PasswordConfirmation"
              v-model="password2"
            />
            <div class="flex items-center justify-between pt-4">
              <input
                class="bg-gradient-to-r from-purple-800 to-green-500 hover:from-pink-500 hover:to-green-500 text-white font-bold py-2 px-4 rounded focus:ring transform transition hover:scale-105 duration-300 ease-in-out"
                type="submit"
                value="SignUp"
              />
            </div>
          </div>
        </form>
      </div>
      <!-- Right Col -->
      <div class="w-full xl:w-3/5 p-12 overflow-hidden">
        <img
          class="mx-auto w-full md:w-4/5 transform -rotate-6 transition hover:scale-105 duration-700 ease-in-out hover:rotate-6"
          src="@/assets/macbook.svg"
        />
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "SignUpView",
  data() {
    return {
      username: null,
      password1: null,
      password2: null,
    };
  },
  methods: {
    signUp() {
      const username = this.username;
      const password1 = this.password1;
      const password2 = this.password2;

      const payload = {
        username,
        password1,
        password2,
      };

      this.$store.dispatch("signUp", payload);
    },
  },
};
</script>

<style>
.signup-page {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
}
</style>
