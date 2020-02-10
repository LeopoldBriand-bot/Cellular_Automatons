<template>
  <div id="leftSideNavBar" class="shadow rounded overflow-auto h-100 mt-a mb-a">
    <b-nav vertical>
        <b-nav-item to="Presentation" :active='this.$store.state.page == 0' v-on:click='changePage(0)'>Présentation</b-nav-item>
        <b-nav-item to="Boids" :active='this.$store.state.page == 1' v-on:click='changePage(1)'>Boid</b-nav-item>
        <b-nav-item to="Cristal" :active='this.$store.state.page == 2' v-on:click='changePage(2)'>Cristal</b-nav-item>
    </b-nav>
  </div>
</template>

<script>
import {mapActions} from 'vuex'
export default {
    methods:{...mapActions(['changePage'])}
}
</script>
<style lang="scss" scoped>
.flex-column {
	-ms-flex-direction: column !important;
	-webkit-box-orient: vertical !important;
	-webkit-box-direction: normal !important;
	flex-direction: column !important;
	width: 100% !important;
}
#leftSideNavBar{
  max-width: 200px;
  height: 100vh !important;
  border: 5px;
  padding: 5px;
  top: 0;
  left: 0;
  display: flex !important;
  box-sizing: border-box !important;
  width: 100% !important;
  background: #433f5e;
}
a{
  text-align: center;
  display: block;
  background-color: #00a79d;
  border-radius: 5px;
  margin: 5px;
  color: white;
}
a:hover{
  background-color: #433f5e3f;
  color: white;
}
a:active{
  background-color: #ec008c;
}
</style>