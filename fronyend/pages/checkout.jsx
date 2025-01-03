import React from "react";

const Checkout = () => {
  return (
    <div className="checkout">
      <h1>Checkout</h1>
      <form>
        <label>Address:</label>
        <input type="text" placeholder="Enter your address" />
        <label>Payment Details:</label>
        <input type="text" placeholder="Enter payment details" />
        <button>Place Order</button>
      </form>
    </div>
  );
};


export default Checkout;
