import os
import openai
import wget
import streamlit as st
from PIL import Image
from serpapi import GoogleSearch
import torch
from diffusers import StableDiffusionPipeline
from bokeh.models.widgets import Button
from bokeh.models.widgets.buttons import Button
from bokeh.models import CustomJS
from streamlit_bokeh_events import streamlit_bokeh_events
import base64
from streamlit_player import st_player
from pytube import YouTube
from pytube import Search
import io
import warnings
from PIL import Image
from stability_sdk import client
import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation
from datetime import datetime
from google.oauth2 import service_account
from googleapiclient.discovery import build
import wget
import urllib.request


def save_uploadedfile(uploadedfile):
    with open(uploadedfile.name,"wb") as f:
        f.write(uploadedfile.getbuffer())

stability_api = client.StabilityInference(
    key=st.secrets["STABILITY_KEY"], #os.environ("STABILITY_KEY"), # key=os.environ['STABILITY_KEY'], # API Key reference.
    verbose=True, # Print debug messages.
    engine="stable-diffusion-v1-5", # Set the engine to use for generation.
    # Available engines: stable-diffusion-v1 stable-diffusion-v1-5 stable-diffusion-512-v2-0 stable-diffusion-768-v2-0
    # stable-diffusion-512-v2-1 stable-diffusion-768-v2-1 stable-inpainting-v1-0 stable-inpainting-512-v2-0
)

def search_internet(question):
    try:    
        params = {
            "q": question,
            "location": "Bengaluru, Karnataka, India",
            "hl": "hi",
            "gl": "in",
            "google_domain": "google.co.in",
            # "api_key": ""
            "api_key": st.secrets["GOOGLE_API"] #os.environ("GOOGLE_API") #os.environ['GOOGLE_API']
        }
    
        params = {
            "q": question,
            "location": "Bengaluru, Karnataka, India",
            "hl": "hi",
            "gl": "in",
            "google_domain": "google.co.in",
            # "api_key": ""
            "api_key": st.secrets["GOOGLE_API"] #os.environ("GOOGLE_API") #os.environ['GOOGLE_API']
        }
    
        search = GoogleSearch(params)
        results = search.get_dict()
        organic_results = results["organic_results"]
      
    
        snippets = ""
        counter = 1
        for item in organic_results:
            snippets += str(counter) + ". " + item.get("snippet", "") + '\n' + item['about_this_result']['source']['source_info_link'] + '\n'
            counter += 1
    
        # snippets
    
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=f'''following are snippets from google search with these as knowledge base only answer questions and print  reference link as well followed by answer. \n\n {snippets}\n\n question-{question}\n\nAnswer-''',
            temperature=0.49,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0)
    
        string_temp = response.choices[0].text
        st.write(string_temp)
        st.write(snippets)
    except:
        try:
            params = {
                "q": question,
                "location": "Bengaluru, Karnataka, India",
                "hl": "hi",
                "gl": "in",
                "google_domain": "google.co.in",
                # "api_key": ""
                "api_key": st.secrets["GOOGLE_API1"] #os.environ("GOOGLE_API") #os.environ['GOOGLE_API']
            }
        
            params = {
                "q": question,
                "location": "Bengaluru, Karnataka, India",
                "hl": "hi",
                "gl": "in",
                "google_domain": "google.co.in",
                # "api_key": ""
                "api_key": st.secrets["GOOGLE_API1"] #os.environ("GOOGLE_API") #os.environ['GOOGLE_API']
            }
        
            search = GoogleSearch(params)
            results = search.get_dict()
            organic_results = results["organic_results"]
          
        
            snippets = ""
            counter = 1
            for item in organic_results:
                snippets += str(counter) + ". " + item.get("snippet", "") + '\n' + item['about_this_result']['source']['source_info_link'] + '\n'
                counter += 1
        
            # snippets
        
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=f'''following are snippets from google search with these as knowledge base only answer questions and print  reference link as well followed by answer. \n\n {snippets}\n\n question-{question}\n\nAnswer-''',
                temperature=0.49,
                max_tokens=256,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0)
        
            string_temp = response.choices[0].text
            st.write(string_temp)
            st.write(snippets)
        except:
            params = {
            "q": question,
            "location": "Bengaluru, Karnataka, India",
            "hl": "hi",
            "gl": "in",
            "google_domain": "google.co.in",
            # "api_key": ""
            "api_key": st.secrets["GOOGLE_API2"] #os.environ("GOOGLE_API") #os.environ['GOOGLE_API']
            }
        
            params = {
                "q": question,
                "location": "Bengaluru, Karnataka, India",
                "hl": "hi",
                "gl": "in",
                "google_domain": "google.co.in",
                # "api_key": ""
                "api_key": st.secrets["GOOGLE_API2"] #os.environ("GOOGLE_API") #os.environ['GOOGLE_API']
            }
        
            search = GoogleSearch(params)
            results = search.get_dict()
            organic_results = results["organic_results"]
          
        
            snippets = ""
            counter = 1
            for item in organic_results:
                snippets += str(counter) + ". " + item.get("snippet", "") + '\n' + item['about_this_result']['source']['source_info_link'] + '\n'
                counter += 1
        
            # snippets
        
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=f'''following are snippets from google search with these as knowledge base only answer questions and print  reference link as well followed by answer. \n\n {snippets}\n\n question-{question}\n\nAnswer-''',
                temperature=0.49,
                max_tokens=256,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0)
        
            string_temp = response.choices[0].text
            st.write(string_temp)
            st.write(snippets)
        

