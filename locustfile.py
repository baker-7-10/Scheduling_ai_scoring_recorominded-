from locust import HttpUser, task, between

SUPABASE_URL = "https://taqdpudyhenvaibczyar.supabase.co"
SUPABASE_API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InRhcWRwdWR5aGVudmFpYmN6eWFyIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjI1MDk1NTMsImV4cCI6MjAzODA4NTU1M30.9f7hsNzSF5sHxyour38HblOybFP2cDkQsypLZg9xcUU"

class SupabaseUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def test_supabase_select(self):
        headers = {
            "apikey": SUPABASE_API_KEY,
            "Authorization": f"Bearer {SUPABASE_API_KEY}"
        }

        self.client.get(
            "/rest/v1/recommendation_category?select=*",
            headers=headers
        )
