import os
import whisper

os.environ["PATH"] += os.pathsep + r"C:\Users\PC\Documents\s2-master\projet3-ml\ffmpeg\ffmpeg-7.1.1-full_build\bin"  # modifie ici selon ton installation

model = whisper.load_model("base")

audio_path = r"C:\Users\PC\AppData\Local\Temp\gradio\d32914a9d3de67e6fe96a18d42770a06a0aee34735345f6afde825457e5a9a97\data\exemple_audio_fr.mp3"

result = model.transcribe(audio_path)
print(result["text"])
