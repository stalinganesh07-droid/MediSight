# AI Doctor Project

[![Python Version](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Workflow Status](https://img.shields.io/badge/workflow-passing-brightgreen.svg)](https://github.com/your-username/your-repo/actions)

This project is an AI-powered medical assistant that can analyze images, transcribe audio, and respond with a doctor-like voice. It integrates **speech-to-text**, **image analysis**, and **text-to-speech** capabilities using Python, Gradio, and ElevenLabs.

---

## Table of Contents

- [Installing FFmpeg and PortAudio](#installing-ffmpeg-and-portaudio)  
  - [macOS](#macos)  
  - [Linux](#linux)  
  - [Windows](#windows)  
- [Setting Up a Python Virtual Environment](#setting-up-a-python-virtual-environment)  
  - [Using Pipenv](#using-pipenv)  
  - [Using pip and venv](#using-pip-and-venv)  
  - [Using Conda](#using-conda)  
- [Running the Application](#running-the-application)  
- [Environment Variables](#environment-variables)  
- [Project Structure](#project-structure)

---

## Installing FFmpeg and PortAudio

### macOS

Install Homebrew (if not already installed):

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
Install FFmpeg and PortAudio:

bash
Copy code
brew install ffmpeg portaudio
Linux (Debian/Ubuntu)
Update the package list:

bash
Copy code
sudo apt update
Install FFmpeg and PortAudio:

bash
Copy code
sudo apt install ffmpeg portaudio19-dev
Windows
Download FFmpeg:

Visit FFmpeg Downloads

Navigate to the Windows builds section and download the latest static build.

Extract and Set Up FFmpeg:

Extract the ZIP file to a folder (e.g., C:\ffmpeg).

Add the bin directory to your system's PATH:

Search for "Environment Variables" in the Start menu.

Click "Edit the system environment variables."

Under "System variables," select the Path variable and click "Edit."

Click "New" and add the path to the bin directory (e.g., C:\ffmpeg\bin).

Click "OK" to apply the changes.

Install PortAudio:

Download the PortAudio binaries from the official website: PortAudio Downloads

Follow the installation instructions provided.

Setting Up a Python Virtual Environment
Using Pipenv
bash
Copy code
pip install pipenv
pipenv install
pipenv shell
Using pip and venv
Create a virtual environment:

bash
Copy code
python -m venv venv
Activate the virtual environment:

macOS/Linux:

bash
Copy code
source venv/bin/activate
Windows:

bash
Copy code
venv\Scripts\activate
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Using Conda
Create a Conda environment:

bash
Copy code
conda create --name myenv python=3.11
conda activate myenv
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Running the Application
The project has four main phases:

Brain of the Doctor

bash
Copy code
python brain_of_the_doctor.py
Voice of the Patient

bash
Copy code
python voice_of_the_patient.py
Voice of the Doctor

bash
Copy code
python voice_of_the_doctor.py
Setup Gradio UI

bash
Copy code
python gradio_app.py
Environment Variables
Make sure to set up your API keys:

bash
Copy code
# Example for ElevenLabs API Key
export ELEVENLABS_API_KEY="your_api_key_here"  # macOS/Linux
setx ELEVENLABS_API_KEY "your_api_key_here"    # Windows

# Example for GROQ API Key
export GROQ_API_KEY="your_api_key_here"  # macOS/Linux
setx GROQ_API_KEY "your_api_key_here"    # Windows
Project Structure
pgsql
Copy code
ai-doctor-2.0-voice-and-vision/
│
├─ brain_of_the_doctor.py      # Image analysis and AI logic
├─ voice_of_the_patient.py     # Speech-to-text recording
├─ voice_of_the_doctor.py      # Text-to-speech conversion
├─ gradio_app.py               # UI for interaction
├─ requirements.txt            # Python dependencies
└─ README.md                   # Project setup guide
