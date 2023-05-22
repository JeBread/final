<template>
    <div>
        <youtube :video-id="videoId" ref="youtube" style="display:none;"></youtube>
        <button @click="playVideo">재생</button>
        <button @click="pauseVideo">일시정지</button>
    </div>
  </template>

<script>
import Vue from 'vue'
import VueYoutube from 'vue-youtube'
 
Vue.use(VueYoutube)

export default {
  name: "YoutubePlayer",
  props:{
    videoId:String
  },
  data() {
    return {
        
      playerVars: {
        autoplay: 1
      }
    }
  },
  components: {
    
  },
  computed: {
    player() {
      return this.$refs.youtube.player
    }
  },
  methods:{
    playVideo() {
      this.player.playVideo()
    },
    pauseVideo() {
      this.player.pauseVideo()
    },
  }
};
</script>

<style scoped>
iframe {
  width: 0px;
  height: 0px;
}
</style>