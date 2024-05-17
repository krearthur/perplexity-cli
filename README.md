**Simple Perplexity Ai Q&A**
=====================

### Overview

This script is a command-line interface to interact with the Perplexity AI chatbot. It uses the OpenAI API to send user input to the chatbot and prints the response.
It has no capability for follow up questions. Each prompt is a new prompt and has nothing todo with the previous.

### Usage

#### Environment Variable

Before running the script, you need to set the `OPENAI_API_KEY` environment variable to your OpenAI API key.

#### Running the Script

You can run the script from the command line, passing your question or input as an argument:
```bash
# dont use question mark at the end!
python perplexity.py whats uuuup

# or use quotes
python perplexity.py "whats uuuup?"

# or dont provide a argument at all to get promptet for an input, where you can write longer prompts:
python perplexity.py
>Ihre Frage:
whats uuuup?
```
#### Example output
```
Das ist ein ziemlich umfangreiches Suchergebnis, das verschiedene Aspekte des Begriffs "Wassup" abdeckt. 

**Wassup? - Die Budweiser-Kampagne**
Die originale Kampagne von Budweiser, die von 1999 bis 2002 lief, war ein großer Erfolg und wurde in vielen Ländern weltweit ausgestrahlt. Sie basierte auf einem Kurzfilm namens "True", der von Charles Stone III geschrieben und gedreht wurde. Die Werbung zeigte eine Gruppe von Freunden, die sich über das Telefon unterhielten und "whassup?" sagten, was zu einem Kultstatus führte.

**Wassup? - Die Musik**
Es gibt auch eine Musikgruppe namens 4 Non Blondes, die ein Lied namens "What's Up?" veröffentlichten. Das Lied wurde 1992 veröffentlicht und erreichte große Popularität. Es ist bekannt für seine emotionalen und inspirierenden Texte.

**Wassup? - Die Parodie in Scary Movie**
In dem Horrorfilm-Parodie "Scary Movie" aus dem Jahr 2000 wird der Begriff "Wassup?" parodiert. In einem bestimmten Szenario wird Shorty von Ghostface angerufen, um zu fragen, was er macht. Dieser Film ist eine Satire auf moderne Horrorfilme und wurde sehr erfolgreich.

**Wassup? - Aktuelle Verwendung**
In jüngerer Zeit wurde der Begriff "Wassup?" in verschiedenen Kontexten verwendet, wie z.B. in einem neuen Werbekampagne von Budweiser, die sich an die COVID-19-Pandemie anpasste. Der Begriff wurde auch in verschiedenen Medien, wie Filmen und Fernsehserien, als Referenz verwendet.

Insgesamt zeigt das Suchergebnis, dass der Begriff "Wassup?" eine breite Vielfalt von Anwendungen und Referenzen hat, von Werbung bis hin zu Musik und Film.
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
