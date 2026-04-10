import json

with open("data/vehicles.json") as f:
    vehicles = json.load(f)["vehicles"]


def recommend(user_need):
    user_need = user_need.lower()

    scored = []

    for v in vehicles:
        score = 0
        reasons = []

        # Type Matching
        if "suv" in user_need and v["type"] == "SUV":
            score += 2
            reasons.append("Matches SUV preference")

        if "truck" in user_need or "pickup" in user_need:
            if v["type"] == "Truck":
                score += 2
                reasons.append("Suitable for truck/pickup usage")

        #Family Requirement
        if "family" in user_need:
            if v["type"] == "SUV" and v["seating_capacity"] >= 7:
                score += 3
                reasons.append("Good for families with higher seating capacity")

        #Towing Requirement
        if "towing" in user_need or "heavy" in user_need:
            if v["type"] == "Truck":
                score += 3
                reasons.append("High towing capability (truck category)")

        #Fuel Preference
        if "electric" in user_need and v["fuel_type"] == "Electric":
            score += 2
            reasons.append("Matches electric vehicle preference")

        if "hybrid" in user_need and v["fuel_type"] == "Hybrid":
            score += 2
            reasons.append("Matches hybrid vehicle preference")

        #Performance
        if "performance" in user_need or "sport" in user_need:
            if v["type"] == "Sports":
                score += 3
                reasons.append("High-performance sports vehicle")

        #Safety (general boost)
        if len(v.get("safety_features", [])) >= 3:
            score += 1
            reasons.append("Equipped with multiple safety features")

        # Only include relevant vehicles
        if score > 0:
            scored.append({
                "model": v["model"],
                "type": v["type"],
                "score": score,
                "reason": reasons
            })

    #Sort by score (descending)
    scored.sort(key=lambda x: x["score"], reverse=True)

    #Return top 2
    return scored[:2]