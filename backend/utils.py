def calculate_scores(responses):
    # Implement your scoring logic here
    scores = {dimension: value for dimension, value in responses.items()}
    return scores

def generate_free_report(responses):
    scores = calculate_scores(responses)
    # Generate basic report data
    return {
        'scores': scores,
        'overall_score': sum(scores.values()) / len(scores),
        # Add other relevant data for the free report
    }

def generate_premium_report(responses):
    scores = calculate_scores(responses)
    # Generate more detailed report data
    return {
        'scores': scores,
        'overall_score': sum(scores.values()) / len(scores),
        # Add other relevant data for the premium report
    }