<template>
  <div id="lp-con">
    <!-- Number of fields: <input type="text"  v-model="numFields" /> -->
    <div id="lp"></div>

    <img :src="center_img" id="musicpointer" :class="{ rotating: isPlaying }" />
    <button>
      <svg
        xmlns="http://www.w3.org/2000/svg"
        fill="none"
        viewBox="0 0 24 24"
        stroke-width="1.5"
        stroke="white"
        class="w-14 h-14 ost-view-playbtn"
        v-if="!isPlaying"
        @click="playOrPause"
      >
        <path
          stroke-linecap="round"
          stroke-linejoin="round"
          d="M5.25 5.653c0-.856.917-1.398 1.667-.986l11.54 6.348a1.125 1.125 0 010 1.971l-11.54 6.347a1.125 1.125 0 01-1.667-.985V5.653z"
        />
      </svg>
    </button>

    <button>
      <svg
        xmlns="http://www.w3.org/2000/svg"
        fill="none"
        viewBox="0 0 24 24"
        stroke-width="1.5"
        stroke="white"
        class="w-14 h-14 ost-view-playbtn"
        v-if="isPlaying"
        @click="playOrPause"
      >
        <path
          stroke-linecap="round"
          stroke-linejoin="round"
          d="M15.75 5.25v13.5m-7.5-13.5v13.5"
        />
      </svg>
    </button>

    <div class="crosshair-y" style="opacity: 0"></div>
    <OstViewPlayer :video-id="videoId" ref="ostplayer" />
  </div>
</template>

<script>
import axios from "axios";
import OstViewPlayer from "@/components/OstViewPlayer.vue";

const API_URL = "http://127.0.0.1:8000";
const imgURL = "https://image.tmdb.org/t/p/original";
/* eslint-disable */
export default {
  name: "OstView",
  components: { OstViewPlayer },
  data() {
    return {
      numFields: 6,
      movies: [],
      center_img: null,
      center_idx: 0,
      videoId: null,
      isPlaying: false,
      
    };
  },
  computed: {
    
  },
  watch: {
    // numFields() {
    //   this.createFields();
    //   this.distributeFields();
    // },
  },
  created() {
    this.getMovies();
  },
  mounted() {
    // const lp_container = document.getElementById("lp-con");
    const container = document.getElementById("lp");
    const lp = container;
    const crosshair = document.querySelector(".crosshair-y");

    let offset = { left: 0, top: 0 };
    let mouseDown = false;

    container.addEventListener("mousedown", () => {
      mouseDown = true;
      document.addEventListener("mousemove", mouse);
    });

    container.addEventListener("mouseup", () => {
      mouseDown = false;
      document.removeEventListener("mousemove", mouse);
    });

    const mouse = (evt) => {
      if (mouseDown) {
        const center_x = offset.left + lp.offsetWidth / 2;
        const center_y = offset.top + lp.offsetHeight / 2;
        const mouse_x = evt.pageX;
        const mouse_y = evt.pageY;
        const radians = Math.atan2(mouse_x - center_x, mouse_y - center_y);
        const degree = radians * (180 / Math.PI) * -1 + 90;

        lp.style.transform = `rotate(${degree}deg)`;

        const imgTags = container.querySelectorAll("#lp img");
        const crosshairRect = crosshair.getBoundingClientRect();

        let closestImg = null;
        let closestTopDiff = Infinity;

        imgTags.forEach((img) => {
          const imgRect = img.getBoundingClientRect();

          const topDiff = Math.abs(crosshairRect.top - imgRect.top);

          if (topDiff <= crosshairRect.height / 2 && topDiff < closestTopDiff) {
            closestImg = img;
            closestTopDiff = topDiff;
          }
        });

        if (closestImg) {
          const altValue = closestImg.getAttribute("alt");
          // console.log(altValue);
          this.center_idx = altValue;
          this.center_img = imgURL + this.movies[this.center_idx].poster_path;
          this.videoId = this.movies[this.center_idx].ost;
        }
      }
    };

    this.$nextTick(() => {
      offset = {
        left: lp.offsetLeft,
        top: lp.offsetTop,
      };
    });
  },
  methods: {
    createFields() {
      var container = document.getElementById("lp");
      container.innerHTML = ""; // Clear previous fields
      container.style.webkitUserDrag = "none";
      container.setAttribute("class", container.className + " noselect");

      for (var i = 0; i < parseInt(this.numFields); i++) {
        var poster = document.createElement("img");
        poster.setAttribute("class", "poster noselect");
        poster.setAttribute(
          "src",
          imgURL + this.movies[i % this.movies.length].poster_path
        );
        poster.setAttribute("alt", i);
        container.appendChild(poster);
      }
    },

    distributeFields() {
      var radius = 200;
      var posters = document.getElementsByClassName("poster");
      var container = document.getElementById("lp");
      var width = container.offsetWidth;
      var height = container.offsetHeight;
      var angle = Math.PI / -2; // 12시 방향으로 시작하도록 수정
      var step = (2 * Math.PI) / posters.length;

      for (let i = 0; i < posters.length; i++) {
        var x = Math.round(
          width / 2 + radius * Math.cos(angle) - posters[i].offsetWidth / 2
        );
        var y = Math.round(
          height / 2 + radius * Math.sin(angle) - posters[i].offsetHeight / 2
        );

        posters[i].style.left = x + "px";
        posters[i].style.top = y + "px";
        posters[i].style.webkitUserDrag = "none";

        var rotationAngle = angle * (180 / Math.PI) + 90;
        posters[i].style.transform = `rotate(${rotationAngle}deg)`;

        angle += step;
      }
    },

    getMovies() {
      axios({
        method: "get",
        url: `${API_URL}/movies/ost/`,
      })
        .then((res) => {
          this.movies = res.data;
          this.createFields();
          this.distributeFields();
          this.center_img = imgURL + this.movies[0].poster_path;
          this.videoId = this.movies[0].ost;
        })
        .catch((err) => {
          console.log(err);
        });
    },

    playerPlay() {
      this.$refs.ostplayer.playVideo();
    },

    playerPause() {
      this.$refs.ostplayer.pauseVideo();
    },

    playOrPause() {
      if (this.isPlaying) {
        this.isPlaying = false;
        this.playerPause();
      } else {
        this.isPlaying = true;
        this.playerPlay();
      }
      
    },
  },
};
</script>

<style>
#lp-con {
  position: relative;
}

.crosshair-y {
  width: 1px;
  height: 300px;
  background: #000;
  position: absolute;
  left: 50%;
  top: 0;
  transform: translateX(-50%);
}

#lp {
  width: 550px;
  height: 550px;
  /* border: 1px solid #000; */
  position: relative;
  margin: 0 auto; /* 가운데 정렬 */
  border-radius: 50%; /* 둥글게 만들기 */
  transform: rotate(0deg);
}
.center {
  width: 10px;
  height: 10px;
  position: absolute;
  left: 295px;
  top: 295px;
  background: #000;
}
.poster {
  width: 130px;
  height: 180px;
  position: absolute;
  background: #f00;
  border-radius: 15px;
}

.noselect {
  -webkit-touch-callout: none;
  -webkit-user-select: none;
  -khtml-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

#musicpointer {
  width: 130px;
  height: 130px;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  border-radius: 50%;
  border: 5px solid transparent;
}

.ost-view-playbtn {
  width: 50px;
  height: 50px;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

.rotating {
  animation: rotate 5s linear infinite;
}

@keyframes rotate {
  from {
    transform: translate(-50%, -50%) rotate(0deg);
  }
  to {
    transform: translate(-50%, -50%) rotate(360deg);
  }
}
</style>
