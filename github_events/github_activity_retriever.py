import requests 
from activity import Activity
from functools import cmp_to_key

class GitHubActivityRetriever:
    def __init__(self, username):
        self.username = username

        self.NUM_EVENTS_PER_PAGE = 10

    def get_activity(self, page_num=1):
        response = requests.get(f"https://api.github.com/users/{self.username}/events/public", params={"page": page_num, "per_page": self.NUM_EVENTS_PER_PAGE}, timeout=10)

        if response.status_code != 200:
            return None
        
        activities = response.json()

        activity_list = [Activity(activity['type'], activity['repo']['name'], activity['created_at'], activity['payload'])
                        for activity in activities]

        activity_list.sort(key=cmp_to_key(Activity.compare))
        
        compressed_activities = []
        for activity in activity_list:
            if compressed_activities and compressed_activities[-1].is_same_type(activity):
                compressed_activities[-1].count += 1
                continue
            
            compressed_activities.append(activity)

        return compressed_activities