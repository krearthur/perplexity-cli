from openai import OpenAI
import sys, re

# needs the OPENAI_API_KEY from environment variable to work
client = OpenAI( base_url="https://api.perplexity.ai")

user_input = ""
if (len(sys.argv) > 1):
    # Iteriere über die Argumente
    for arg in sys.argv[1:]:
        # Füge jedes Argument an den String an
        user_input += arg + " "
else:
    user_input = input("\033[34m\033[1mDeine Frage: \033[0m\n")

def convert_to_ansi(text):
    pattern = r'\*\*(.*?)\*\*'
    ansi_text = re.sub(pattern, r'\033[1m\1\033[0m\033[32m', text, flags=re.DOTALL)
    return ansi_text

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
print(f"\033[32m{convert_to_ansi(response.choices[0].message.content)}\033[0m")

# chat completion with streaming
# response_stream = client.chat.completions.create(
#     model="llama-3-sonar-large-32k-online",
#     messages=messages,
#     stream=True,
# )
# for response in response_stream:
#     print(response)
