from langchain.text_splitter import RecursiveCharacterTextSplitter
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

GENAI_API_KEY = os.getenv("GENAI_API_KEY")
EMB_MODEL_NAME = os.getenv("EMB_MODEL_NAME")
genai.configure(api_key=GENAI_API_KEY)

def split_texts(text):
    splitter = RecursiveCharacterTextSplitter(
                    chunk_size = 1500,
                    chunk_overlap = 100,
                    separators = [" ", "\n", "\n\n"],
                    length_function = len
    )
    texts = splitter.split_text(text=text)
    return texts


def get_embedding(texts):
    return [genai.embed_content(model=EMB_MODEL_NAME, content=text)["embedding"] for text in texts]