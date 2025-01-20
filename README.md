# Do It All

## Overview
The **Do It All** basic agent system for Python. It provides a framework for building automated AI agent scripts in Python using a variety of models and API's.

## Features
- Creates a path and follows it
- Internet Search
- Image Generation
- RAG system
- Document reading
- Normal Chatbot

## Installation
### CLI

### 1. Clone the repository:
```bash
git clone https://github.com/broadfield-dev/Do_it_All.git
```

### 2. Install dependencies:
```bash
pip install ./doitall
```

### 3. Run the demo script (demo.py):
```bash
python doitall/demo.py
```
### 3.1 Run the demo script (demo2.py):
Demo2 includes RAG, and document reading, and requires additional dependency installs
```bash
pip install ollama langchain langchain_community langchain_chroma langchain_huggingface pypdf
```
Now run the demo
```bash
python doitall/demo2.py
```
### Python

Save your API keys as the following Environmental Variables to use the models from each.
- ```HF_KEY``` (Huggingface API)
- ```OPENAI_API_KEY```
- ```GEMINI_API_KEY```

The available models can be updated in the doitall/main.py file.  The format is as follows:
client_openai=[
    {'type':'text','loc':'openai','name':"gpt-4o-mini",'rank':'op','max_tokens':128000,'schema':{'bos':['<|system|>','<|user|>','<|assistant|>'],'eos':'<|im_end|>'},'ppt':'None'},
    {'type':'audio','loc':'openai','name':"whisper-1",'rank':'op','max_tokens':32000,'schema':{'bos':[],'eos':''},'ppt':'None'},
]


# TODO
- Add more model sources
- Screen Reading
- Console Control
- Screen Control
- Voice in/out

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
