<template>
  <div>
    <h1>퀴즈 페이지</h1>
    <YoutubePlayer :video-id="videoId"/>
    <button @click="getQuiz">새로고침</button>
    <br>
    <div v-for="(img,idx) in imgs" :key="idx" style="display: inline-block;">
      <img :src="img.imgPath" height=180 width=180 style="margin:30px;" @click="check(img.title)">
    </div>
    
  </div>
</template>

<script>
import YoutubePlayer from '@/components/YoutubePlayer.vue';
import axios from 'axios'
import _ from "lodash"

const API_URL = "http://127.0.0.1:8000";
const imgURL='https://image.tmdb.org/t/p/original'

export default {
  name: "QuizView",
  components: {YoutubePlayer,},
  data(){
    return{
      videoId:'',
      correct:null,
      uncorrect1:null,
      uncorrect2:null,
      imgs:[],
    }
  },
  computed: {},
  created() {
    this.getQuiz();
  },
  beforeUpdated(){
    this.getQuiz();
  },
  methods: {
    getQuiz() {
      axios({
        method: "get",
        url: `${API_URL}/movies/ostQuiz/`,
      })
        .then((res) => {

          const correct=JSON.parse(res.data.correct)[0]
          const uncorrect1=JSON.parse(res.data.uncorrect1)[0]
          const uncorrect2=JSON.parse(res.data.uncorrect2)[0]

          this.videoId=correct.fields.ost
          this.correct=correct
          this.uncorrect1=uncorrect1
          this.uncorrect2=uncorrect2
          this.imgs=[]
          this.imgs.push({imgPath:imgURL+correct.fields.poster_path,title:correct.fields.title})
          this.imgs.push({imgPath:imgURL+uncorrect1.fields.poster_path,title:uncorrect1.fields.title})
          this.imgs.push({imgPath:imgURL+uncorrect2.fields.poster_path,title:uncorrect2.fields.title})
          this.imgs=_.shuffle(this.imgs)

        })
        .catch((err) => {
          console.log(err);
        });
    },
    check(imgTitle){
      if(imgTitle===this.correct.fields.title){
        axios({
          method: "get",
          url: `${API_URL}/movies/ostQuiz/correct`,
          params: {
            pk:this.correct.pk
          },
        })
          .then(() => {
            // console.log('suc')
            // console.log(res)
          })
          .catch((err) => {
            console.log(err);
          });
        
        alert("정답")
      }
      else{
        alert("오답")
      }
    },
    refresh(){
      axios({
        method: "get",
        url: `${API_URL}/movies/ostQuiz/`,
        
      })
        .then((res) => {
          
          const correct=JSON.parse(res.data.correct)[0].fields
          const uncorrect1=JSON.parse(res.data.uncorrect1)[0].fields
          const uncorrect2=JSON.parse(res.data.uncorrect2)[0].fields

          this.videoId=correct.ost
          this.correct=correct
          this.uncorrect=uncorrect1
          this.uncorrect2=uncorrect2
          this.imgs=[]
          this.imgs.push({imgPath:imgURL+correct.poster_path,title:correct.title})
          this.imgs.push({imgPath:imgURL+uncorrect1.poster_path,title:uncorrect1.title})
          this.imgs.push({imgPath:imgURL+uncorrect2.poster_path,title:uncorrect2.title})
          this.imgs=_.shuffle(this.imgs)

        })
        .catch((err) => {
          console.log(err);
        });
    }
  },
};
</script>

<style></style>
