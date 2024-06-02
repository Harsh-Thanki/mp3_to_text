# mp3_to_text

This project turns mp3 input into text and writes it down in a txt file.

1. Clone the repository.

2. Activate your virtual environment.

3. Install whisper from it's repository:

```sh
pip install git+https://github.com/openai/whisper.git
```

3. Install ffmpeg

```sh
sudo apt update
sudo apt install ffmpeg
```

4. Create a blank txt in same directory as the python file.
5. Replace the file name to newly created file name at output_file_path.
6. Run the main.py

The input mp3 is Kwaai public meet May 17 2024 audio. If you want to change it follow below steps:

Add mp3 that you want to the same location as main.py & then change the value of audio_file_path variable inside main.py to the added mp3 file name.