# openai.api_key = ""
openai.api_key = st.secrets["OPENAI_KEY"] #os.environ("OPENAI_KEY") #os.environ['OPENAI_KEY']
date_time = str(datetime.now())

# dictionary = st.secrets("GSHEET_KEY")
# json_object = json.dumps(dictionary, indent=4)

def g_sheet_log(myinput, output):
  SERVICE_ACCOUNT_FILE = 'gsheet.json'

  credentials = service_account.Credentials.from_service_account_file(
      filename=SERVICE_ACCOUNT_FILE
  )

  service_sheets = build('sheets', 'v4', credentials=credentials)

  GOOGLE_SHEETS_ID = '16cM8lHm7n_X0ZVLgWfL5fcBhvKWIGO9LQz3zCl2Dn_8'
  worksheet_name = 'Prompt_Logs!'
  cell_range_insert = 'A:C'

  values = (
      (myinput, output, date_time),
  )

  value_range_body = {
      'majorDimension' : 'ROWS',
      'values' : values
  }

  service_sheets.spreadsheets().values().append(
      spreadsheetId=GOOGLE_SHEETS_ID,
      valueInputOption='USER_ENTERED',
      range=worksheet_name + cell_range_insert,
      body=value_range_body
  ).execute()

openai.api_key = st.secrets["OPENAI_KEY"]

def openai_response(PROMPT):
    response = openai.Image.create(
    prompt=PROMPT,
    n=1,
    size="256x256",
)
    return response["data"][0]["url"]

st.title("Hi! :red[HyperBot] here!!🤖⭐️")
st.title("Go on ask me anything!!")

st.write('''
⭐️ *HyperBot is your virtual assistant powered by Whisper / 
chatgpt / internet / Dall-E / OpenAI embeddings - the perfect 
companion for you. With HyperBot, you can ask anything you ask 
internet everyday . Get answers to questions about the weather, 
stocks 📈, news📰, and more! Plus, you can also generate 🖌️ 
paintings, drawings, abstract art 🎨, play music 🎵 or videos, 
create tweets 🐦 and posts 📝, and compose emails 📧 - all with 
the help of HyperBot!* 🤖 ✨
''')

st.text('''You can ask me: 
1. All the things you ask ChatGPT.
2. To generate paintings, drawings, abstract art. 
3. Music or Videos
4. Weather 
5. Stocks 
6. Current Affairs and News.
7. Create or compose tweets or Linkedin posts or email.''')

Input_type = st.radio(
    "**Input type:**",
    ('TEXT', 'SPEECH')
    )

