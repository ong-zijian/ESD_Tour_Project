<template>
<div class="container bg-light mt-4 mb-4 p-2">
    <form>

      <label class="form-label mt-4" for="name">Name</label>
      <input class="form-control" type="text" id="name" name="name" placeholder="Your name.." v-model="Name">

      <label class="form-label mt-4" for="email">Email</label>
      <input class="form-control" type="text" id="email" name="email" placeholder="Your email address.." v-model="Email">

      <label class="form-label mt-4" for="country">Country</label>
      <select class="form-select" id="country" name="country" v-model="Country">
        <option value="Singapore">Singapore</option>
        <option value="canada">Others</option>
      </select><br>
      <div>

      </div>
      <label class="form-label" for="subject"> I hereby consent that I will be punctual in the assembly of tour on and be kind to the tour guides.</label><br/>
      <input type="checkbox" id="vehicle2" name="consent" value="I consent" class="ml-2"><br>

      <input class="btn btn-warning mt-4 mb-4" type="submit" value="Submit" @click="placeBooking">

    </form>
  </div>
</template>

<script>
  //import axios from 'axios'
  import moment from 'moment';

  const place_booking_url = "http://127.0.0.1:5101/place_booking";
  let increment_tour_url = "http://127.0.0.1:5002/tour";

  export default{
    props: {
      TID: {
        type: Number,
        required: true
      },
      startDateTime: {
        type: String,
        required: true
      },
      Price: {
        type: Number,
        required: true
      }
    },
    data() {
      return {
        TID: Number(this.$route.params.TID),
        Price: Number(this.$route.params.Price),
        startDateTime: this.$route.params.startDateTime,
        Name: this.Name,
        Email: this.Email,
        Country: this.Country,
        bookingSuccessful: false,

      }; 
    },       
    methods: {
      // removes the " GMT" at the end of startDateTime for passing into the place_booking method
      cleanGMT() {
        const format = "ddd, DD MMM YYYY HH:mm:ss";
        const datetime = moment.utc(this.startDateTime, format).format("YYYY-MM-DDTHH:mm:ss");
        this.startDateTime = datetime;
      },
      //process the place_booking
      placeBooking(event){
        event.preventDefault();
        fetch(place_booking_url,
        {
          method: "POST",
          headers: {
              "Content-type": "application/json"
          },
          body: JSON.stringify(
            {
                "startDateTime": this.startDateTime,
                "TID": this.TID,
                "cName": this.Name,
                "Email": this.Email,
                "Price": this.Price
            })
        })
        .then(response => response.json())
        .then(data => {
            console.log(data);
            let result = data.data;
            let orderMessage;
            console.log(result.order_result.data.Price);
            // 3 cases
            switch (data.code) {
              case 201:
                // 201
                this.bookingSuccessful = true;
                const BID = result.order_result.data.booking_id;
                const Price = result.order_result.data.Price;
                console.log(this.bookingSuccessful)
                orderMessage = `Response code:${result.order_result.code}`;
                this.increment()
                //send to next page
                this.$router.push({ name: 'paymentPlaceholder' , params: { BID, Price } })
                break;

              case 400:
                  // 400 
                this.bookingSuccessful = true;
                orderMessage =`Code: ${result.order_result.code}, Error handling: ${data.message}`;
                alert("Please enter the valid field")
                break;
            case 500:
                // 500 
                orderMessage = `Code: ${result.order_result.code}:${result.order_result.message};
                                Error handling: ${data.message}`;
                alert("Please try again")
                break;

            default:
                orderMessage = `Unexpected error: ${data.code}`;
                console.log(`Unknown error code : ${data.code}`);
                alert("Please try again")
                break;

              } // switch
              console.log(orderMessage);
              this.orderPlaced = true;
          })
          .catch(error => {
              console.log("Problem in placing an order. " + error);
              alert("Please key in the fields and try again")
          })

      },
      increment(){
        //insert put to increment_tour_url
        console.log("incrementing")
        increment_tour_url = increment_tour_url + "/"+ this.TID +  "/" + this.startDateTime
        fetch(increment_tour_url, {
          method: "PUT",
          headers: {
            "Content-type": "application/json"
          },
        })
        .then(response => response.json())
        .then(data => {
          console.log("Tour increment success:", data);
        })
        .catch(error => {
          console.error("Problem incrementing tour count:", error);
        });
        // end of insert
      }
    },
     
    // to be deleted if no need to debug
    mounted() {
      console.log('TID:', this.TID) // should output the TID parameter
      this.cleanGMT()
      console.log('startDateTime:', this.startDateTime) // should output the startDateTime parameter
    }
  }
</script>