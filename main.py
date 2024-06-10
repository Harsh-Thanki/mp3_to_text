import whisper


def load_model(model_name="tiny"):
    try:
        print("Loading model...")
        model = whisper.load_model(model_name)
        print(f"{model_name.capitalize()} model loaded!")
        return model
    except Exception as e:
        print(f"Error loading model: {e}")
        raise


def transcribe_audio(model, audio_file_path):
    try:
        print(f"Transcribing audio file: {audio_file_path}")
        result = model.transcribe(audio_file_path)
        transcription = result['text']
        return transcription
    except Exception as e:
        print(f"Error transcribing audio file: {e}")
        raise


def save_transcription(transcription, output_file_path):
    try:
        with open(output_file_path, 'w') as file:
            file.write(transcription)
        print(f"Transcription saved to {output_file_path}")
    except Exception as e:
        print(f"Error saving transcription: {e}")
        raise


def main():
    audio_file_path = "input/Kwaai Public Meeting May 17th 2024.mp3"  # MP3 file path
    output_file_path = "output/transcription.txt"  # Replace with your desired output file path
    model_name = "tiny"

    model = load_model(model_name)
    transcription = transcribe_audio(model, audio_file_path)
    print(transcription)
    save_transcription(transcription, output_file_path)


if __name__ == "__main__":
    main()