if Input_type == 'TEXT':
    st.write('**You are now in Text input mode**')
    mytext = st.text_input('**Go on! Ask me anything:**')
    if st.button("SUBMIT"):
        question=mytext
        response = openai.Completion.create(
          model="text-davinci-003",
          prompt=f'''Your name is HyperBot and  knowledge cutoff date is 2021-09, and you are not aware of any events after that time. if the  
                    Answer to following questions is not from your knowledge base or in case of queries like weather 
                      updates / stock updates / current news or people which requires you to have internet connection  then print i don't have access to internet to answer your question, 
                      if  question is related to  image or  painting or drawing generation then print ipython type output function gen_draw("detailed prompt of image to be generated")
                      if the question is related to playing a song or video or music of a singer then print ipython type output  function vid_tube("relevent search query")
                      if the question is related to operating home appliances then print ipython type output function home_app(" action(ON/Off),appliance(TV,Geaser,Fridge,Lights,fans,AC)") . 
                      if question is realted to sending mail or sms then print ipython type output function messenger_app(" message of us ,messenger(email,sms)")
                      \nQuestion-{question}
                      \nAnswer -''',
          temperature=0.49,
          max_tokens=256,
          top_p=1,
          frequency_penalty=0,
          presence_penalty=0
        )
        string_temp=response.choices[0].text

        if ("gen_draw" in string_temp):
            try:
                try:
                    wget.download(openai_response(prompt))
                    img2 = Image.open(wget.download(openai_response(prompt)))
                    img2.show()
                    rx = 'Image returned'
                    g_sheet_log(mytext, rx)
                except:
                    urllib.request.urlretrieve(openai_response(prompt),"img_ret.png")
                    img = Image.open("img_ret.png")
                    img.show()
                    rx = 'Image returned'
                    g_sheet_log(mytext, rx)
            except:
                # Set up our initial generation parameters.
                answers = stability_api.generate(
                prompt = mytext,
                seed=992446758, # If a seed is provided, the resulting generated image will be deterministic.
                        # What this means is that as long as all generation parameters remain the same, you can always recall the same image simply by generating it again.
                        # Note: This isn't quite the case for Clip Guided generations, which we'll tackle in a future example notebook.
                steps=30, # Amount of inference steps performed on image generation. Defaults to 30.
                cfg_scale=8.0, # Influences how strongly your generation is guided to match your prompt.
                    # Setting this value higher increases the strength in which it tries to match your prompt.
                    # Defaults to 7.0 if not specified.
                width=512, # Generation width, defaults to 512 if not included.
                height=512, # Generation height, defaults to 512 if not included.
                samples=1, # Number of images to generate, defaults to 1 if not included.
                sampler=generation.SAMPLER_K_DPMPP_2M # Choose which sampler we want to denoise our generation with.
                                                    # Defaults to k_dpmpp_2m if not specified. Clip Guidance only supports ancestral samplers.
                                                    # (Available Samplers: ddim, plms, k_euler, k_euler_ancestral, k_heun, k_dpm_2, k_dpm_2_ancestral, k_dpmpp_2s_ancestral, k_lms, k_dpmpp_2m)
                )

                # Set up our warning to print to the console if the adult content classifier is tripped.
                # If adult content classifier is not tripped, save generated images.
                for resp in answers:
                    for artifact in resp.artifacts:
                        if artifact.finish_reason == generation.FILTER:
                            warnings.warn(
                                "Your request activated the API's safety filters and could not be processed."
                                "Please modify the prompt and try again.")
                        if artifact.type == generation.ARTIFACT_IMAGE:
                            img = Image.open(io.BytesIO(artifact.binary))
                            st.image(img)
                            img.save(str(artifact.seed)+ ".png") # Save our generated images with their seed number as the filename.
                            rx = 'Image returned'
                            g_sheet_log(mytext, rx)
                            
            # except:        
            #     st.write('image is being generated please wait...')
            #     def extract_image_description(input_string):
            #         return input_string.split('gen_draw("')[1].split('")')[0]
            #     prompt=extract_image_description(string_temp)
            #     # model_id = "CompVis/stable-diffusion-v1-4"
            #     model_id='runwayml/stable-diffusion-v1-5'
            #     device = "cuda"


            #     pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
            #     pipe = pipe.to(device)

            #     # prompt = "a photo of an astronaut riding a horse on mars"
            #     image = pipe(prompt).images[0]  
                
            #     image.save("astronaut_rides_horse.png")
            #     st.image(image)
            #     # image

        elif ("vid_tube" in string_temp):
            s = Search(mytext)
            search_res = s.results
            first_vid = search_res[0]
            print(first_vid)
            string = str(first_vid)
            video_id = string[string.index('=') + 1:-1]
            # print(video_id)
            YoutubeURL = "https://www.youtube.com/watch?v="
            OurURL = YoutubeURL + video_id
            st.write(OurURL)
            st_player(OurURL)
            ry = 'Youtube link and video returned'
            g_sheet_log(mytext, ry)

        elif ("don't" in string_temp or "internet" in string_temp):
            st.write('searching internet ')
            search_internet(question)
            rz = 'Internet result returned'
            g_sheet_log(mytext, string_temp)

        else:
            st.write(string_temp)
            g_sheet_log(mytext, string_temp)

