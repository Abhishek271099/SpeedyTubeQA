# YouTube Chatbot

## Overview
This Python project implements a chatbot that operates on YouTube video links. The chatbot's main functionality is to download the audio from the provided video link, convert it to text using OpenAI's Whisper model, and then generate responses to questions related to the content of the video using a Retrieve and Generate (RAG) approach. The aim of this project is to provide users with a quick way to get answers from very long videos on YouTube, eliminating the need to watch the entire video.

## Features
* YouTube Link Processing: Accepts YouTube video links as input.
* Audio Extraction: Downloads audio from the provided YouTube video link.
* Text Generation: Generates responses to questions based on the content of the video with Google's gemini-pro model.
* RAG Implementation: Implements a simple RAG approach without utilizing any external libraries.
* Cosine Similarity: Utilizes cosine similarity to match questions with relevant chunks of text from the video transcript.
* Quick Sort Algorithm: Sorts similarities for efficient retrieval.

## How it Works
1) Input: User provides a link to a YouTube video.
2) Audio Extraction: The chatbot downloads the audio from the video.
3) Transcription: The audio is transcribed into text using OpenAI's Whisper model.
4) Question Processing: When a question is asked, the chatbot processes it.
5) Text Chunk Matching: The chatbot matches the question with relevant chunks of text from the video transcript using cosine similarity.
6) Response Generation: If a match is found above a certain threshold, the corresponding text chunk is used to generate a response using a Language Model (LLM).
7) Response Presentation: The generated response is presented to the user.

## Installation
1) Clone this repository: git clone https://github.com/Abhishek271099/SpeedyTubeQA.git
2) Navigate to the project directory: cd SpeedyTubeQA
3) Install dependencies: pip install -r requirements.txt
4) create .env file and add these environment variables to it  <br />
    a- GENAI_API_KEY = "YOUR-GEMINI-APIKEY"  <br />
    b- EMB_MODEL_NAME = "models/embedding-001"   <br />
    c- RESPONSE_MODEL_NAME = "gemini-pro"  <br />
5) Run the command in termial  <br />
    uvicorn main:app --reload   ---> dev environment  <br />
    uvicorn main:app            ---> prod environment