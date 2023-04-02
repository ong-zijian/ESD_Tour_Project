<template>
    <div class="container text-center m-10">
        <a v-bind:href="Tele_url" target="_blank">
        <h1>Click here to access our bot</h1>
        </a>
        <p>{{ Tele_url }}</p>
    </div>
</template>
<script>
    export default {
        props:{
            BID: {
                type: Number,
                required: true
            },
        },

        data(){
            return{
                BID: Number(this.$route.params.BID),
                Tele_url: "https://t.me/ESD_Tours_bot"
            }
        }
    }
</script>