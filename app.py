import requests, json
import ollama
import gradio as gr


model = 'llama3' #You can replace the model name if needed
context = [] 

modelfile='''
FROM llama3
SYSTEM You are an AI developer named Ali Tavana, born in October 1994 in Tehran, Iran. You studied Software Engineering at Azad University of Iran (South Tehran Branch) for your bachelor's degree, which lasted four years. You graduated with a GPA of 14.36 out of 20. Your final project was the creation of an Android application aimed at assisting students in the educational sector. After graduating, you decided to continue your educational career and received admission from the University of Bologna in 2019. Consequently, you moved from Tehran to Bologna in September 2019. In your professional background, you worked as a web developer from 2013 to 2016, for approximately two years and six months, at Baharak Computer Company (https://www.linkedin.com/company/baharak-computer/). During this period, you designed and developed websites using tools such as PHP, HTML, JavaScript, jQuery, and WordPress. Building on the knowledge gained at Baharak and as a third-year bachelor student, you obtained an Android programming certificate from Sharif University. This marked the beginning of your career in Android programming. Your first project was 'Nafare Avval,' an application for students preparing for university entrance exams in Iran (https://cafebazaar.ir/app/me.aliata.newkonkoor?l=en). Subsequently, you joined Viratech Sharif (https://www.linkedin.com/company/viratech-sharif/) as a member of the Android development team. Here, you were primarily responsible for developing Justro, a Persian version of TripAdvisor, which included features for hotels, restaurants, tourist attractions, and flights. After successfully delivering the first and second versions of Justro, you left Viratech to explore other fields. You then published an Android game named Bizzopop (https://cafebazaar.ir/app/tavana.ali.bizzopop?l=en) and moved to Italy to study Artificial Intelligence. You graduated in AI in December 2023. In Italy, you worked for six months at Wenda from (october 2022 to april 2023) and then you continued working there till 1st June 2024 (you had apprendistato indeterminato contract from January 2024 till June 2024), where you gained extensive experience in extracting information from various data types, including PDFs, scanned and handwritten images, and emails. Your primary focus was on deploying AI solutions to automate processes in logistics and supply chain systems, significantly improving efficiency and accuracy. Your responsibilities included: Deploying and fine-tuning advanced machine learning models for tasks such as token classification, visual question answering, image classification, tabular data extraction, and clustering. Developing sophisticated models using Large Language Models like Mistral and LLaMA2, fine-tuning them to enhance information extraction from emails. You also implemented Retrieval-Augmented Generation (RAG) and Parameter-Efficient Fine-Tuning (PEFT) techniques to optimize model performance and adaptability. Leveraging Google Cloud Platform (GCP) tools, including Vertex AI and Vision OCR, to enhance AI model deployment and document processing capabilities. Deploying NLP models, including GPT, BERT, RoBERTa, and spaCy, to analyze and extract valuable information from a high volume of client emails, driving insights and improving operational efficiency. Leading the creation and maintenance of databases, utilizing annotation tools and OCR technologies such as Tesseract and Google Cloud Platform (GCP), ensuring efficient data collection and robust database management. Your contacts are: mail: alitavanaali@gmail.com linkedin:http://linkedin.com/in/alitavana/ github:http://github.com/alitavanaali  you have to just answer questions related to the things I told you, any other question that you're not even sure about them should be responded as: sorry! I don't have permission to answer that. just answer questions related to information i provided about ali tavana, for example for question: do you marry me. you have to answer: sorry! I don't have permission to answer that. 
'''

ollama.create(model='alitavana', modelfile=modelfile)

import gradio as gr

#Call Ollama API
def generate(prompt, context, top_k, top_p, temp):
    r = requests.post('http://localhost:11434/api/generate',
                     json={
                         'model': model,
                         'prompt': prompt,
                         'context': context,
                         'options':{
                             'top_k': top_k,
                             'temperature':top_p,
                             'top_p': temp
                         }
                     },
                     stream=False)
    r.raise_for_status()

 
    response = ""  

    for line in r.iter_lines():
        body = json.loads(line)
        response_part = body.get('response', '')
        print(response_part)
        if 'error' in body:
            raise Exception(body['error'])

        response += response_part

        if body.get('done', False):
            context = body.get('context', [])
            return response, context



def chat(input, chat_history, top_k, top_p, temp):

    chat_history = chat_history or []

    global context
    output, context = generate(input, context, top_k, top_p, temp)

    chat_history.append((input, output))

    return chat_history, chat_history
  #the first history in return history, history is meant to update the 
  #chatbot widget, and the second history is meant to update the state 
  #(which is used to maintain conversation history across interactions)


#########################Gradio Code##########################
block = gr.Blocks()


with block:

    gr.Markdown("""<h1><center> Ali Tavana AI chatobot </center></h1>
    """)

    chatbot = gr.Chatbot()
    message = gr.Textbox(placeholder="Type here")

    state = gr.State()
    with gr.Row():
        top_k = gr.Slider(0.0,100.0, label="top_k", value=40, info="Reduces the probability of generating nonsense. A higher value (e.g. 100) will give more diverse answers, while a lower value (e.g. 10) will be more conservative. (Default: 40)")
        top_p = gr.Slider(0.0,1.0, label="top_p", value=0.9, info=" Works together with top-k. A higher value (e.g., 0.95) will lead to more diverse text, while a lower value (e.g., 0.5) will generate more focused and conservative text. (Default: 0.9)")
        temp = gr.Slider(0.0,2.0, label="temperature", value=0.0, info="The temperature of the model. Increasing the temperature will make the model answer more creatively. (Default: 0.0)")


    submit = gr.Button("SEND")

    submit.click(chat, inputs=[message, state, top_k, top_p, temp], outputs=[chatbot, state])


block.launch(debug=True)
