<template>
  <div class="home">
    <hero/>
  </div>
</template>

<script>
// @ is an alias to /src
//import HelloWorld from "@/components/HelloWorld.vue";
import hero from "@/components/hero.vue";
import axios from "axios"; 
export default {
  name: "HomeView",
  components: {
    hero
  },
  // async created() {
  //   const response = await axios.get('user');
  //   console.log(response)
  // }
};
</script>
