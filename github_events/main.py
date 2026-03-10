from github_activity_retriever import GitHubActivityRetriever
from activity import Activity


username = input("> Enter username whose activity you'd like to see: ")
github_activity = GitHubActivityRetriever(username)
activity_list = github_activity.get_activity()

if activity_list is None:
    print("Error fetching information. Please check the username and try again.")
    exit()

for activity in activity_list:
    print(activity)
