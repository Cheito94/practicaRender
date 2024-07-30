const ctx = document.getElementById('myChart').getContext('2d'); //Obtiene el contexto del canvas donde se dibujará el gráfico.
const myChart = new Chart(ctx, { //Instancia de Chart.js
    type: 'bar', //Tipo de gráfico(linbar, line, radar, polarArea, pie, doughnut, bubble
    data: {
        labels: ['Alaquez', 'Belisario Quevedo', 'Guaytacama', 'Mulaló', 'Eloy Alfaro', 'Poaló', 'Tanicuchí'],
        datasets: [{
            label: '# de votos',
            data: [4895, 5581, 7475, 7360, 6970, 5283, 11009 ],//Escala de datos que se mostrarán en el gráfico
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)',
                'rgba(255, 115, 25, 0.2)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)',
                'rgba(255, 115, 25, 1)'
            ],
            borderWidth: 3
        }]
    },
    options: {//Configura las opciones del gráfico, como el inicio del eje y en cero.
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});
