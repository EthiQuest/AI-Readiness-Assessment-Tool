document.addEventListener('DOMContentLoaded', function() {
    // In a real application, you would fetch this data from your server
    const sampleData = {
        overallScore: 6.5,
        dimensionScores: {
            Leadership: 7,
            Data: 6,
            Technology: 8,
            People: 5,
            Process: 7,
            Governance: 6
        }
    };

    displayReport(sampleData);
});

function displayReport(data) {
    document.getElementById('overall-score').textContent = data.overallScore.toFixed(2);
    document.getElementById('score-interpretation').textContent = getScoreInterpretation(data.overallScore);

    const ctx = document.getElementById('radar-chart').getContext('2d');
    new Chart(ctx, {
        type: 'radar',
        data: {
            labels: Object.keys(data.dimensionScores),
            datasets: [{
                label: 'AI Readiness Scores',
                data: Object.values(data.dimensionScores),
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
            },
            scales: {
                r: {
                    angleLines: {
                        display: false
                    },
                    suggestedMin: 0,
                    suggestedMax: 10
                }
            }
        }
    });

    displayStrengthsWeaknesses(data.dimensionScores);
    displayRecommendations(data.dimensionScores);
}

function getScoreInterpretation(score) {
    if (score < 3) return "Your organization is in the early stages of AI readiness.";
    if (score < 6) return "Your organization has made some progress towards AI readiness, but there's room for improvement.";
    if (score < 8) return "Your organization is well on its way to AI readiness, with some areas still needing attention.";
    return "Your organization demonstrates strong AI readiness across most dimensions.";
}

function displayStrengthsWeaknesses(scores) {
    const sortedDimensions = Object.entries(scores).sort((a, b) => b[1] - a[1]);
    const strengths = sortedDimensions.slice(0, 2);
    const weaknesses = sortedDimensions.slice(-2).reverse();

    const strengthsHtml = strengths.map(([dimension, score]) => 
        `<p><strong>${dimension}:</strong> Score of ${score}/10. This is a key strength in your AI readiness.</p>`
    ).join('');

    const weaknessesHtml = weaknesses.map(([dimension, score]) => 
        `<p><strong>${dimension}:</strong> Score of ${score}/10. This area needs improvement to enhance your AI readiness.</p>`
    ).join('');

    document.getElementById('strengths').innerHTML = `<h3>Top Strengths</h3>${strengthsHtml}`;
    document.getElementById('weaknesses').innerHTML = `<h3>Areas for Improvement</h3>${weaknessesHtml}`;
}

function displayRecommendations(scores) {
    const recommendations = [
        "Invest in AI education and training programs for your team.",
        "Develop a clear AI strategy aligned with your business goals.",
        "Improve data quality and accessibility across your organization.",
        "Establish robust AI governance and ethics policies.",
        "Enhance your IT infrastructure to support AI initiatives."
    ];

    const recommendationHtml = recommendations.map(rec => `<li>${rec}</li>`).join('');
    document.getElementById('recommendation-list').innerHTML = recommendationHtml;
}

document.getElementById('upgrade-button').addEventListener('click', function() {
    alert('Upgrading to premium... In a full implementation, this would process payment and generate the premium report.');
});