<template>
  <div class="container">
    <h1>Quiz</h1>
    <!-- 모달창 -->
    <div class="jutify-center">
      <!-- 정답일때 모달창 -->
      <div class="black-bg" v-if="correctmodal == true">
        <div
          class="inline-block white-bg justify-center justify-items-center text-center"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
            stroke-width="1.5"
            stroke="currentColor"
            class="w-10 h-10"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              d="M9 12.75L11.25 15 15 9.75M21 12c0 1.268-.63 2.39-1.593 3.068a3.745 3.745 0 01-1.043 3.296 3.745 3.745 0 01-3.296 1.043A3.745 3.745 0 0112 21c-1.268 0-2.39-.63-3.068-1.593a3.746 3.746 0 01-3.296-1.043 3.745 3.745 0 01-1.043-3.296A3.745 3.745 0 013 12c0-1.268.63-2.39 1.593-3.068a3.745 3.745 0 011.043-3.296 3.746 3.746 0 013.296-1.043A3.746 3.746 0 0112 3c1.268 0 2.39.63 3.068 1.593a3.746 3.746 0 013.296 1.043 3.746 3.746 0 011.043 3.296A3.745 3.745 0 0121 12z"
            />
          </svg>
          <button class="text-xl" @click="correctmodal = false">Correct</button>
        </div>
      </div>
      <!-- 오답일때 모달창 -->
      <div class="black-bg" v-if="incorrectmodal == true">
        <div class="white-bg">
          <p class="text-xl">Fuck you</p>
          <button class="text-xl" @click="incorrectmodal = false">Retry</button>
        </div>
      </div>
    </div>
    <!-- 모달창 끝 -->
    <YoutubePlayer class="mt-5" :video-id="videoId" />
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
    <div
      class="mt-4"
      v-for="(img, idx) in imgs"
      :key="idx"
      style="display: inline-block"
    >
      <img
        :src="img.imgPath"
        height="180"
        width="180"
        style="margin: 30px"
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
      correctmodal: false,
      incorrectmodal: false,
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

        // alert("정답");
        this.correctmodal = true;
      } else {
        // alert("오답");
        this.incorrectmodal = true;
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

<style>
.black-bg {
  /* width: 50%; */
  width: 18%;
  height: 15%;
  background: rgba(0, 0, 0, 0.5);
  position: fixed;
  padding: 15px;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  border-radius: 20px;
}
.white-bg {
  width: 100%;
  height: 100%;
  background: rgba(255, 255, 255, 0.842);
  border-radius: 8px;
  padding: 20px;
}
/* .title {
  letter-spacing: 0px;
  background: linear-gradient(
    45deg,
    deepskyblue,
    deeppink,
    deepskyblue,
    deeppink
  );
  background-clip: text;
  -webkit-background-clip: text;
  color: transparent;
  font-size: 40px;
} */
</style>
