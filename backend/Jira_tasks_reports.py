from datetime import datetime


def Jira_tasks_reports(tasks_by_user):
    
    i=0
    
    task_summaries = []
    
    for assignee, tasks in tasks_by_user.items():

        
    
        
        if assignee not in task_summaries:
        
            report_assignee = f"Report for {assignee}:  "
            task_summaries.append(report_assignee)


        
        

        for task in tasks:


        
        

            due_date = task['due_date']
            print(due_date)
            status = task['status']

            resolution_date = task['resolution_date']

            if due_date: 
                due = datetime.strptime(due_date, '%Y-%m-%d') 
           
            else:
                due = None
            
            if resolution_date is not None:
                print(f"resolution data raw value: {task['resolution_date']}")
                resolved = datetime.strptime(resolution_date[:10],'%Y-%m-%d') 
            else:
                None

            if due and resolved:
                delta = (resolved - due).days
            
                if delta <=0 :
                    task_summaries[i] = task_summaries[i] + f"the status for '{task['summary']}' is On Time;  "  
        
                elif delta > 0:
                    task_summaries[i] = task_summaries[i] +  f"the status for '{task['summary']}' is: {delta} days late;  "

            elif due and not resolved:
                delta = (datetime.now() -due).days
                if delta > 0:
                    task_summaries[i] =+ task_summaries[i] + f"the status for '{task['summary']}' is pending with {delta} days overdue ;  "
                elif delta < 0:
                    task_summaries[i] =+ task_summaries[i] + f"the status for '{task['summary']}' is pending on time;   "

        i = i + 1
        
    return task_summaries
