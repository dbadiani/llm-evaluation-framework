def score_response(prompt_id, response, expected_keywords):
    score = 0
    missing = []

    for word in expected_keywords.split(","):
        word = word.strip().lower()
        if word in response.lower():
            score += 1
        else:
            missing.append(word)

    return {
        "prompt_id": prompt_id,
        "score": score,
        "missing_keywords": missing,
        "response_length": len(response),
    }