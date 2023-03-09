<script setup>
import Navbar from "./components/Navbar.vue";
import Footer from "./components/footer.vue";
</script>
<template>
  <Navbar />
  <router-view />
  <Footer/>
</template>

<script>
  const url = "http://127.0.0.1:5000/test1"

  export default {
    data() {
      return{
        name1:""
      }
    },
    methods:{
      test1() {
        const response = 
        fetch(url)
        .then(response => response.json())
        .then(data => {
          console.log(response)
          console.log(data) 
          this.name1 = data        
        })
        .catch(error =>{
          alert(error)
        }); 
      }
        
    }

  }

</script>
<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
