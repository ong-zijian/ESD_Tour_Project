<template>
<div class="container bg-light mt-4 mb-4 p-2">
    <form action="action_page.php">

      <label class="form-label mt-4" for="fname">First Name</label>
      <input class="form-control" type="text" id="fname" name="firstname" placeholder="Your name..">

      <label class="form-label mt-4" for="lname">Last Name</label>
      <input class="form-control" type="text" id="lname" name="lastname" placeholder="Your last name..">

      <label class="form-label mt-4" for="country">Country</label>
      <select class="form-select" id="country" name="country">
        <option value="Singapore">Singapore</option>
        <option value="canada">Others</option>
      </select><br>

     <button class="btn btn-primary mb-2" @click="retrieve" >Retrieve</button>


      <label class="form-label" for="subject"> I hereby consent that I will be punctual in the assembly of tour on and be kind to the tour guides.</label>
      <input type="checkbox" id="vehicle2" name="consent" value="I consent"><br>

      <input class="btn btn-warning mt-4 mb-4" type="submit" value="Submit">

    </form>
  </div>
</template>

<script>
    export default{
//         props: {
//             TID,
//             startDateTime
//   },
        props: [TID, 
                startDateTime],
                
        methods: {
            
            retrieve() {
                console.log(TID, startDateTime)
            }
        }
    }
</script>