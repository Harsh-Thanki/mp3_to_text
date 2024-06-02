# mp3_to_text

1. Activate your virtual environment.

2. Install whisper from it's repository:

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