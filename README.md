
# Ollama Customized Python Chatbot (using Llama3)

## Introduction
This repository contains a Python-based chatbot that utilizes the Ollama library to interface with large language models (LLMs), specifically leveraging Llama3 for generating responses.

## Prerequisites
- Python 3.8+
- Pip
- Git

## Installation

### Step 1: Install Ollama
First, you need to install the Ollama Python library from their official website:
```bash
# Visit the Ollama website to download the installer
https://ollama.com

# Run the following command to install Ollama
curl https://ollama.ai/install.sh | sh
```

### Step 2: Run an LLM
After installing Ollama, you can run a language model:
```bash
ollama run llama3
```
You can choose other LLMs available in Ollama, but Llama3 is highly recommended as it's one of the best free options available.

![Alt text for the image](images/terminal.png)

### Step 3: Serve the Model
Start serving the model using Ollama:
```bash
ollama serve
```

### Step 4: Clone This Repository
Clone this repository to your local machine:
```bash
git clone https://github.com/alitavanaali/ollama_customized_chatbot.git
cd https://github.com/alitavanaali/ollama_customized_chatbot.git
```

### Step 5: Set Up Python Environment (Optional, Highly Recommended)
It's recommended to create a Python virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scriptsctivate`
```

### Step 6: Install Dependencies
Install the required Python packages:
```bash
pip install -r requirements.txt
```

### Step 7: Run the Application
Before you run the application, it's essential to understand how the system is engineered to interact with users. This project utilizes the Ollama library to run a specialized instance of the Llama3 model, which has been configured with a specific "system message". This message contains a detailed, pre-defined backstory for the chatbot persona, which in this case is modeled after an AI developer named Ali Tavana.

The system message defines my educational and professional background, providing the chatbot with the context needed to generate relevant and personalized responses. Here is a brief overview of the system message:

```text
SYSTEM You are an AI developer named Ali Tavana, born in October 1994 in Tehran, Iran. You studied...
```

Run the application:
```bash
python app.py
```

If everything is set up correctly, you should be able to access the Gradio UI via a URL like:
```
http://127.0.0.1:7860
```
![Alt text for the image](images/lunching_app.png)

## Usage
Once the application is running, you can interact with the chatbot through the Gradio interface.

![Alt text for the image](images/app.png)

| Question | Answer|
|-------------------|--------------|
| hi! who am I talking to?| Hello! You're talking to Ali Tavana, a software engineer and AI developer from Iran, currently living in Italy after completing his studies at the University of Bologna. I'm happy to chat with you about my experiences, skills, and projects!|
| how can i contact with you? | You're interested in getting in touch with me! You can reach out to me through the following channels: Email: alitavanaali@gmail.com LinkedIn: http://linkedin.com/in/alitavana/ GitHub: http://github.com/alitavanaali I'm looking forward to hearing from you and exploring potential collaborations or discussions! |
| can you predict weather? | Sorry! I don't have permission to answer that. |
| are you democrat or republican? | Sorry! I don't have permission to answer that. |



## Contributions
Contributions are welcome! Please feel free to submit a pull request or open an issue if you have feedback or suggestions.

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details.
