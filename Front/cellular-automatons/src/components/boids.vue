<template>
  <div class="boids">
      <leftSideNavBar></leftSideNavBar>
      <environmentPlayground
      name="Boids"
      @play="playBoids"
      @forward="forwardBoids"
      @reset="resetBoids">
        <template #headerOptions>
          <b-button-group class="mx-1">
              <b-button @click="buttonAddBoidPress">Add Boid</b-button>
          </b-button-group>
        </template>
        <template #environment>
          <canvas id="boidCanvas"></canvas>
        </template>
      </environmentPlayground>
  </div>
</template>
<script>
import leftSideNavBar from "./leftSideNavBar.vue";
import environmentPlayground from "./environmentPlayground";
export default {
  components: {
    leftSideNavBar,
    environmentPlayground
  },
  data() {
    return {
      canvas: null,
      canvasContext: null,
    }
  },
  computed: {
    canvasSize: function () {
      return !this.canvas === null
      ? [this.canvasHeight, this.canvasWidth]
      : [null, null];
    },
    canvasHeight: function () {
      return !this.canvas === null
      ? this.canvas.clientHeight
      : 0;
    },
    canvasWidth: function () {
      return !this.canvas === null
      ? this.canvas.clientWidth
      : 0;
    },
  },
  watch: {
    canvasSize: function () {
      this.changingCanvasSize;
    }
  },
  mounted() {
    this.canvas = document.getElementById('boidCanvas');
    //this.canvasContext = this.canvas.getContext('2d');

  },
  methods: {
    buttonAddBoidPress() {
      //eslint-disable-next-line
      console.log("Add")
    },
    playBoids(play){
      if(play) {
        //eslint-disable-next-line
        console.log("play")
      }
      else {
        //eslint-disable-next-line
        console.log("pause")
      }
    },
    forwardBoids(){
      //eslint-disable-next-line
      console.log("forward")
      //eslint-disable-next-line
      console.log(this.canvasHeight, this.canvasWidth)
    },

    resetBoids(){
      //eslint-disable-next-line
      console.log("reset")
    },

    askForNextMove(){
      //eslint-disable-next-line
      console.log("nextMove")
    },

    changingCanvasSize(){
      //eslint-disable-next-line
      console.log("alert of canvas size changing")
      this.resetBoids;
    }

  }
}
</script>

<style scoped>
.boids {
  flex-direction: row;
  display: flex;
}
.boidCanvas {
  height : 100%;
  width : 100%;
}
</style>