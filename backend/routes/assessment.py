from flask import Blueprint, request, jsonify, render_template
from backend.models import Assessment
from backend.services.assessment_service import submit_assessment, get_free_report, get_premium_report
from backend.services.llm_service import llm_service
from backend.services.ai_integration_service import ai_integration_service

bp = Blueprint('assessment', __name__)

@bp.route('/assessment', methods=['POST'])
def submit_assessment_route():
    data = request.json
    
    # Traditional assessment
    traditional_result = submit_assessment(data)
    
    # LLM-based assessment
    llm_assessment = llm_service.generate_assessment(data)
    
    # AI service integrations assessments
    azure_assessment = ai_integration_service.azure_openai_assessment(data)
    claude_assessment = ai_integration_service.anthropic_claude_assessment(data)
    
    # Combine all assessments
    combined_result = {
        'traditional_assessment': traditional_result,
        'llm_assessment': llm_assessment,
        'azure_assessment': azure_assessment,
        'claude_assessment': claude_assessment
    }
    
    # Here, you might want to save the combined result to your database
    # and return an assessment ID for future reference
    
    return jsonify(combined_result)

@bp.route('/report/<int:assessment_id>')
def get_free_report_route(assessment_id):
    report_data = get_free_report(assessment_id)
    return render_template('free_report.html', report=report_data)

@bp.route('/premium-report/<int:assessment_id>')
def get_premium_report_route(assessment_id):
    report_data = get_premium_report(assessment_id)
    
    # For premium reports, we might want to include the LLM and AI service assessments
    llm_assessment = llm_service.get_assessment(assessment_id)
    ai_assessments = ai_integration_service.get_assessments(assessment_id)
    
    combined_report = {
        **report_data,
        'llm_assessment': llm_assessment,
        'ai_assessments': ai_assessments
    }
    
    return render_template('premium_report.html', report=combined_report)

@bp.route('/comparative-report/<int:assessment_id>')
def get_comparative_report_route(assessment_id):
    traditional_report = get_premium_report(assessment_id)
    llm_assessment = llm_service.get_assessment(assessment_id)
    ai_assessments = ai_integration_service.get_assessments(assessment_id)
    
    comparative_report = {
        'traditional': traditional_report,
        'llm': llm_assessment,
        'ai_services': ai_assessments
    }
    
    return render_template('comparative_report.html', report=comparative_report)