elif Input_type == 'SPEECH':
    option_speech = st.selectbox(
    'Choose from below: (Options for Transcription)',
    ('Use Microphone', 'OpenAI Whisper (Upload audio file)')
    )

    if option_speech == 'Use Microphone':
        stt_button = Button(label="Speak", width=100)
        stt_button.js_on_event("button_click", CustomJS(code="""
            var recognition = new webkitSpeechRecognition();
            recognition.continuous = true;
            recognition.interimResults = true;
         
            recognition.onresult = function (e) {
                var value = "";
                for (var i = e.resultIndex; i < e.results.length; ++i) {
                    if (e.results[i].isFinal) {
                        value += e.results[i][0].transcript;
                    }
                }
                if ( value != "") {
                    document.dispatchEvent(new CustomEvent("GET_TEXT", {detail: value}));
                }
            }
            recognition.start();
            """))
        
        result = streamlit_bokeh_events(
            stt_button,
            events="GET_TEXT",
            key="listen",
            refresh_on_update=False,
            override_height=75,
            debounce_time=0)
        
        if result:
            if "GET_TEXT" in result:
                question = result.get("GET_TEXT")
                response = openai.Completion.create(
                model="text-davinci-003",
                prompt=f'''Your knowledge cutoff is 2021-09, and it is not aware of any events after that time. if the  
                          Answer to following questions is not  from your knowledge base or in case of queries like weather 
                            updates / stock updates / current news Etc which requires you to have internet connection  then print i don't have access to internet to answer your question, 
                            if  question is related to  image or  painting or drawing generation then print ipython type output   function gen_draw("detailed prompt of image to be generated")
                            if the question is related to playing a song or video or music of a singer then print ipython type output  function vid_tube("relevent search query")
                            \nQuestion-{question}
                            \nAnswer -''',
                temperature=0.49,
                max_tokens=256,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
                )
                string_temp=response.choices[0].text
    
                if ("gen_draw" in string_temp):
                    st.write('*image is being generated please wait..* ')
                    def extract_image_description(input_string):
                        return input_string.split('gen_draw("')[1].split('")')[0]
                    prompt=extract_image_description(string_temp)
                    # model_id = "CompVis/stable-diffusion-v1-4"
                    model_id='runwayml/stable-diffusion-v1-5'
                    device = "cuda"
    
                    pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
                    pipe = pipe.to(device)
    
                    # prompt = "a photo of an astronaut riding a horse on mars"
                    image = pipe(prompt).images[0]  
                      
                    image.save("astronaut_rides_horse.png")
                    st.image(image)
                    # image 
                
                elif ("vid_tube" in string_temp):
                    s = Search(question)
                    search_res = s.results
                    first_vid = search_res[0]
                    print(first_vid)
                    string = str(first_vid)
                    video_id = string[string.index('=') + 1:-1]
                    # print(video_id)
                    YoutubeURL = "https://www.youtube.com/watch?v="
                    OurURL = YoutubeURL + video_id
                    st.write(OurURL)
                    st_player(OurURL)
    
                elif ("don't" in string_temp or "internet" in string_temp  ):
                    st.write('*searching internet*')
                    search_internet(question)
                else:
                    st.write(string_temp)

    elif option_speech == 'OpenAI Whisper (Upload audio file)':
        audio_file = st.file_uploader("Upload Audio file",type=['wav', 'mp3'])
        if audio_file is not None:
            # file = open(audio_file, "rb")
            st.audio(audio_file)
            transcription = openai.Audio.transcribe("whisper-1", audio_file)
            st.write(transcription["text"])
            result = transcription["text"]
            question = result
            response = openai.Completion.create(
            model="text-davinci-003",
            prompt=f'''Your knowledge cutoff is 2021-09, and it is not aware of any events after that time. if the  
                      Answer to following questions is not  from your knowledge base or in case of queries like weather 
                        updates / stock updates / current news Etc which requires you to have internet connection  then print i don't have access to internet to answer your question, 
                        if  question is related to  image or  painting or drawing generation then print ipython type output   function gen_draw("detailed prompt of image to be generated")
                        if the question is related to playing a song or video or music of a singer then print ipython type output  function vid_tube("relevent search query")
                        \nQuestion-{question}
                        \nAnswer -''',
            temperature=0.49,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
            )
            
            string_temp=response.choices[0].text

            if ("gen_draw" in string_temp):
                st.write('*image is being generated please wait..* ')
                def extract_image_description(input_string):
                    return input_string.split('gen_draw("')[1].split('")')[0]
                prompt=extract_image_description(string_temp)
                # model_id = "CompVis/stable-diffusion-v1-4"
                model_id='runwayml/stable-diffusion-v1-5'
                device = "cuda"

                pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
                pipe = pipe.to(device)

                # prompt = "a photo of an astronaut riding a horse on mars"
                image = pipe(prompt).images[0]  
                  
                image.save("astronaut_rides_horse.png")
                st.image(image)
                # image 
            
            elif ("vid_tube" in string_temp):
                s = Search(question)
                search_res = s.results
                first_vid = search_res[0]
                print(first_vid)
                string = str(first_vid)
                video_id = string[string.index('=') + 1:-1]
                # print(video_id)
                YoutubeURL = "https://www.youtube.com/watch?v="
                OurURL = YoutubeURL + video_id
                st.write(OurURL)
                st_player(OurURL)

            elif ("don't" in string_temp or "internet" in string_temp  ):
                st.write('*searching internet*')
                search_internet(question)
            else:
                st.write(string_temp)
else:
    pass
