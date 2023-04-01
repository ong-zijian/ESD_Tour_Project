// getting Stripe publishable key and getting a new instance of Stripe.js
fetch("/config") 
.then((result) => {return result.json()})
.then((data)=>{
    const stripe = Stripe(data.publicKey);

    document.getElementById('submit').addEventListener("click",()=>{
        fetch("/checkout-session")
        .then((result) => {return result.json();})
        .then((session) => {
            console.log(session);
            //redirect to Stripe checkout
            console.log(session.sessionId);
            return stripe.redirectToCheckout({sessionId: session.sessionId})
        })
        .then((res) => {
            console.log(res);
        });
    })
});
