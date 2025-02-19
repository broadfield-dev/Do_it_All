import gradio as gr
import random
from doitall import main
from doitall import gradio_theme as gt
from doitall import gradio_sidebar as gs
from doitall.addons import html_screenshot as ss

def isV(inp,is_=False):  # Verbose
    if is_==True:
        print(inp)
        is_=False

clients_main=[]
client_hf=[
    
    {'type':'image','loc':'hf','key':'','name':'black-forest-labs/FLUX.1-dev','rank':'op','max_tokens':16000,'schema':{'bos':'<|im_start|>','eos':'<|im_end|>'},'ppt':'None'},
    {'type':'image','loc':'hf','key':'','name':'ostris/Flex.1-alpha','rank':'op','max_tokens':16384,'schema':{'bos':'<|im_start|>','eos':'<|im_end|>'},'ppt':'None'},
    {'type':'text','loc':'hf','name':'Qwen/Qwen2.5-Coder-32B-Instruct','rank':'op','max_tokens':16000,'schema':{'bos':'<|im_start|>','eos':'<|im_end|>'},'ppt':'None'},
    {'type':'text','loc':'hf','name':'Qwen/Qwen2.5-72B-Instruct','rank':'op','max_tokens':32768,'schema':{'bos':'<|im_start|>','eos':'<|im_end|>'},'ppt':'None'},
    {'type':'text','loc':'hf','name':'Qwen/QwQ-32B-Preview','rank':'op','max_tokens':16384,'schema':{'bos':'<|im_start|>','eos':'<|im_end|>'},'ppt':'None'},
    {'type':'text','loc':'hf','name':'mistralai/Mixtral-8x7B-Instruct-v0.1','rank':'op','max_tokens':40000,'schema':{'bos':'<s>','eos':'</s>'},'ppt':'None'},
    {'type':'text','loc':'hf','name':'mistralai/Mixtral-7B-Instruct-v0.2','rank':'op','max_tokens':40000,'schema':{'bos':'<s>','eos':'</s>'},'ppt':'None'},
    {'type':'text','loc':'hf','name':'mistralai/Mixtral-7B-Instruct-v0.3','rank':'op','max_tokens':40000,'schema':{'bos':'<s>','eos':'</s>'},'ppt':'None'},
    {'type':'text','loc':'hf','name':'deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B','rank':'op','max_tokens':40000,'schema':{'bos':'<s>','eos':'</s>'},'ppt':'None'},
    {'type':'text','loc':'hf','name':'deepseek-ai/DeepSeek-R1-Distill-Qwen-32B','rank':'op','max_tokens':40000,'schema':{'bos':'<s>','eos':'</s>'},'ppt':'None'},
    {'type':'text','loc':'hf','name':'meta-llama/Llama-3.1-8B-Instruct','rank':'op','max_tokens':16384,'schema':{'bos':'<|im_start|>','eos':'<|im_end|>'},'ppt':'None'},
    {'type':'text','loc':'hf','name':'meta-llama/Llama-3,2-3B-Instruct','rank':'op','max_tokens':16384,'schema':{'bos':'<|im_start|>','eos':'<|im_end|>'},'ppt':'None'},
    {'type':'text','loc':'hf','name':'meta-llama/Llama-3.3-70B-Instruct','rank':'op','max_tokens':16384,'schema':{'bos':'<|im_start|>','eos':'<|im_end|>'},'ppt':'None'},
    {'type':'text','loc':'hf','name':'google/gemma-2-2b-it','rank':'op','max_tokens':16384,'schema':{'bos':'<|im_start|>','eos':'<|im_end|>'},'ppt':'None'},
    {'type':'text','loc':'hf','name':'google/gemma-2-9b-it','rank':'op','max_tokens':16384,'schema':{'bos':'<|im_start|>','eos':'<|im_end|>'},'ppt':'None'},
    {'type':'text','loc':'hf','name':'google/gemma-2-27b-it','rank':'op','max_tokens':16384,'schema':{'bos':'<|im_start|>','eos':'<|im_end|>'},'ppt':'None'},
    {'type':'text','loc':'hf','name':'microsoft/Phi-3-mini-4k-instruct','rank':'op','max_tokens':16384,'schema':{'bos':'<|im_start|>','eos':'<|im_end|>'},'ppt':'None'},
    {'type':'text','loc':'hf','name':'microsoft/Phi-3.5-mini-instruct','rank':'op','max_tokens':16384,'schema':{'bos':'<|im_start|>','eos':'<|im_end|>'},'ppt':'None'},
]

