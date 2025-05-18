# 🎙️ Transcription Audio avec Whisper

## 🎯 Objectif
Ce projet permet de **convertir un fichier audio (MP3, WAV, etc.) en texte** à l’aide du modèle **Whisper** d’OpenAI, à travers une interface web intuitive développée avec **Gradio**.

---

## 🧰 Technologies utilisées

| Outil        | Description                                |
|--------------|--------------------------------------------|
| 🐍 Python     | Version Python 3.11.0                    |
| 🧠 Whisper    | Modèle de reconnaissance vocale d’OpenAI   |
| 🌐 Gradio    | Interface web pour lancer facilement l'outil |
| 🎵 FFmpeg    | Pour le traitement des fichiers audio       |

---

## 📦 Prérequis

Assurez-vous d’avoir installé :

- [Python Python 3.11.0](https://www.python.org/downloads/)
- [FFmpeg](https://ffmpeg.org/download.html) (et ajouté à la variable d’environnement `PATH`)
- `pip` (installateur de paquets Python)

---

## 🚀 Installation et lancement du projet

### 1. Cloner le dépôt

bash
git clone https://github.com/hindelmouden/Transcription_Audio_To_Text.git
cd Transcription_Audio_To_Text

---

### 2. Créer un environnement virtuel (recommandé)

python -m venv venv
`source venv/bin/activate   # Sous macOS/Linux`
`venv\Scripts\activate      # Sous Windows`
