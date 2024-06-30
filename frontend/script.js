document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('ai-readiness-form');
    const resultsSection = document.getElementById('results');
    const generateReportBtn = document.getElementById('generate-report');

    // Sample questions for each dimension
    const questions = [
        { dimension: 'Leadership', question: 'How committed is your leadership to AI adoption?' },
        { dimension: 'Data', question: 'How would you rate your organization\'s data quality and accessibility?' },
        { dimension: 'Technology', question: 'How advanced is your current IT infrastructure for AI integration?' },
        { dimension: 'People', question: 'How would you rate your team\'s AI and data science skills?' },
        { dimension: 'Process', question: 'How well-defined are your processes for AI implementation?' },
        { dimension: 'Governance', question: 'How robust are your AI governance and ethics policies?' }
    ];

    // Populate the form with questions
    questions.forEach((q, index) => {
        const questionHtml = `
            <div class="question">
                <h3>${q.dimension}</h3>
                <p>${q.question}</p>
                <input type="range" id="q${index}" name="q${index}" min="1" max="10" value="5">
                <span class="range-value">5</span>
            </div>
        `;
        form.insertAdjacentHTML('beforeend', questionHtml);
    });

    // Add submit button to form
    form.insertAdjacentHTML('beforeend', '<button type="submit">Submit Assessment</button>');

    // Update range value display
    form.addEventListener('input', function(e) {
        if (e.target.type === 'range') {
            e.target.nextElementSibling.textContent = e.target.value;
        }
    });

    // Handle form submission
    form.addEventListener('submit', function(e) {
        e.preventDefault();
        const formData = new FormData(form);
        const responses = {};
        
        questions.forEach((q, index) => {
            responses[q.dimension] = parseInt(formData.get(`q${index}`));
        });

        submitAssessment(responses);
    });

    async function submitAssessment(responses) {
        try {
            const response = await fetch('/assessment', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(responses),
            });
            const scores = await response.json();
            displayResults(scores);
        } catch (error) {
            console.error('Error submitting assessment:', error);
            alert('There was an error submitting your assessment. Please try again.');
        }
    }

    function displayResults(scores) {
        const ctx = document.getElementById('radar-chart').getContext('2d');
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

        const overallScore = Object.values(scores).reduce((a, b) => a + b, 0) / Object.values(scores).length;
        document.getElementById('score-summary').textContent = `Your overall AI Readiness score is ${overallScore.toFixed(2)} out of 10.`;

        resultsSection.classList.remove('hidden');
    }

    generateReportBtn.addEventListener('click', function() {
        // In a real application, this would send the scores to the server and redirect to the report page
        alert('Generating report... In a full implementation, this would redirect to your report page.');
    });
});