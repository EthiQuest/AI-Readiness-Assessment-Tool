async function submitAssessment(responses) {
    const response = await fetch('/assessment', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(responses),
    });
    const scores = await response.json();
    displayScores(scores);
}

function displayScores(scores) {
    const ctx = document.getElementById('scoreChart').getContext('2d');
    new Chart(ctx, {
        type: 'radar',
        data: {
            labels: Object.keys(scores),
            datasets: [{
                label: 'AI Readiness Scores',
                data: Object.values(scores),
                fill: true,
                backgroundColor: 'rgba(255, 99, 132, 0.2)',
                borderColor: 'rgb(255, 99, 132)',
                pointBackgroundColor: 'rgb(255, 99, 132)',
                pointBorderColor: '#fff',
                pointHoverBackgroundColor: '#fff',
                pointHoverBorderColor: 'rgb(255, 99, 132)'
            }]
        },
        options: {
            elements: {
                line: {
                    borderWidth: 3
                }
            }
        }
    });
}
