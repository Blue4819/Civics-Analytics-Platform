// src/components/NationalDisasters.js
import React, { useEffect } from 'react';
import Chart from 'chart.js/auto';
import NavBar from '../navbar.js'


const NationalDisasters = () => {
    useEffect(() => {
        const ctx = document.getElementById('disasterChart').getContext('2d');

        fetch('/get-data/national_disasters', {
            method: 'POST'
        })
        .then(response => response.json())
        .then(data => {
            const labels = Object.keys(data);
            const counts = Object.values(data);

            new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: labels,
                    datasets: [{
                        label: 'Number of Disasters',
                        data: counts,
                        backgroundColor: 'rgba(75, 192, 192, 0.6)',
                        borderColor: 'rgba(75, 192, 192, 1)',
                        borderWidth: 1
                    }]
                },
                options: {
                    responsive: true,
                    scales: {
                        y: {
                            beginAtZero: true,
                            title: {
                                display: true,
                                text: 'Number of Disasters'
                            }
                        },
                        x: {
                            title: {
                                display: true,
                                text: 'Years'
                            }
                        }
                    }
                }
            });
        })
        .catch(error => console.error('Error fetching data:', error));
    }, []);

    return (
        <div className="card-container">
            <NavBar/>
            <div className="card">
                <h3>Disaster Statistics</h3>
                <canvas id="disasterChart" width="400" height="200"></canvas>
            </div>
        </div>
    );
};

export default NationalDisasters;