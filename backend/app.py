from flask import Flask, request, jsonify, render_template
from models import db, Assessment
from utils import calculate_scores, generate_report

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///assessment.db'
db.init_app(app)

@app.route('/assessment', methods=['POST'])
def submit_assessment():
    data = request.json
    assessment = Assessment(responses=data)
    db.session.add(assessment)
    db.session.commit()
    scores = calculate_scores(data)
    return jsonify(scores)

@app.route('/report/<int:assessment_id>')
def get_report(assessment_id):
    assessment = Assessment.query.get_or_404(assessment_id)
    report_data = generate_report(assessment.responses)
    return render_template('free_report.html', report=report_data)

if __name__ == '__main__':
    app.run(debug=True)
