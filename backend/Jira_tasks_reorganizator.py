def Jira_tasks_reorganizator(tasks):

    tasks_by_user = {}

    for task in tasks:
        assignee = task['fields']['assignee']['displayName'] if task['fields']['assignee'] else "Unassigned"
        summary = task['fields']['summary']
        due_date = task['fields']['duedate']
        resolution_date = task['fields']['resolutiondate']
        status = task['fields']['status']['name']

        task_data  = {
        "summary": summary,
        "due_date": due_date,
        "status": status,
        "resolution_date": resolution_date

        }

        if assignee not in tasks_by_user:
            tasks_by_user[assignee] = []
    
        tasks_by_user[assignee].append(task_data)

    print('printing tasks by user!')

    print(tasks_by_user)

    return tasks_by_user
