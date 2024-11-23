document.getElementById('fetchData').addEventListener('click', () => {
    // Simulate fetching data
    const data = { message: 'Hello from Flask!' };
    document.getElementById('dataDisplay').innerText = data.message;
});
