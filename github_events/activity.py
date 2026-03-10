from datetime import datetime, timezone

class Activity:
    def __init__(self, activity_type, repo, date, payload=None):
          self.type = activity_type
          self.repo = repo 
          self.count = 1
          self.payload = payload 
          self.date = date
    
    @staticmethod
    def compare(A, B):
        if A.is_same_type(B):
            return 0
        if A.repo.lower() != B.repo.lower():
            return -1 if A.repo.lower() < B.repo.lower() else 1
        if A.type != B.type:
            return -1 if A.type < B.type else 1
        return -1 if A.payload['action'] < B.payload['action'] else 1

    def is_same_type(self, activity):
        if self.type != activity.type or self.repo != activity.repo:
            return False
        if self.type in ('PullRequestEvent', 'DiscussionEvent', 'IssuesEvent'):
            return self.payload['action'] == activity.payload['action']
        return True

    def __str__(self):
        dt = datetime.fromisoformat(self.date)
        dt = dt.strftime("%Y-%m-%d %H:%M:%S")

        repo_at_text = f"{self.repo} at {dt}"

        if self.type == 'PushEvent':
            return f"Pushed {"a commit" if self.count == 1 else str(self.count) + " commits"} to {repo_at_text}"
        elif self.type == 'WatchEvent':
            return f"Watched {repo_at_text}"
        elif self.type == 'CreateEvent':
            if self.payload['ref_type'] == 'repository':
                return f"Created {repo_at_text}"
            else:
                return f"Created {self.payload['ref_type']} {self.payload['ref']} in {repo_at_text}"
        elif self.type == 'DeleteEvent':
                return f"Deleted {self.payload['ref_type']} {self.payload['ref']} in {repo_at_text}"
        elif self.type == 'PullRequestEvent':
                return f"{self.payload['action'].title()} {"a pull request" if self.count == 1 else str(self.count) + " pull requests"} in {repo_at_text}"
        elif self.type == 'DiscussionEvent':
                return f"{self.payload['action'].title()} {"a discussion" if self.count == 1 else str(self.count) + " discussions"} in {repo_at_text}"
        elif self.type == 'IssuesEvent':
                return f"{self.payload['action'].title()} {"an issue" if self.count == 1 else str(self.count) + " issues"} in {repo_at_text}"
        elif self.type == 'IssueCommentEvent':
                return f"Left {"a comment" if self.count == 1 else str(self.count) + " comments"} on an issue in {repo_at_text}"
        else:
            return f"{self.type} at {dt} {self.payload}"