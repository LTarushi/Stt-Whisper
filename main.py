import whisper
import sys

# Ensure the user provides an audio file
if len(sys.argv) != 2:
    print("Usage: python main.py <audio.mp3>")
    sys.exit(1)

audio_file = sys.argv[1]

# Load Whisper model
model = whisper.load_model("small")

# Transcribe the audio
result = model.transcribe(audio_file)

# Print the transcription
print("\nTranscription:\n", result["text"])