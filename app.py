import gradio as gr
import whisper
import os
import subprocess

# Ajouter le dossier ffmpeg au PATH
ffmpeg_dir = r"C:\Users\PC\Documents\s2-master\projet3-ml\ffmpeg\ffmpeg-7.1.1-full_build\bin"
os.environ["PATH"] += os.pathsep + ffmpeg_dir

# Vérifier que ffmpeg est accessible
try:
    result = subprocess.run(["ffmpeg", "-version"], check=True, capture_output=True, text=True)
    print("ffmpeg est disponible :\n", result.stdout)
except FileNotFoundError:
    print("ffmpeg non trouvé via subprocess.")

# Charger le modèle Whisper
model = whisper.load_model("base")

def transcrire(audio_path):
    if audio_path is None or not os.path.exists(audio_path):
        return "Aucun fichier audio valide fourni."
    result = model.transcribe(audio_path)
    return result["text"]

iface = gr.Interface(
    fn=transcrire,
    inputs=gr.Audio(type="filepath"),
    outputs="text",
    title="Transcripteur Audio avec Whisper",
    description="Téléversez un fichier audio (WAV, MP3, etc.) pour obtenir sa transcription."
)

iface.launch()
