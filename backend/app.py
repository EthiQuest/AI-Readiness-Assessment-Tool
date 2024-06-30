from flask import Flask, request, jsonify, render_template, send_from_directory
from models import db, Assessment
from utils import calculate_scores, generate_free_report, generate_premium_report
import os

app = Flask(__name__, static_folder='../frontend', template_folder='../templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///assessment.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/assessment', methods=['POST'])
def submit_assessment():
    data = request.json
    assessment = Assessment(responses=data)
    db.session.add(assessment)
    db.session.commit()
    
    scores = calculate_scores(data)
    
    return jsonify({
        'assessment_id': assessment.id,
        'scores': scores
    })

@app.route('/report/<int:assessment_id>')
def get_free_report(assessment_id):
    assessment = Assessment.query.get_or_404(assessment_id)
    report_data = generate_free_report(assessment.responses)
    return render_template('free_report.html', report=report_data)

@app.route('/premium-report/<int:assessment_id>')
def get_premium_report(assessment_id):
    assessment = Assessment.query.get_or_404(assessment_id)
    report_data = generate_premium_report(assessment.responses)
    return render_template('premium_report.html', report=report_data)

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory(app.static_folder, path)

if __name__ == '__main__':
    app.run(debug=True)