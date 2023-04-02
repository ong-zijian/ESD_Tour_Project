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
            <td> <button class="btn btn-primary mb-2 " v-for="(value, key) in tour.details" 
              :key="key" @click="onBook(tour.Tour_ID, value.startDateTime, tour.Price)" 
              :disabled="value.disabled"
              :id="'bookBtn-' + tour.Tour_ID + '-' + cleanGMT(value.startDateTime)">{{ value.startDateTime }}</button> </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import { start } from '@popperjs/core';
import moment from 'moment';

  const get_tour_url = "http://localhost:8000/api/v1/tour";
  export default{
    name: "TourListingView",
    data() {
      return {
        "tours": []
      }
    },
    computed:{
      getAllListing() {
        fetch(get_tour_url)
          .then(response => response.json())
          .then(data => {
            this.tours = data.data.tour;
            this.tours.forEach(tour => {
              tour.details.forEach(detail => {
                const startDateTime = this.cleanGMT(detail.startDateTime);
                this.isSlotAvailable(tour.Tour_ID, startDateTime)
                  .then(isAvailable => {
                    detail.disabled = !isAvailable;
                  })
                  .catch(error => {
                    alert(error);
                  });
              });
            });
          })
          .catch(error => {
            alert(error);
          });
      }
    },
    methods: {
      cleanGMT(startDateTime) {
        const format = "ddd, DD MMM YYYY HH:mm:ss";
        const datetime = moment.utc(startDateTime, format).format("YYYY-MM-DDTHH:mm:ss");
        return datetime
      },
      onBook(TID, startDateTime, Price) {
        //console.log(TID, startDateTime, Price)
        this.$router.push({ name: 'orderForm', params: { TID, startDateTime, Price } })
      },
      isSlotAvailable(TID, startDateTime) {
        return fetch(`${get_tour_url}/${TID}/${startDateTime}`)
          .then(response => {
            if (response.status === 200) {
              return response.json().then(data => {
                return data.code === 200;
              });
            } else {
              throw new Error(`Failed to fetch availability: ${response.status}`);
            }
          });
      }
    }
  }
</script>
