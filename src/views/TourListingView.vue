<template>
  <div id="main-container" class="container mb-4">
    <h1 class="display-4">Tour Listing</h1>
    <a id="filterBtn" class="btn btn-success">Filter</a>
    <p> {{ getAllListing }}</p>
    <table class='table table-striped border-1'>
        <thead class='table-dark'>
            <tr>
                <th>TID</th>
                <th>Title 13</th>
                <th>Description</th>
                <th>Postcode</th>
            </tr>
        </thead>
      <tbody id="toursTable">
        <tr v-for="tour in tours">
          <td>{{ tour.Tour_ID }}</td>
          <td>{{ tour.Title }}</td>
          <td>{{ tour.Description }}</td>
          <td>{{ tour.Postcode }}</td>
        </tr>
      </tbody>
    </table>
    <a id="addBookBtn" class="btn btn-primary" href="add-book.html">Add a book</a>
  </div>
</template>

<script>
  const url = "http://127.0.0.1:5002/tour"
  export default{
    name: "TourListingView",
    data() {
      return {
        "tours": []
      }
    },
    computed:{
      getAllListing(){
        const response = 
        fetch(url)
        .then(response => response.json())
        .then(data => {
          console.log(response)
          console.log(data.data.tour)
          this.tours = data.data.tour      
        })
        .catch(error =>{
          alert(error)
        });
      } 
    }
  }
</script>
