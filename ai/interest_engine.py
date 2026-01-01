from typing import List, Optional

class InterestEngine:
    MAX_SCORE = 100

    def calculate(
        self,
        time_sec: float,
        rating: float = 0,
        comment: Optional[str] = None,
        favorite: bool = False,
        cart: Optional[List[str]] = None
    ) -> float:

        if cart is None:
            cart = []

        capped_time = min(max(time_sec, 0), 300)
        time_score = (capped_time / 300) * 90

        rating_score = (min(max(rating, 0), 5) / 5) * 5
        favorite_score = 3 if favorite else 0
        comment_score = 2 if comment else 0
        cart_score = min(len(cart), 3)

        final_score = (
            time_score +
            rating_score +
            favorite_score +
            comment_score +
            cart_score
        )

        return round(min(final_score, self.MAX_SCORE), 2)


engine = InterestEngine()


def calculate_interest(
    time_sec: float,
    product_name: str,
    category: str,
    rating: float = 0,
    comment: Optional[str] = None,
    favorite: bool = False,
    cart: Optional[list] = None
):
    score = engine.calculate(
        time_sec=time_sec,
        rating=rating,
        comment=comment,
        favorite=favorite,
        cart=cart
    )

    return {
        "product_name": product_name,
        "category": category,
        "interest_score": score
    }
