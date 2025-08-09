import openai
from .send_email import send_email

first_prompt = 'make a short analysis of the tasks for each user. the user is written after report for ...'

def gateway_openai(task_summaries):

    email = 'insert your email here'

    subject = "AI-Generated generated report for user"

    for prompt in task_summaries:

        print(prompt)

        print('sending prompt to chatgpt')

        response = openai.chat.completions.create(model = "gpt-3.5-turbo", messages=[{'role' : 'user', 'content': first_prompt}, {
        'role' : 'user', 'content': prompt }], max_tokens = 250)

        ai_output = response.choices[0].message.content.strip()
        
        send_email(email, subject, ai_output)
    
        print(f"Email sent to {email} successfully!")
    
        print(ai_output)