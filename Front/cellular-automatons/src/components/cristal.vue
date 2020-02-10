<template>
    <div class="cristal">
        <leftSideNavBar></leftSideNavBar>
        <p>Cristal</p>
    </div>
</template>
<script>
import leftSideNavBar from "./leftSideNavBar.vue";
export default {
  components: {
    leftSideNavBar
  },
}
</script>

<style scoped>
.cristal {
  flex-direction: row;
  display: flex;
}
</style>