client_openai=[
    {'type':'text','loc':'openai','name':"gpt-4o-mini",'rank':'op','max_tokens':128000,'schema':{'bos':['<|system|>','<|user|>','<|assistant|>'],'eos':'<|im_end|>'},'ppt':'None'},
    {'type':'audio','loc':'openai','name':"whisper-1",'rank':'op','max_tokens':128000,'schema':{'bos':['<|system|>','<|user|>','<|assistant|>'],'eos':'<|im_end|>'},'ppt':'None'},
    {'type':'audio','loc':'openai','name':"tts-1",'rank':'op','max_tokens':128000,'schema':{'bos':['<|system|>','<|user|>','<|assistant|>'],'eos':'<|im_end|>'},'ppt':'None'},
    {'type':'image','loc':'openai','name':"dall-e-2",'rank':'op','max_tokens':128000,'schema':{'bos':['<|system|>','<|user|>','<|assistant|>'],'eos':'<|im_end|>'},'ppt':'None'},
    {'type':'image','loc':'openai','name':"dall-e-3",'rank':'op','max_tokens':128000,'schema':{'bos':['<|system|>','<|user|>','<|assistant|>'],'eos':'<|im_end|>'},'ppt':'None'},
]
client_google=[
    {'type':'text','loc':'google','name':"gemini-2.0-flash-exp",'rank':'op','max_tokens':128000,'schema':{'bos':['<|system|>','<|user|>','<|assistant|>'],'eos':'<|im_end|>'},'ppt':'None'},
    {'type':'text','loc':'google','name':"gemini-exp-1206",'rank':'op','max_tokens':128000,'schema':{'bos':['<|system|>','<|user|>','<|assistant|>'],'eos':'<|im_end|>'},'ppt':'None'},
    {'type':'text','loc':'google','name':"gemini-2.0-flash-thinking-exp-1219",'rank':'op','max_tokens':64000,'schema':{'bos':['<|system|>','<|user|>','<|assistant|>'],'eos':'<|im_end|>'},'ppt':'None'},
    {'type':'text','loc':'google','name':"learnlm-1.5-pro-experimental",'rank':'op','max_tokens':128000,'schema':{'bos':['<|system|>','<|user|>','<|assistant|>'],'eos':'<|im_end|>'},'ppt':'None'},
]
client_gradio=[
    {'type':'text','loc':'gradio','name':'bigscience/bloomz','rank':'op','max_tokens':16384,'schema':{'bos':'<|im_start|>','eos':'<|im_end|>'},'ppt':'None'},
]
client_ollama=[
    {'type':'text','loc':'ollama','name':'hf.co/bartowski/SmallThinker-3B-Preview-GGUF:IQ4_NL','rank':'op','max_tokens':16384,'schema':{'bos':['<|system|>','<|user|>','<|assistant|>'],'eos':'<|im_end|>'},'ppt':'None'},
]
clients_main.extend([{'type':'label','loc':'label','name':"-- Huggingface --",'rank':'','max_tokens':0,'schema':{'bos':'','eos':''},'ppt':'None'}])
clients_main.extend(client_hf)
clients_main.extend([{'type':'label','loc':'label','name':"-- OpenAI --",'rank':'','max_tokens':0,'schema':{'bos':'','eos':''},'ppt':'None'}])
clients_main.extend(client_openai)
clients_main.extend([{'type':'label','loc':'label','name':"-- Google --",'rank':'','max_tokens':0,'schema':{'bos':'','eos':''},'ppt':'None'}])
clients_main.extend(client_google)
clients_main.extend([{'type':'label','loc':'label','name':"-- Gradio --",'rank':'','max_tokens':0,'schema':{'bos':'','eos':''},'ppt':'None'}])
clients_main.extend(client_gradio)
clients_main.extend([{'type':'label','loc':'label','name':"-- Ollama --",'rank':'','max_tokens':0,'schema':{'bos':'','eos':''},'ppt':'None'}])
clients_main.extend(client_ollama)
txt_box=[]
img_box=[]
vis_box=[]
aud_box=[]
for cl in clients_main:
    if cl['type'] == 'label':
        txt_box.append(cl)
        img_box.append(cl)
        vis_box.append(cl)
        aud_box.append(cl)
    elif cl['type'] == 'text':
        txt_box.append(cl)
    elif cl['type'] == 'image':
        img_box.append(cl)
    elif cl['type'] == 'vision':
        vis_box.append(cl)
    elif cl['type'] == 'audio':
        aud_box.append(cl)

clients_out={'txt':txt_box, 'img':img_box, 'vis':vis_box, 'aud':aud_box}

do_it=main.Do_It_All(clients=clients_out)

def load_merm(inp):
    if inp != None:
        outp=do_it.merm_html.replace('**CONTENT**',inp)
        return outp
    else:
        pass
def load_html(inp):
    if inp != None:
        outp=inp
        outp=do_it.merm_html.replace('**CONTENT**',inp)
        return outp
    else:
        pass

