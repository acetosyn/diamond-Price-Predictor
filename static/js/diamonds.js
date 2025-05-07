document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('form');
    const loader = document.getElementById('loader');
    const result = document.getElementById('result');
  
    form.addEventListener('submit', async function (e) {
      e.preventDefault();
  
      loader.style.display = 'block';
      result.textContent = '';
  
      const carat = parseFloat(document.getElementById('carat').value);
      const cut = document.getElementById('cut').value;
      const color = document.getElementById('color').value;
      const clarity = document.getElementById('clarity').value;
  
      try {
        const response = await fetch('/predict', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({ carat, cut, color, clarity })
        });
  
        if (!response.ok) {
          throw new Error('Prediction failed.');
        }
  
        const data = await response.json();
        loader.style.display = 'none';
        result.innerHTML = `<h2>💰 Predicted Price: <span style="color:#2ecc71;">${data.price}</span></h2>`;
      } catch (error) {
        loader.style.display = 'none';
        result.innerHTML = `<span style="color: red;">❌ Error: ${error.message}</span>`;
      }
    });
  });
  