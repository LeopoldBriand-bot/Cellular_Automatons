<template>
  <div>
    <b-card>
      <template v-slot:header>
        <p id="name">{{ name }}</p>
        <b-button-toolbar id="default-toolbar" key-nav aria-label="Toolbar with button groups">
          <b-button-group class="mx-1">
            <b-button @click="buttonPlayPress">
                <b-icon :icon="playIconState"></b-icon>
            </b-button>
            <b-button @click="buttonForwardPress">
                <b-icon icon="forward"></b-icon>
            </b-button>
          </b-button-group>
          <b-button-group class="mx-1">
              <b-button @click="buttonResetPress">Reset</b-button>
          </b-button-group>
        </b-button-toolbar>
        <slot name="headerOptions"></slot>
      </template>
      <slot name="environment"></slot>
    </b-card>
  </div>
</template>

<script>
export default {
  props:{
    name : String
  },
  data() {
    return{
      state: "paused",
      playIconState: "play"
    }
  },
  methods: {
    buttonPlayPress() {
      if(this.state==='paused') {
        this.state='played';
        this.$emit('play', true);
        this.playIconState = "pause"
      }
      else if(this.state==='played'){
        this.state = 'paused';
        this.$emit('play', false);
        this.playIconState = "play"
      }
    },

    buttonForwardPress() {
      if(this.state==='paused') {
        this.$emit('forward');
      }
    },

    buttonResetPress() {
      this.$emit('reset');
    }
  }
}
</script>
