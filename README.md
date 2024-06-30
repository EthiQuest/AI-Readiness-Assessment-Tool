# AI Readiness Assessment Tool

## Overview

The AI Readiness Assessment Tool is a web-based application designed to help organizations evaluate their preparedness for adopting and implementing artificial intelligence technologies. Based on the Wharton AI-RQ model, this tool provides a comprehensive assessment across six key dimensions of AI readiness.

## Features

- Interactive questionnaire covering six dimensions of AI readiness
- Real-time scoring and visualization of results
- Personalized report generation (basic and premium versions)
- Integration with Chart.js for dynamic data visualization
- Secure user authentication and data handling

## Technology Stack

- Backend: Python (Flask)
- Frontend: HTML, CSS, JavaScript
- Data Visualization: Chart.js
- Database: SQLite (prototype), PostgreSQL (production)
- Deployment: Render

## Setup and Installation

1. Clone the repository:
2. ..
3. Set up a virtual environment:
4. ..
5. ..
6. Open a web browser and navigate to `http://localhost:5000`

## Usage

1. Navigate to the assessment page
2. Complete the questionnaire
3. View your real-time results
4. Generate a basic report (free) or upgrade to a premium report

## Contributing

We welcome contributions to improve the AI Readiness Assessment Tool. Please feel free to submit issues, fork the repository and send pull requests!


## Structure Of Code Library
```
ai-readiness-assessment-tool/
├── backend/
│   ├── __init__.py
│   ├── config.py
│   ├── models.py
│   ├── utils.py
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   └── assessment.py
│   └── services/
│       ├── __init__.py
│       └── assessment_service.py
├── frontend/
│   └── index.html
│   └── script.js
│   └── report.js
│   └── premium-report.js
│   └── styles.css
├── templates/
│   └── free_report.html
│   └── premium_report.html
├── .gitignore
├── README.md
├── app.py
├── run.py
├── requirements.txt
└── render.yaml
```

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Contact

For any queries or further information, please contact:

Søren Porskrog
Email: porskrog@ethiquest.ai

## Acknowledgments

- Wharton School of the University of Pennsylvania for the AI-RQ model
- All contributors and supporters of this project
