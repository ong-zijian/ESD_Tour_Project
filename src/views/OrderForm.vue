<template>
<div class="container bg-light mt-4 mb-4 p-2">
    <form action="action_page.php" >

      <label class="form-label mt-4" for="name">Name</label>
      <input class="form-control" type="text" id="name" name="name" placeholder="Your name.." v-model="Name">

      <label class="form-label mt-4" for="email">Email</label>
      <input class="form-control" type="text" id="email" name="email" placeholder="Your email address.." v-model="Email">

      <label class="form-label mt-4" for="country">Country</label>
      <select class="form-select" id="country" name="country" v-model="Country">
        <option value="Singapore">Singapore</option>
        <option value="canada">Others</option>
      </select><br>
      <!-- Remove if done troubleshooting
      <p>Info: {{ TID }}, {{ startDateTime }},</p>

      <button @click="test">test</button>

      -->
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

  const place_booking_url = "http://127.0.0.1:5101/place_booking"
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
      placeBooking(){
        // const booking_data = {
        //   "TID": this.TID,
        //   "startDateTime": this.startDateTime,
        //   "cName": this.Name,
        //   'Postcode': this.Postcode 
        // };
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
            result = data.data;
            console.log(result);
            // 3 cases
            switch (data.code) {
              case 201:
                // 201
                this.bookingSuccessful = true;
                const bid = result.order_result.data.booking_id;
                const price = result.order_result.data.price;
                //bookingMessage =`booking placed. booking Result: ${result.order_result.code}:${result.order_result.data.booking_id}`;
                this.$router.push({ name: 'paymentPlaceholder' })
                break;

              case 400:
                  // 400 
                this.bookingSuccessful = true;
                bookingMessage =
                    `booking placed
                    booking Result:
                    ${result.booking_result.code}:${result.booking_result.data.status};

                      Error handling:
                      ${data.message}`;
                break;
            case 500:
                // 500 
                bookingMessage =
                    `booking placed with error:
                    booking Result:
                    ${result.booking_result.code}:${result.booking_result.message}

                    Error handling:
                    ${data.message}`;
                break;
            default:
                bookingMessage = `Unexpected error: ${data.code}`;
                console.log(`Unknown error code : ${data.code}`);
                break;

              } // switch
              console.log(orderMessage);
              this.orderPlaced = true;
          })
          .catch(error => {
              console.log("Problem in placing an order. " + error);
          })
        

        // axios.post(booking_url, booking_data)
        //   .then(response => {
        //     // handle successful response
        //     console.log(response);
        //   })
        //   .catch(error => {
        //     // handle error
        //     console.log(error);
        //   });


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