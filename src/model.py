import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

GENAI_API_KEY = os.getenv("GENAI_API_KEY")
RESPONSE_MODEL = os.getenv("RESPONSE_MODEL_NAME")
EMB_MODEL = os.getenv("EMB_MODEL_NAME")

genai.configure(api_key=GENAI_API_KEY)

class Chatbot:

    def __init__(self, model_name=RESPONSE_MODEL, emb_model_name=EMB_MODEL):
        self.model = genai.GenerativeModel(model_name)
        self.emb_model_name = emb_model_name

    def get_response(self, question, context):
        prompt = """Your are question answering chatbot. You will be provided with chunk of transcribe text from Youtube Video.
                    An question will be asked on that context. If the context does not have the answer for the question asked,
                    just say \'I don\'t know\'. 
                    Do not come up with your own answer.
                    Context: """
        feed = prompt + context + "\n" + "Question: " + question
        print("feed:", feed)
        response = self.model.generate_content(feed)
        return response.text

    def get_embedding(self, text):
        return genai.embed_content(model=self.emb_model_name, content=text)['embedding']