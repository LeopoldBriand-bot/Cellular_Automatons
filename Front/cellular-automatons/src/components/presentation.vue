<template>
    <div class="presentation">
        <leftSideNavBar></leftSideNavBar>
        <p>Presentation</p>
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
.presentation {
  flex-direction: row;
  display: flex;
}
</style>
