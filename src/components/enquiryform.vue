<template>
  <div class="container bg-light mt-4 mb-4 p-2">
    <form action="action_page.php">

      <label class="form-label mt-4" for="fname">First Name</label>
      <input class="form-control" type="text" id="fname" name="firstname" placeholder="Your name..">

      <label class="form-label mt-4" for="lname">Last Name</label>
      <input class="form-control" type="text" id="lname" name="lastname" placeholder="Your last name..">

      <label class="form-label mt-4" for="country">Country</label>
      <select class="form-select" id="country" name="country">
        <option value="australia">Singapore</option>
        <option value="canada">Others</option>
      </select>

      <label class="form-label mt-4" for="subject">Subject</label>
      <textarea class="form-control" id="subject" name="subject" placeholder="Write something.." style="height:200px"></textarea>

      <input class="btn btn-primary mt-4 mb-4" type="submit" value="Submit">

    </form>
  </div>
</template>

<script>
export default {
  name: "enquiryform",
};
</script>
