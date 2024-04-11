from pytube import YouTube
import whisper
import os

whisper_model = whisper.load_model("base")

def download_audio(link):
    yt = YouTube(link)
    audio = yt.streams.filter(only_audio=True).first()
    file = audio.download(output_path=os.path.join(os.getcwd(), "text"))
    transcription = whisper_model.transcribe(file, fp16=False)["text"].strip()
    file_path = os.path.join(os.path.join(os.getcwd(), "text"), "transcribe.txt")
    with open(file_path, "w") as f:
        f.write(transcription)

    return transcription
