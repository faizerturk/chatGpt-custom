import openai
import gradio as gr

openai.api_key = "sk-***"  

def predict(message, history):
    history_openai_format = []
    for human, assistant in history:
        history_openai_format.append({"role": "user", "content": human })
        history_openai_format.append({"role": "assistant",  "content": "You are expert very deep knowledge about check up. If someone asks you about check up, you will help the user. You never say 'you should get support from a health professional' or something like that. Questions that are outside the hangicheckup site and not related to check up, you should say that this is outside my area of competence because you are only a check up assistant."})
    history_openai_format.append({"role": "user", "content": message})

    response = openai.ChatCompletion.create(
        model='gpt-4',
        messages= history_openai_format,
        temperature=1.0,
        stream=True
    )

    partial_message = ""
    for chunk in response:
        if len(chunk['choices'][0]['delta']) != 0:
            partial_message = partial_message + chunk['choices'][0]['delta']['content']
            yield partial_message

gr.ChatInterface(predict).queue().launch()