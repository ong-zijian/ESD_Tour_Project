<template>
  <div id="main-container" class="container mb-4">
    <h1 class="display-4">All Available Tours</h1>
    <!-- <a id="filterBtn" class="btn btn-success">Filter</a> -->
    <p> {{ getAllListing }}</p>
    <div class="table-responsive">
      <table class='table table-striped border-1 w'>
          <thead class='table-dark'>
              <tr>
                  <th>TID</th>
                  <th>Tour Name</th>
                  <th>Description</th>
                  <th>Guide</th>
                  <th>Postcode</th>
                  <th>Price (S$)</th>
                  <th>Time Slots</th>
                  
              </tr>
          </thead>
        <tbody id="toursTable">
          <tr v-for="tour in tours">
            <td>{{ tour.Tour_ID }}</td>
            <td>{{ tour.Title }}</td>
            <td>{{ tour.Description }}</td>
            <td>{{ tour.Guide }}</td>
            <td>{{ tour.Postcode }}</td>
            <td>{{ tour.Price }}</td>
            <td> <button class="btn btn-primary mb-2 " v-for="(value, key) in tour.details" :key="key" @click="onBook(tour.Tour_ID, value.startDateTime, tour.Price)">{{ value.startDateTime }}</button> </td>
          </tr>
        </tbody>
      </table>
    </div>
    <!-- <a id="addBookBtn" class="btn btn-primary" href="add-book.html">Add a book</a> -->
  </div>
</template>

<script>
import { start } from '@popperjs/core';

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
    },
    methods: {
      onBook(TID, startDateTime, Price) {
        console.log(TID, startDateTime, Price)
        this.$router.push({ name: 'orderForm', params: { TID, startDateTime, Price } })
      }
    }
  }
</script>
