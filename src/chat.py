from ollama import chat

response = chat(
    model='qwen:0.5b',
    messages=[{'role': 'user', 'content': 'Hi there!'}],
)

print(response.message.content)
