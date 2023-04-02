<template>
    <div>
        <h2>Placeholder for working with payments</h2>
    </div>
</template>
<script>
    export default{
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
        data() {
            return {
                BID: Number(this.$route.params.BID),
                Price: Number(this.$route.params.Price),          

            }; 
        },     
    }
</script>