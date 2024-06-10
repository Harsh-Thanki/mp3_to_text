import whisper

print("Model is being loaded.")
# Loading the Whisper model: options are tiny, base, small, medium, large
model = whisper.load_model("tiny")
print("Model loaded!!")

# Transcribing the MP3 file
audio_file_path = "input/Kwaai Public Meeting May 17th 2024.mp3"  # MP3 file path
result = model.transcribe(audio_file_path)

# Extracting the transcription
transcription = result['text']

# Printing the transcription to the console
print(transcription)

# Saving the transcription to a text file
output_file_path = "output/transcription.txt"  # Replace with your desired output file path
with open(output_file_path, 'w') as file:
    file.write(transcription)

print(f"Transcription saved to {output_file_path}")


