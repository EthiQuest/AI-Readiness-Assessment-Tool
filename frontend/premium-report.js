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
        },
        industryBenchmarks: {
            Leadership: 6.5,
            Data: 5.5,
            Technology: 7,
            People: 6,
            Process: 6.5,
            Governance: 5.5
        },
        recommendations: {
            Leadership: "Develop a comprehensive AI strategy and communicate it across the organization.",
            Data: "Implement a data governance framework to improve data quality and accessibility.",
            Technology: "Invest in cloud computing resources to support AI workloads.",
            People: "Launch an AI skills development program for employees across departments.",
            Process: "Create standardized processes for AI project management and deployment.",
            Governance: "Establish an AI ethics committee to oversee AI initiatives and ensure responsible use."
        },
        roi: {
            projected: "15-20%",
            timeframe: "18-24 months"
        },
        risks: [
            { name: "Data Privacy Breach", impact: "High", likelihood: "Medium" },
            { name: "AI Bias", impact: "High", likelihood: "Medium" },
            { name: "Skill Gap", impact: "Medium", likelihood: "High" },
            { name: "Technology Obsolescence", impact: "Medium", likelihood: "Low" }
        ]
    };

    displayPremiumReport(sampleData);
});

function displayPremiumReport(data) {
    document.getElementById('overall-score').textContent = data.overallScore.toFixed(2);
    document.getElementById('score-interpretation').textContent = getScoreInterpretation(data.overallScore);

    displayRadarChart(data.dimensionScores, data.industryBenchmarks);
    displayDimensionDetails(data.dimensionScores, data.recommendations);
    displayBenchmarkChart(data.dimensionScores, data.industryBenchmarks);
    displayRecommendations(data.recommendations);
    displayRoiProjection(data.roi);
    displayRiskAssessment(data.risks);
    displayRoadmap(data.dimensionScores);
    displayResources();
}

function displayRadarChart(scores, benchmarks) {
    const ctx = document.getElementById('radar-chart').getContext('2d');
    new Chart(ctx, {
        type: 'radar',
        data: {
            labels: Object.keys(scores),
            datasets: [{
                label: 'Your Scores',
                data: Object.values(scores),
                fill: true,
                backgroundColor: 'rgba(255, 99, 132, 0.2)',
                borderColor: 'rgb(255, 99, 132)',
                pointBackgroundColor: 'rgb(255, 99, 132)',
                pointBorderColor: '#fff',
                pointHoverBackgroundColor: '#fff',
                pointHoverBorderColor: 'rgb(255, 99, 132)'
            }, {
                label: 'Industry Benchmarks',
                data: Object.values(benchmarks),
                fill: true,
                backgroundColor: 'rgba(54, 162, 235, 0.2)',
                borderColor: 'rgb(54, 162, 235)',
                pointBackgroundColor: 'rgb(54, 162, 235)',
                pointBorderColor: '#fff',
                pointHoverBackgroundColor: '#fff',
                pointHoverBorderColor: 'rgb(54, 162, 235)'
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
}

function displayDimensionDetails(scores, recommendations) {
    const detailsHtml = Object.entries(scores).map(([dimension, score]) => `
        <div class="dimension-detail">
            <h3>${dimension}</h3>
            <p>Score: ${score}/10</p>
            <p>Recommendation: ${recommendations[dimension]}</p>
        </div>
    `).join('');

    document.getElementById('dimension-details').innerHTML = detailsHtml;
}

function displayBenchmarkChart(scores, benchmarks) {
    const ctx = document.getElementById('benchmark-chart').getContext('2d');
    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: Object.keys(scores),
            datasets: [{
                label: 'Your Scores',
                data: Object.values(scores),
                backgroundColor: 'rgba(255, 99, 132, 0.8)'
            }, {
                label: 'Industry Benchmarks',
                data: Object.values(benchmarks),
                backgroundColor: 'rgba(54, 162, 235, 0.8)'
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true,
                    max: 10
                }
            }
        }
    });
}

function displayRecommendations(recommendations) {
    const recHtml = Object.entries(recommendations).map(([dimension, rec]) => `
        <div class="recommendation">
            <h3>${dimension}</h3>
            <p>${rec}</p>
        </div>
    `).join('');

    document.getElementById('recommendation-details').innerHTML = recHtml;
}

function displayRoiProjection(roi) {
    document.getElementById('roi-details').innerHTML = `
        <p>Projected ROI: ${roi.projected}</p>
        <p>Estimated Timeframe: ${roi.timeframe}</p>
    `;
}

function displayRiskAssessment(risks) {
    const riskHtml = risks.map(risk => `
        <div class="risk">
            <h3>${risk.name}</h3>
            <p>Impact: ${risk.impact}</p>
            <p>Likelihood: ${risk.likelihood}</p>
        </div>
    `).join('');

    document.getElementById('risk-matrix').innerHTML = riskHtml;
}

function displayRoadmap(scores) {
    const priorities = Object.entries(scores)
        .sort((a, b) => a[1] - b[1])
        .map(([dimension, score]) => dimension);

    const roadmapHtml = `
        <h3>Short-term (0-3 months)</h3>
        <p>Focus on improving ${priorities[0]} and ${priorities[1]}</p>
        <h3>Medium-term (3-6 months)</h3>
        <p>Address ${priorities[2]} and ${priorities[3]}</p>
        <h3>Long-term (6-12 months)</h3>
        <p>Enhance ${priorities[4]} and ${priorities[5]}</p>
    `;

    document.getElementById('roadmap-details').innerHTML = roadmapHtml;
}

function displayResources() {
    const resources = [
        "AI for Business: A Practical Guide to Machine Learning",
        "Data Strategy: How to Profit from a World of Big Data, Analytics and the Internet of Things",
        "AI Ethics: A Framework for Responsible Innovation",
        "Leading Digital: Turning Technology into Business Transformation",
        "The AI Organization: Learn from Real Companies and Microsoft