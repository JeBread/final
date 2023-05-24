<template>
    <div>
        <youtube :video-id="videoId" ref="youtube" style=""></youtube>
    </div>
  </template>

<script>
import Vue from 'vue'
import VueYoutube from 'vue-youtube'
 
Vue.use(VueYoutube)

export default {
  name: "MovieVideoPlayer",
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

</style>