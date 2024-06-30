from backend.models import Assessment, db
from backend.utils import calculate_scores, generate_free_report, generate_premium_report

def submit_assessment(data):
    assessment = Assessment(responses=data)
    db.session.add(assessment)
    db.session.commit()
    
    scores = calculate_scores(data)
    
    return {
        'assessment_id': assessment.id,
        'scores': scores
    }

def get_free_report(assessment_id):
    assessment = Assessment.query.get_or_404(assessment_id)
    return generate_free_report(assessment.responses)

def get_premium_report(assessment_id):
    assessment = Assessment.query.get_or_404(assessment_id)
    return generate_premium_report(assessment.responses)