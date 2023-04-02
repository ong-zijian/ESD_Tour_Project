<template>
    <div class="container m-10 text-center">
        <h2>Hay Dairies Farm Tour</h2>
        <button class="btn btn-info" id="submit" name="submit" @click="redirectToCheckout">Purchase!</button>
    </div>
    <div class="container text-center m-10">
        <a v-bind:href="Tele_url" target="_blank">
            <h1> Click here to access our bot</h1> 
        </a>
        <p>Enter your booking ID to get a notification: {{ BID }}</p>
    </div>

</template>
<script>
    import axios from "axios";
import { toDisplayString } from "vue";

    export default {
        name: "MyComponent",
        props: {
            BID: {
                type: Number,
                required: true
            },
            Price: {
                type: Number,
                required: true
            }
        },
        methods: {
            redirectToCheckout() {
                window.location.href = 'http://127.0.0.1:5200';
            }
        },
        data() {
            return{
                BID: Number(this.$route.params.BID),
                Tele_url: "https://t.me/ESD_Tours_bot"
            }
            
        },
        created() {
            console.log(this.$route);
        }

    };
</script>
