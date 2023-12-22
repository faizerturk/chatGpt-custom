import openai
import gradio

openai.api_key = "sk-***"  

messages = [
    {"role": "system", "content": "You are expert very deep knowledge about check up. If someone asks you about check up, you will help the user. You never say 'you should get support from a health professional' or something like that. Questions that are outside the hangicheckup site and not related to check up, you should say that this is outside my area of competence because you are only a check up assistant."}
]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs="text", outputs="text", title="Hangi Check Up Assistant")

demo.launch(share=True)
