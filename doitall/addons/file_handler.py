from pypdf import PdfReader
from io import BytesIO
import requests
import random
import json
import os

def compress_data(self,c,purpose, history,mod,tok,seed,data):
    resp=[None,]
    #if not data: data=[];data[0]="NONE"
    seed=random.randint(1,1000000000)
    divr=int(c)/self.MAX_HISTORY
    divi=int(divr)+1 if divr != int(divr) else int(divr)
    chunk = int(int(c)/divr)
    task1="refine this data"
    out = []
    #out=""
    s=0
    e=chunk
    new_history=""
    task = f'Compile this data to fulfill the task: {task1}, and complete the purpose: {purpose}\n'
    for z in range(divi):
        data[0]=new_history
        hist = history[s:e]
        resp = self.generate(
            prompt=purpose,
            history=hist,
            mod=int(mod),
            tok=int(tok),
            seed=int(seed),
            role='COMPRESS',
            data=data,
        )
        resp_o = list(resp)[0]
        new_history = resp_o
        out+=resp_o
        e=e+chunk
        s=s+chunk
    
    #history = [{'role':'system','content':'Compressed History: ' + str(resp_o)}]
    return str(resp_o)

def read_pdf(pdf_path):
    if not os.path.isdir("./images"):
        os.mkdir("./images")
    text=[]
    images = ""
    reader = PdfReader(pdf_path)
    number_of_pages = len(reader.pages)
    file_name=str(pdf_path).split("\\")[-1]
    for i in range(number_of_pages):
        page = reader.pages[i]
        images=""
        if len(page.images) >0:
            for count, image_file_object in enumerate(page.images):
                with open( "./images/" + str(count) + image_file_object.name, "wb") as fp:
                    fp.write(image_file_object.data)
                #buffer = io.BytesIO(image_file_object.data)
                #images.append({"name":file_name,"page":i,"cnt":count,"image":Image.open(buffer)})
                #images.append(str(image_file_object.data))
                fp.close()
                images += "./images/" + str(count) + image_file_object.name + "\n"
        else:
            images=""
        text.append({"page":i,"text":page.extract_text(),"images":images})
    return text

def download_pdf_to_bytesio(url):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        buffer = BytesIO(response.content)
        
        pdf_json=read_pdf(buffer)
        print(pdf_json)
        return pdf_json
    else:
        raise Exception(f"Failed to download PDF: Status code {response.status_code}")

MAX_HISTORY=15000
def read_file(file_path):
    file_box=[]

    if str(file_path).endswith(('.txt','.html','.json','.css','.js','.py','.svg')):
        with open(str(file_path), "r") as file:
            file_box.extend([{'doc_name':file_path,'content':file.read()}])
            file.close()
    elif str(file_path).endswith(('.pdf')):
        pdf_json=read_pdf(str(file_path))
        file_box.extend([{'doc_name':file_path,'content':'PDF_CONTENT'+json.dumps(pdf_json,indent=1)}])    
    #if len(str(file_box)) > MAX_HISTORY:
    #    file_out = compress_data(len(str(file_box)),prompt, str(file_box),mod,10000,seed,in_data)
    #else: file_out=str(file_box)
    return str(file_box)
