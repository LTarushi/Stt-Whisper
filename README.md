# Whisper MP3 to Text Transcription

This project allows you to convert an MP3 file to text using OpenAI's Whisper model on your local machine.

---

## **Installation Guide**

### **Step 1: Install Python and FFmpeg**
Make sure you have Python (3.7 or later) installed.

#### **For Windows:**
1. Install Python from [python.org](https://www.python.org/downloads/).
2. Install FFmpeg:
   - Download from [FFmpeg website](https://ffmpeg.org/download.html).
   - Extract it and add the `bin` folder to your system `PATH`.
   - or just run winget install ffmpeg on cmd
#### **For macOS:**
```sh
brew install ffmpeg
```

#### **For Linux (Debian/Ubuntu):**
```sh
sudo apt update && sudo apt install ffmpeg
```

---

### **Step 2: Install Dependencies**
Run the following command to install required Python packages:

```sh
pip install openai-whisper ffmpeg-python torch
```

---

## **How to Run the Transcription Script**

1. Place your MP3 file in the project directory.
2. Run the transcription script from the terminal:

```sh
python main.py sampleaudio.mp3
```

Replace `sampleaudio.mp3` with the actual filename you want to transcribe.

---

## **Troubleshooting**

### **1. 'ffmpeg' Not Found Error**
- Ensure `ffmpeg` is installed and added to your system `PATH`.
- Test it by running:
  ```sh
  ffmpeg -version
  ```

### **2. Model Download Takes Time**
- The first time you run Whisper, it downloads the model.
- You can pre-download it manually:
  ```sh
  whisper.load_model("base")
  ```

---

## **Additional Notes**
- This script supports various Whisper models (`tiny`, `small`, `medium`, `large`).
- For faster processing, use `tiny` or `small` models.
- Works with MP3, WAV, and other audio formats.
