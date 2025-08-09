import openai
from backend.gateway_openai import gateway_openai
from backend.send_email import send_email
from backend.Jira_tasks_reorganizator import Jira_tasks_reorganizator
from backend.Jira_tasks_reports import Jira_tasks_reports
from backend.Jira_authentication import Jira_authentication



JIRA_DOMAIN = "insert your jira domain"
JIRA_EMAIL = "insert your jira email"
JIRA_API_TOKEN = "insert your jira api token"


tasks = Jira_authentication(JIRA_DOMAIN, JIRA_EMAIL, JIRA_API_TOKEN)

tasks_by_user = Jira_tasks_reorganizator(tasks)

task_summaries = Jira_tasks_reports(tasks_by_user)


print(task_summaries)



openai.api_key = "insert your api key for openai"

gateway_openai(task_summaries)


