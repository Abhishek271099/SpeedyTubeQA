from fastapi import FastAPI, status, HTTPException
from src import model, rag, schemas, youtube, processing
import os

app = FastAPI()

@app.get("/")
def home_page():
    return {"message": "Hello"}



@app.post("/response")
def generate_response(data: schemas.InputSchema):
    question = data.question
    if not (data.youtube_link or os.listdir('text')):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Please provide link to youtube video")
    
    if not os.listdir('text'):     
        print('downloading transcribe')       
        youtube_link = data.youtube_link
        try:
            text = youtube.download_audio(youtube_link)

        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail=f"Failed with error: {e}")
    else:
        directory = os.path.join(os.getcwd(), 'text')
        path = os.path.join(directory, os.listdir(directory)[0])
        with open(path, 'r') as f:
            text = f.read()
        
    texts = processing.split_texts(text)
    embeddings = processing.get_embedding(texts)

    simplerag = rag.SimpleRAG(texts = texts,
                              embeddings = embeddings)
    
    chatbot = model.Chatbot()
    question_emb = chatbot.get_embedding(question)

    relevant_texts = simplerag.selectTopK(question_emb, 3)
    context = ""

    for text in relevant_texts:
        context += text + "\n"

    response = chatbot.get_response(question, context)
    print("response: ", response)
    return {'response': response}

