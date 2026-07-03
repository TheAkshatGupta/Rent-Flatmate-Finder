def calculate_score(profile, listing):

    score = 0

    explanation = []

    # Budget (40)

    if profile.budget >= listing.rent:

        score += 40

        explanation.append(
            "Budget matches."
        )

    # Location (30)

    if profile.bio:

        if listing.city.lower() in profile.bio.lower():

            score += 30

            explanation.append(
                "Preferred location matches."
            )

    # Food (10)

    if profile.food_preference:

        score += 10

        explanation.append(
            "Food preference considered."
        )

    # Smoking (10)

    if profile.smoking == "No":

        score += 10

        explanation.append(
            "Non-smoker preference matched."
        )

    # Cleanliness (10)

    if profile.cleanliness:

        score += 10

        explanation.append(
            "Cleanliness preference matched."
        )

    return {

        "score": score,

        "explanation": " ".join(explanation)

    }