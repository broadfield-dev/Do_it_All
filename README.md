# Do It All

## Overview
The **Do It All** basic agent system for Python. It provides a framework for building automated AI agent scripts in Python using a variety of models and API's.

## Features
- Creates a path and follows it
- Internet Search
- Image Generation
- RAG system
- Document reading

## API Integrations
- Huggingface
- OpenAI
- Google GenAI

## Installation
### CLI

### 1. Clone and install the repository:
```bash
pip install git+https://github.com/broadfield-dev/Do_it_All
```

### 2. Run the demo script (demo.py):
```bash
python doitall/demo.py
```

### Python

### 1. Install Do_it_All
```bash
pip install git+https://github.com/broadfield-dev/Do_it_All
```

### 2. Save API Keys
```
Save your API keys as the following Environmental Variables to use the models from each.
- ```HF_KEY``` (Huggingface API)
- ```OPENAI_API_KEY```
- ```GEMINI_API_KEY```
If you are signed in to a service already, the environmental varialble may already be set
```

### 3. Load in Python
```python
from doitall import main
history = []
prompt_in="why is the sky blue?"
print(main.agent(prompt_in,history,mod=2,tok_in="",rand_seed=True,seed=1,max_thought=5,save_mem=False,recall_mem=False,rag_col=False))
```

### 3.1 Configure Models
The available models can be configured in the doitall/main.py file.  The format is as follows:

```python
client_openai=[
    {'type':'text','loc':'openai','name':"gpt-4o-mini",'rank':'op','max_tokens':128000,'schema':{'bos':['<|system|>','<|user|>','<|assistant|>'],'eos':'<|im_end|>'},'ppt':'None'},
    {'type':'audio','loc':'openai','name':"whisper-1",'rank':'op','max_tokens':32000,'schema':{'bos':[],'eos':''},'ppt':'None'},
]
```

# TODO
- Add more model sources
- Screen Reading
- Console Control
- Screen Control
- Voice in/out

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
