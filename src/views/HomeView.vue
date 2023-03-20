<template>
  <div class="home">
    <hero/>
    <homeCard/>
  </div>
</template>

<script>
// @ is an alias to /src
//import HelloWorld from "@/components/HelloWorld.vue";
import hero from "@/components/hero.vue";
import homeCard from "@/components/homeCard.vue";
import axios from "axios"; 
export default {
  name: "HomeView",
  components: {
    hero,
    homeCard
  },
  // async created() {
  //   const response = await axios.get('user');
  //   console.log(response)
  // }
};
</script>
