<template>
  <div>
    <youtube :video-id="videoId" ref="youtube" style="display: none"></youtube>
    <button @click="playVideo">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        fill="none"
        viewBox="0 0 24 24"
        stroke-width="1.5"
        stroke="currentColor"
        class="w-14 h-14 hover:scale-125 duration-300 ease-in-out"
      >
        <path
          stroke-linecap="round"
          stroke-linejoin="round"
          d="M5.25 5.653c0-.856.917-1.398 1.667-.986l11.54 6.348a1.125 1.125 0 010 1.971l-11.54 6.347a1.125 1.125 0 01-1.667-.985V5.653z"
        />
      </svg>
    </button>
    <button @click="pauseVideo">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        fill="none"
        viewBox="0 0 24 24"
        stroke-width="1.5"
        stroke="currentColor"
        class="w-14 h-14 hover:scale-125 duration-300 ease-in-out"
      >
        <path
          stroke-linecap="round"
          stroke-linejoin="round"
          d="M15.75 5.25v13.5m-7.5-13.5v13.5"
        />
      </svg>
    </button>
  </div>
</template>

<script>
import Vue from "vue";
import VueYoutube from "vue-youtube";

Vue.use(VueYoutube);

export default {
  name: "YoutubePlayer",
  props: {
    videoId: String,
  },
  data() {
    return {
      playerVars: {
        autoplay: 1,
      },
    };
  },
  components: {},
  computed: {
    player() {
      return this.$refs.youtube.player;
    },
  },
  methods: {
    playVideo() {
      const iframe = document.querySelectorAll("iframe");
      iframe.forEach((tag) => {
        if (tag.getAttribute("title").trim() === "YouTube video player") {
          alert("동영상 오류\n다음 문제로 넘어갑니다.");
          this.$emit("evt");
        }
      });
      this.player.playVideo();
    },
    pauseVideo() {
      this.player.pauseVideo();
    },
  },
};
</script>

<style scoped>
iframe {
  width: 0px;
  height: 0px;
}
</style>
