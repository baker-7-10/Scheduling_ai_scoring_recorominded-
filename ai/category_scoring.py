def calculate_category_scores(user_data: list):
    scores = {
        "Women’s Fashion": 0,
        "Men’s Fashion": 0,
        "Electronics": 0,
        "Home & Lifestyle": 0,
        "Medicine": 0,
        "Sports & Outdoor": 0,
        "Baby’s & Toys": 0,
        "Groceries & Pets": 0,
        "Health & Beauty": 0
    }

    for row in user_data:
        category = row.get("category")
        interest_score = row.get("interest_score", 0)

        if category in scores:
            scores[category] += interest_score

    return scores
