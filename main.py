from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional

from ai.interest_engine import calculate_interest
from supabase_client import supabase
from scheduler.jobs import start_scheduler


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class InterestInput(BaseModel):
    time_sec: float
    product_name: str
    category: str
    rating: float = 0
    comment: Optional[str] = None
    favorite: bool = False
    cart: Optional[List[str]] = []
    user_id: str


@app.post("/calculate_interest")
def calculate_interest_api(payload: InterestInput):

    result = calculate_interest(
        time_sec=payload.time_sec,
        product_name=payload.product_name,
        category=payload.category,
        rating=payload.rating,
        comment=payload.comment,
        favorite=payload.favorite,
        cart=payload.cart
    )

    supabase.table("ia").insert({
        "product_name": result["product_name"],
        "category": result["category"],
        "interest_score": result["interest_score"],
        "user_id": payload.user_id,
    }).execute()

    return result


@app.on_event("startup")
def startup_event():
    start_scheduler()
    print("Scheduler started...")