def check_ch(inp,inp_val):
    if inp == True and inp_val <= 1:
        value = random.randint(1,9999999999999)
    elif inp == True and inp_val > 1:
        value = do_it.seed_val
    else:
        value=inp_val
    return value
def check_box():
    return True

def upd_collection():
    out = do_it.load_collections()

    return gr.update(choices=out)
def upd_3d_view(rag_col=""):
    do_it.view_collection(rag_col=rag_col)
    return """<div style='height:600px;width:600px;'><iframe src='http://127.0.0.1:5000' height=600 width=600>3d View</iframe></div>"""
add_css="""
#prompt_box textarea{
    color:white;
  }
span.svelte-5ncdh7{
  color:white;
  }
.btn_row {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    }
.new_btn {
    background:#1e293b;
    color:white;
    padding:5px;
    border-radius:10px;
    box-shadow:#fffcfc 0px 0px 5px 2px;
    margin: 5px;
} """
def take_ss(html_str):
    return ss.html_ss(html_str)
def clear_chat_on_load():
    return []
def main():
    with gr.Blocks(head=gs.head,theme=gt.theme,css=add_css+gs.css) as ux:
        gr.HTML(gs.leftbar)
        gr.HTML("""<center><div style='font-family:monospace;font-size:xxx-large;font-weight:900;'>Do-it-All</div><br>
                <div style='font-size:large;font-weight:700;'>Basic AI Agent System</div><br>
                <div style='font-size:large;font-weight:900;'></div><br>
                <div class="btn_row">
                <div class="new_btn">Image</div>
                <div class="new_btn">Documents</div>
                <div class="new_btn">Web Search</div>
                <div class="new_btn">RAG Memory</div>
                </div>
                </center>
                """)
    
        prompt=gr.MultimodalTextbox(label="Prompt", elem_id="prompt_box", file_count="multiple", stop_btn=True, file_types=["image",'.pdf','.txt','.html','.json','.css','.js','.py','.svg'])
        chatbot=gr.Chatbot(label="Chatbot",type='messages',show_label=False, height=800, show_share_button=False, show_copy_button=True, layout="panel")

        with gr.Group(elem_id='gs_left_control_panel'):
            seed_ch=gr.Checkbox(label="Random",value=False)
            seed=gr.Number(label="Seed",step=1,precision=0,value=do_it.seed_val,interactive=True)

            mod_c=gr.Dropdown(label="Chat Model",choices=[n['name'] for n in do_it.txt_clients],value='Qwen/Qwen2.5-Coder-32B-Instruct',type='index')
            mod_im=gr.Dropdown(label="Image Model",choices=[n['name'] for n in do_it.img_clients],value='black-forest-labs/FLUX.1-dev',type='index')
            tok_in=gr.Textbox(label='HF TOKEN', visible=False)

            max_loop=gr.Slider(label="Max loop", minimum=1,maximum=10,value=5,step=1)
            with gr.Row():
                rag_col=gr.Dropdown(label="Collection Name",choices=[],allow_custom_value=True,value='memory',interactive=True)
                with gr.Column():
                    save_mem=gr.Checkbox(label="Save to RAG",value=False)
                    recall_mem=gr.Checkbox(label="Recall from RAG",value=False)
            submit_b = gr.Button()
            stop_b = gr.Button("Stop")
            clear = gr.ClearButton([chatbot])
            ss_btn=gr.Button("Save Image")
        ss_img=gr.Image()
        vector_html=gr.HTML( """<div style='height:600px;width:600px;'></div>""")


        ux.load(check_box,None,seed_ch).then(upd_collection,None,rag_col).then(clear_chat_on_load,None,chatbot)
        #vector_btn.click(upd_3d_view,rag_col,vector_html)
        ss_btn.click(take_ss, chatbot, ss_img)
        seed_ch.change(check_ch,[seed_ch,seed],seed)
        sub_b = submit_b.click(check_ch,[seed_ch,seed],seed).then(do_it.agent, [prompt,chatbot,mod_c,mod_im,tok_in,seed_ch,seed,max_loop,save_mem,recall_mem,rag_col],[chatbot]).then(upd_collection,None,rag_col)
        sub_p = prompt.submit(check_ch,[seed_ch,seed],seed).then(do_it.agent, [prompt,chatbot,mod_c,mod_im,tok_in,seed_ch,seed,max_loop,save_mem,recall_mem,rag_col],[chatbot]).then(upd_collection,None,rag_col)
        
        stop_b.click(None,None,None, cancels=[sub_b,sub_p])
    ux.queue(default_concurrency_limit=20).launch(max_threads=40)
if __name__ == '__main__':
    main()
