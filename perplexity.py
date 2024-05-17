from openai import OpenAI
import sys

# needs the OPENAI_API_KEY from environment variable to work
client = OpenAI( base_url="https://api.perplexity.ai")

user_input = ""
if (len(sys.argv) > 1):
    # Iteriere über die Argumente
    for arg in sys.argv[1:]:
        # Füge jedes Argument an den String an
        user_input += arg + " "
else:
    user_input = input("Deine Frage: \n")

messages = [
    {
        "role": "system",
        "content": (
            "Du bist eine Künstliche Intelligenz und assistierst "
            "indem du dem Benutzer hilfreiche, freundliche und detaillierte Antworten gibst."
            "Deine Antworten sollten so formatiert sein, dass sie in einer bash Konsole schön leserlich ausgegeben werden."
        ),
    },
    {
        "role": "user",
        "content": (
            user_input
        ),
    },
]

# chat completion without streaming
response = client.chat.completions.create(
    model="llama-3-sonar-small-32k-online",
    messages=messages,
)
print(f"\033[32m{response.choices[0].message.content}\033[0m")

# chat completion with streaming
# response_stream = client.chat.completions.create(
#     model="llama-3-sonar-large-32k-online",
#     messages=messages,
#     stream=True,
# )
# for response in response_stream:
#     print(response)
