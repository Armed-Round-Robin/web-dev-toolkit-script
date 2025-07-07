// Example JavaScript pseudocode for integrating a crypto payment API
async function initiateCryptoPayment(amount, cryptoType) {
    const response = await fetch('https://api.crypto-payments.com/create', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({amount: amount, currency: cryptoType})
    });
    const data = await response.json();
    // Redirect user to payment gateway
    window.location.href = data.payment_url;
}

// Usage
initiateCryptoPayment(100, 'BTC');
