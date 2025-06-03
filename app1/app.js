const axios = require('axios');

setInterval(async () => {
  try {
    const res = await axios.get('http://172.18.0.3:5000/');
    console.log("Resposta do app2:", res.data);
  } catch (err) {
    console.error("Erro ao conectar com app2:", err.message);
  }
}, 5000);