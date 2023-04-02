<template>
    <div class="container m-10 text-center">
        <h2>Hay Dairies Farm Tour</h2>
        <button class="btn btn-info" id="submit" name="submit" @click="redirectToCheckout">Purchase!</button>
    </div>

</template>
<script>
    import axios from "axios";

    export default {
    name: "MyComponent",
        methods: {
            redirectToCheckout() {
                window.location.href = 'http://127.0.0.1:5200';
        }
    }
    };
</script>
