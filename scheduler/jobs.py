from apscheduler.schedulers.background import BackgroundScheduler
from supabase_client import supabase
from ai.ai_service import update_or_publish_score


def run_ml_for_all_users():
    response_ids = supabase.table("User").select("id").execute()
    list_of_id = [row["id"] for row in response_ids.data]

    for user_id in list_of_id:
        try:
            update_or_publish_score(user_id)
            print(f"Updated ML score for user {user_id}")
        except Exception as e:
            print(f"Error updating user {user_id}: {e}")


def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(run_ml_for_all_users, "interval", minutes=1)
    scheduler.start()
