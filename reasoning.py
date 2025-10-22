def generate_advice(emotion, intent):
    points = 0
    if emotion in ['stressed','impulsive']:
        advice = "Pause and think carefully before proceeding."
        points += 5
    elif intent == "safe_choice":
        advice = "Excellent choice! You protected yourself."
        points += 15
    else:
        advice = "Consider safer alternatives."
        points += 10
    return advice, points
