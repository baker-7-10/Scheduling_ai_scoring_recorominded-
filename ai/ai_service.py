from supabase_client import supabase
from .category_scoring import calculate_category_scores


def update_or_publish_score(user_id: str):

    existing_users = supabase.table(
        "recommendation_category"
    ).select("user_id").execute()

    result2 = [row["user_id"] for row in existing_users.data]

    response = supabase.table("ia").select("*").eq("user_id", user_id).execute()

    if not response.data:
        raise Exception(f"No data for user {user_id}")

    result = calculate_category_scores(response.data)

    payload = {
        "WomenFashion": result["Women’s Fashion"],
        "MenFashion": result["Men’s Fashion"],
        "Electronics": result["Electronics"],
        "HomeLifestyle": result["Home & Lifestyle"],
        "Medicine": result["Medicine"],
        "SportsOutdoor": result["Sports & Outdoor"],
        "BabyToys": result["Baby’s & Toys"],
        "GroceriesPets": result["Groceries & Pets"],
        "HealthBeauty": result["Health & Beauty"]
    }

    if user_id in result2:
        supabase.table("recommendation_category") \
            .update(payload) \
            .eq("user_id", user_id) \
            .execute()
    else:
        payload["user_id"] = user_id
        supabase.table("recommendation_category").insert(payload).execute()

    return result
