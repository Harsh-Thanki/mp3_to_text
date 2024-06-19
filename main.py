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
        result = model.transcribe(audio_file_path, verbose=True)
        return result
    except Exception as e:
        print(f"Error transcribing audio file: {e}")
        raise


def format_timestamp(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds = int(seconds % 60)
    milliseconds = int((seconds % 1) * 1000)
    return f"{hours:02}:{minutes:02}:{seconds:02},{milliseconds:03}"


def save_transcription_txt(transcription, output_file_path):
    try:
        with open(output_file_path, 'w') as file:
            file.write(transcription)
        print(f"Transcription saved to {output_file_path}")
    except Exception as e:
        print(f"Error saving transcription: {e}")
        raise


def save_transcription_srt(transcription_result, output_file_path):
    try:
        segments = transcription_result['segments']
        with open(output_file_path, 'w') as file:
            for i, segment in enumerate(segments):
                start_time = format_timestamp(segment['start'])
                end_time = format_timestamp(segment['end'])
                text = segment['text']
                file.write(f"{i + 1}\n")
                file.write(f"{start_time} --> {end_time}\n")
                file.write(f"{text.strip()}\n\n")
        print(f"Transcription saved to {output_file_path}")
    except Exception as e:
        print(f"Error saving transcription: {e}")
        raise


def main():
    audio_file_path = "input/Kwaai Public Meeting May 17th 2024.mp3"  # MP3 file path
    model_name = "tiny"

    # Get user input for output format
    output_format = input("Enter output format (txt/srt): ").strip().lower()
    if output_format == "txt":
        output_file_path = "output/transcription.txt"  # Replace with your desired output file path
    elif output_format == "srt":
        output_file_path = "output/transcription.srt"  # Replace with your desired output file path
    else:
        print("Invalid output format. Please enter 'txt' or 'srt'.")
        return

    model = load_model(model_name)
    transcription_result = transcribe_audio(model, audio_file_path)

    if output_format == "txt":
        transcription = transcription_result['text']
        print(transcription)
        save_transcription_txt(transcription, output_file_path)
    elif output_format == "srt":
        save_transcription_srt(transcription_result, output_file_path)


if __name__ == "__main__":
    main()
