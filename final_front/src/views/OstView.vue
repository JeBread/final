<template>
    <div>
        <!-- Number of fields: <input type="text"  v-model="numFields" /> -->
        <div id="lp">
            <div class="center"></div>
            <div class="crosshair-x"></div>
            <div class="crosshair-y"></div>
        </div>
    </div>
  </template>
  
  <script>
  const API_URL = "http://127.0.0.1:8000";
  import axios from 'axios'
export default {
  name: "OstView",
  data() {
    return {
      numFields: 6,
      movies:[],
    };
  },
  watch: {
    numFields() {
      this.createFields();
      this.distributeFields();
    },
  },
  created(){
    this.getMovies()
  },
  mounted() {
    this.createFields();
    this.distributeFields();

    const container = document.getElementById("lp");
    const lp = container;

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

    container.addEventListener("mouseleave", () => {
      mouseDown = false;
      document.removeEventListener("mousemove", mouse);
    });

    function mouse(evt) {
      if (mouseDown) {
        const center_x = offset.left + lp.offsetWidth / 2;
        const center_y = offset.top + lp.offsetHeight / 2;
        const mouse_x = evt.pageX;
        const mouse_y = evt.pageY;
        const radians = Math.atan2(mouse_x - center_x, mouse_y - center_y);
        const degree = radians * (180 / Math.PI) * -1 + 90;

        lp.style.transform = `rotate(${degree}deg)`;
      }
    }

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

      for (var i = 0; i < parseInt(this.numFields); i++) {
        var poster = document.createElement("div");
        poster.className = "poster";
        poster.innerText = i + 1;
        container.appendChild(poster);
      }
    },
    distributeFields() {
      var radius = 200;
      var posters = document.getElementsByClassName("poster");
      var container = document.getElementById("lp");
      var width = container.offsetWidth;
      var height = container.offsetHeight;
      var angle = 0;
      var step = (2 * Math.PI) / posters.length;

      for (var i = 0; i < posters.length; i++) {
        var x =
          Math.round(width / 2 + radius * Math.cos(angle) - posters[i].offsetWidth / 2);
        var y =
          Math.round(height / 2 + radius * Math.sin(angle) - posters[i].offsetHeight / 2);

        posters[i].style.left = x + "px";
        posters[i].style.top = y + "px";

        angle += step;
      }
    },
    getMovies(){
        axios({
        method: "get",
        url: `${API_URL}/movies/ost/`,
      })
        .then((res) => {
            for(const movie of res.data){
                console.log(movie)
                this.movies.push(movie)
            }

        })
        .catch((err) => {
          console.log(err);
        });
    }
  },
};
</script>

<style>
#lp {
  width: 600px;
  height: 600px;
  border: 1px solid #000;
  position: relative;
  margin: 0 auto; /* 가운데 정렬 */
  border-radius: 50%; /* 둥글게 만들기 */
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
  width: 20px;
  height: 20px;
  position: absolute;
  background: #f00;
}
.crosshair-x {
  width: 600px;
  height: 1px;
  background: #000;
  position: absolute;
  left: 0;
  top: 300px;
}
.crosshair-y {
  width: 1px;
  height: 600px;
  background: #000;
  position: absolute;
  left: 300px;
  top: 0;
}
</style>
  