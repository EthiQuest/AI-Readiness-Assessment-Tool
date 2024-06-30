from flask import Blueprint, request, jsonify, render_template
from backend.models import Assessment
from backend.services.assessment_service import submit_assessment, get_free_report, get_premium_report

bp = Blueprint('assessment', __name__)

@bp.route('/assessment', methods=['POST'])
def submit_assessment_route():
    data = request.json
    result = submit_assessment(data)
    return jsonify(result)

@bp.route('/report/<int:assessment_id>')
def get_free_report_route(assessment_id):
    report_data = get_free_report(assessment_id)
    return render_template('free_report.html', report=report_data)

@bp.route('/premium-report/<int:assessment_id>')
def get_premium_report_route(assessment_id):
    report_data = get_premium_report(assessment_id)
    return render_template('premium_report.html', report=report_data)