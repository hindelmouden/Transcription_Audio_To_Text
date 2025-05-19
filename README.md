# 🎙️ Transcription Audio avec Whisper

## 🎯 Objectif
Ce projet permet de **convertir un fichier audio (MP3, WAV, etc.) en texte** à l’aide du modèle **Whisper** d’OpenAI, à travers une interface web intuitive développée avec **Gradio**.

https://github.com/user-attachments/assets/8e2a6eba-54f7-4451-9700-6b2f0ea8cf8f

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

## 2. Créer un environnement virtuel (recommandé)

```bash
python -m venv venv
source venv/bin/activate   # Sous macOS/Linux
venv\Scripts\activate      # Sous Windows
```

----

## 3. Installer les dépendances :

```bash
pip install -r requirements.txt



```

## 4. Installer ffmpeg

Téléchargement : Rendez-vous sur le site officiel de ffmpeg : https://ffmpeg.org/download.html

Choix de la version : Pour Windows, vous pouvez utiliser des builds précompilés disponibles sur https://www.gyan.dev/ffmpeg/builds/

Installation :

Téléchargez l'archive ZIP de la version "release full" pour Windows.

Extrayez le contenu de l'archive dans un répertoire de votre choix, par exemple C:\ffmpeg.

À l'intérieur de ce répertoire, vous trouverez un dossier bin contenant l'exécutable ffmpeg.exe.

Ajouter ffmpeg au PATH

Accès aux variables d'environnement :

Cliquez avec le bouton droit sur "Ce PC" ou "Poste de travail" et sélectionnez "Propriétés".

Cliquez sur "Paramètres système avancés".

Dans la fenêtre qui s'ouvre, cliquez sur "Variables d'environnement".

Modification de la variable PATH :

Dans la section "Variables système", recherchez la variable nommée Path et sélectionnez-la, puis cliquez sur "Modifier".

Cliquez sur "Nouveau" et ajoutez le chemin complet vers le dossier bin de ffmpeg, par exemple :
makefile

```bash
C:\ffmpeg\bin
```

Validation :

Cliquez sur "OK" pour fermer toutes les fenêtres et appliquer les modifications.
Discussions on Python.org

 Vérifier l'installation
Ouvrez une nouvelle fenêtre de l'invite de commandes (cmd).

Tapez la commande suivante pour vérifier que ffmpeg est correctement installé et accessible :

```bash
ffmpeg --versoin
```

---

## 5. Lancer l'application :

```bash
python app.py
```

----

