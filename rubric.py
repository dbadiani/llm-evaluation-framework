def evaluate_quality(response):
    issues = []

    if len(response) < 30:
        issues.append("too_short")

    if "I don't know" in response:
        issues.append("uncertain_answer")

    if "maybe" in response.lower():
        issues.append("low_confidence_language")

    return issues