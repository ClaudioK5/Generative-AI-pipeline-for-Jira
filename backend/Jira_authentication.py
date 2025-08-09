import requests
from requests.auth import HTTPBasicAuth


def Jira_authentication(JIRA_DOMAIN, JIRA_EMAIL, JIRA_API_TOKEN):
    
    PROJECT_KEY = "KAN"
    MAX_RESULTS = 50

    auth = HTTPBasicAuth(JIRA_EMAIL, JIRA_API_TOKEN)
    headers = {'Accept' : 'application/json'}
    url = f"{JIRA_DOMAIN}/rest/api/3/search"

    query = {
    'jql' : f'project = {PROJECT_KEY} AND status in ("Done", "In Progress", "To Do")',
    'maxResults': MAX_RESULTS,
    'fields': 'summary,assignee,status,duedate,created,resolutiondate'
    }

    response = requests.get(url, headers=headers, params=query, auth=auth)

    tasks = response.json()['issues']

    print(tasks)

    return tasks
