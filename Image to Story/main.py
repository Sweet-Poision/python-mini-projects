from langchain.llms import OpenAI
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.memory import ConversationBufferMemory
from customtkinter import *
import os

os.environ["SCENEX_API_KEY"] = "API_KEY_HERE"
OPEN_AI_KEY = "API_KEY_HERE" 

def speak_story(story):
    system_string = "say '" + story + "' &"
    os.system(system_string)

def getStory():
    global input_field_url
    global input_field_type
    global OPEN_AI_KEY
    img_url = input_field_url.get().lower()
    story_type = input_field_type.get().lower()
    if story_type == "" :
        story_type = "random"
    print(img_url)
    myllm = OpenAI(
        model = 'text-davinci-003',
        temperature = 1,
        openai_api_key = OPEN_AI_KEY
    )
    mytool = load_tools(tool_names=["sceneXplain"])
    mymemory = ConversationBufferMemory(memory_key="chat_history")
    myagent = initialize_agent(
        llm = myllm,
        memory = mymemory,
        tools = mytool,
        agent = "conversational-react-description",
        verbose = True
    )
    prompt_text = "make a" + story_type + "story about the image " + img_url + " in about 20 words"
    story = myagent.run(prompt_text)
    speak_story(story)


# Creating Window
set_appearance_mode("light")
app = CTk()
app.resizable(None, None)
app.title("Image to Story")
app.geometry("500x450")

input_field_url = CTkEntry(master=app, width=400)

input_field_type = CTkEntry(master=app, width=400)

heading_label = CTkLabel(
    master=app,
    text="Generate Story from Image using AI",
    font=("Helvetica", 20),
    text_color="#000000",        
)

body_url_label = CTkLabel(
    master=app,
    text="Enter image URL",
)

body_type_label = CTkLabel(
    master=app,
    text="Enter story type (example - epic, dramatic, romatice, tragic, etc..)",
)

generate_button = CTkButton(
    master = app,
    text = "Generate Story",
    corner_radius=32,
    fg_color="#C850C0",
    hover_color="#4158D0",
    command=getStory,
)

heading_label.pack(pady=30)
body_url_label.pack(pady=20)
input_field_url.pack(pady=10)
body_type_label.pack(pady=20)
input_field_type.pack(pady=10)
generate_button.pack(pady=10)

app.mainloop()