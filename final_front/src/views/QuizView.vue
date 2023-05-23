<template>
  <div>
    <h1>Quiz</h1>
    <YoutubePlayer class="mt-5" :video-id="videoId" @evt="refresh" />
    <button @click="getQuiz">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        fill="none"
        viewBox="0 0 24 24"
        stroke-width="1.5"
        stroke="currentColor"
        class="w-12 h-12"
      >
        <path
          stroke-linecap="round"
          stroke-linejoin="round"
          d="M15 15l6-6m0 0l-6-6m6 6H9a6 6 0 000 12h3"
        />
      </svg>
    </button>
    <br />
    <div v-for="(img, idx) in imgs" :key="idx" style="display: inline-block">
      <img
        :src="img.imgPath"
        style="margin: 30px; height: 220px; width: 180px"
        @click="check(img.title)"
      />
    </div>
  </div>
</template>

<script>
import YoutubePlayer from "@/components/YoutubePlayer.vue";
import axios from "axios";
import _ from "lodash";

const API_URL = "http://127.0.0.1:8000";
const imgURL = "https://image.tmdb.org/t/p/original";

export default {
  name: "QuizView",
  components: { YoutubePlayer },
  data() {
    return {
      videoId: "",
      correct: null,
      uncorrect1: null,
      uncorrect2: null,
      imgs: [],
    };
  },
  computed: {},
  created() {
    this.getQuiz();
    // const iframe=document.querySelectorAll("iframe")
    // iframe.forEach((tag)=>{
    //   if(tag.getAttribute("title").trim()==="YouTube video player"){
    //     alert("동영상 오류")
    //   }
    // })
  },
  beforeUpdated() {
    this.getQuiz();
  },
  mounted() {},
  updated() {},
  methods: {
    getQuiz() {
      axios({
        method: "get",
        url: `${API_URL}/movies/ostQuiz/`,
      })
        .then((res) => {
          const correct = JSON.parse(res.data.correct)[0];
          const uncorrect1 = JSON.parse(res.data.uncorrect1)[0];
          const uncorrect2 = JSON.parse(res.data.uncorrect2)[0];

          this.videoId = correct.fields.ost;
          this.correct = correct;
          this.uncorrect1 = uncorrect1;
          this.uncorrect2 = uncorrect2;
          this.imgs = [];
          this.imgs.push({
            imgPath: imgURL + correct.fields.poster_path,
            title: correct.fields.title,
          });
          this.imgs.push({
            imgPath: imgURL + uncorrect1.fields.poster_path,
            title: uncorrect1.fields.title,
          });
          this.imgs.push({
            imgPath: imgURL + uncorrect2.fields.poster_path,
            title: uncorrect2.fields.title,
          });
          this.imgs = _.shuffle(this.imgs);
        })
        .catch((err) => {
          console.log(err);
        });
    },
    check(imgTitle) {
      
      if (imgTitle === this.correct.fields.title) {
        axios({
          method: "get",
          url: `${API_URL}/movies/ostQuiz/correct`,
          params: {
            pk: this.correct.pk,
          },
        })
          .then(() => {
            // console.log('suc')
            // console.log(res)
          })
          .catch((err) => {
            console.log(err);
          });

        alert("정답");
      } else {
        alert("오답");
      }
    },
    refresh() {
      axios({
        method: "get",
        url: `${API_URL}/movies/ostQuiz/`,
      })
        .then((res) => {
          const correct = JSON.parse(res.data.correct)[0].fields;
          const uncorrect1 = JSON.parse(res.data.uncorrect1)[0].fields;
          const uncorrect2 = JSON.parse(res.data.uncorrect2)[0].fields;

          this.videoId = correct.ost;
          this.correct = correct;
          this.uncorrect = uncorrect1;
          this.uncorrect2 = uncorrect2;
          this.imgs = [];
          this.imgs.push({
            imgPath: imgURL + correct.poster_path,
            title: correct.title,
          });
          this.imgs.push({
            imgPath: imgURL + uncorrect1.poster_path,
            title: uncorrect1.title,
          });
          this.imgs.push({
            imgPath: imgURL + uncorrect2.poster_path,
            title: uncorrect2.title,
          });
          this.imgs = _.shuffle(this.imgs);
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
};
</script>

<style></style>
