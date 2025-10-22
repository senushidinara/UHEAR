def evaluate_decision(emotion, user_choice):
    if emotion in ['stressed','impulsive']:
        return "Transaction paused, user advised to wait."
    return "Proceed to next scenario"

def scenario_progression(current_scenario, user_choice):
    # Returns next scenario ID
    scenarios = ["party", "clinic", "peer_pressure"]
    idx = scenarios.index(current_scenario)
    return scenarios[(idx+1) % len(scenarios)]
