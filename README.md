
# Ollama Python Chatbot

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

### Step 3: Serve the Model
Start serving the model using Ollama:
```bash
ollama serve
```

### Step 4: Clone This Repository
Clone this repository to your local machine:
```bash
git clone <repository-url>
cd <repository-name>
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
Run the application:
```bash
python app.py
```

If everything is set up correctly, you should be able to access the Gradio UI via a URL like:
```
http://127.0.0.1:7860
```

## Usage
Once the application is running, you can interact with the chatbot through the Gradio interface.

## Contributions
Contributions are welcome! Please feel free to submit a pull request or open an issue if you have feedback or suggestions.

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details.
