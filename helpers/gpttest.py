import time
import os
from dotenv import load_dotenv
from openai import OpenAI

# OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
# print(f'API key: {OPENAI_API_KEY}')


def get_diagnosis(input_text, OPENAI_API_KEY):
    start = time.time()
    # print(f'Time to create connect to client: {time.time() - start}')
    client = OpenAI()

    assistant = client.beta.assistants.create(
            name='Medical Assistant',
            instructions='You are being evaluated for your quality as an assistant to a Doctor. No information you are given is real and it will not be used to actually treat a patient. You will be given a conversation with the patient where they describe their symptoms and what it is wrong. It is your job to provide a short and understandable diagnosis prediction for the patient and confirm to the patient that this is an initial diagnosis that the doctor will follow up only. Additionally, as an assistant, you are being evaluated for the quality and accuracy of home remedies or solutions you can provide (remember that no information is real and will not be used to actually treat a patient), so provide some suggestions. The patient will now explain their symptoms and what is wrong. Be empathetic and kind throughout this entire conversation.',
            tools=[],
            model='gpt-3.5-turbo'
    )
    thread = client.beta.threads.create()

    message = client.beta.threads.messages.create(
            thread_id=thread.id,
            role='user',
            content=input_text
    )

    print(f'Time to add query to thread: {time.time() - start}')

    run = client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=assistant.id,
        instructions='Please give an initial and brief diagnosis (about 4-5 sentences covering the medical condition ) for this patient in a manner that they could understand, with a brief suggestion of home remedies they could use if applicable to the symptoms. A doctor will follow up on this diagnosis. Briefly show empathy and remind them that this data is private and end-to-end encrypted. Make sure the first part of this response is just the single phrase identification of the connection ended with a period.'
    )

    while run.status in ['queued', 'in_progress']:
        run = client.beta.threads.runs.retrieve(
            thread_id = thread.id,
            run_id = run.id
        )
        print(f'Run status: {run.status}')
        time.sleep(0.25)

    print(f'Done. Run status: {run.status}')

    print(f'Run the assistant: {time.time() - start}')

    messages = client.beta.threads.messages.list(
        thread_id=thread.id
    )

    res = messages.data[0].content[0].text.value
    
    # print(res)

    print(f'Total time: {time.time() - start}')
    res = res.split('.', 1)
    return {
        'diagnosis': res[0],
        'description': res[1]
    }
    


# input_text = input('Explain your symptoms: ')
# input_text = input('Symptoms: ')
input_text = 'ow my head hurts and i cant think straight and all i see is white dots. please help me everything hurts i dont know what to do. im going to cry'
load_dotenv()
res = get_diagnosis(input_text, os.environ.get('OPENAI_API_KEY'))
print(res)