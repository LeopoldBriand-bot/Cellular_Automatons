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
              <b-button>Add Boid</b-button>
          </b-button-group>
        </template>
        <template #environment>
          <canvas id="boidCanvas" width="500" height="500"></canvas>
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
  created() {
    this.canvas = document.getElementById('boidCanvas');
    this.canvasContext = this.canvas.getContext('2d');
  },
  method: {
    playBoids(play){
      if(play) {
        //eslint-disable-next-line
        console.log("play")
      }
    },
    forwardBoids(){
      //eslint-disable-next-line
      console.log("forward")
    },

    resetBoids(){
      //eslint-disable-next-line
      console.log("reset")
    },

    askForNextMove(){
      //eslint-disable-next-line
      console.log("nextMove")
    },

  }
}
</script>

<style scoped>
.boids {
  flex-direction: row;
  display: flex;
}
</style>