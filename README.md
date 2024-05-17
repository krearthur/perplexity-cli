**Perplexity AI Chatbot**
=====================

### Overview

This script is a command-line interface to interact with the Perplexity AI chatbot. It uses the OpenAI API to send user input to the chatbot and prints the response.

### Usage

#### Environment Variable

Before running the script, you need to set the `OPENAI_API_KEY` environment variable to your OpenAI API key.

#### Running the Script

You can run the script from the command line, passing your question or input as an argument:
```bash
python perplexity.py "Your question here"
```

If you don't provide an argument, the script will prompt you to enter your question.

### How it Works
The script creates a chat completion request to the Perplexity AI model, passing the user's input as a message. It then prints the response from the chatbot.
### Note
This script assumes you have the OpenAI library installed. You can install it using pip:

```bash
pip install openai
```

### License
This script is licensed under the MIT License.
