# mp3_to_text

This project turns mp3 input into text and writes it down in a txt file.

1. Clone the repository.

2. Activate your virtual environment.

3. Install `whisper` from it's repository using below command:

```sh
pip install git+https://github.com/openai/whisper.git
```

3. Install `ffmpeg` using below command:

```sh
sudo apt update
sudo apt install ffmpeg
```

4. The input mp3 is Kwaai public meet May 17 2024 audio. If you want to change it:
   -  Add the mp3 that you want to convert in text in the input directory.
   -  Now change the value of `audio_file_path` variable inside main.py to the added mp3 file path.


5. Replace the output file name to a new file name at the `output_file_path` variable in main.py file.
6. Run the main.py
7. After the main.py runs successfully you can check the output file inside output directory with your specified name.

### NOTE: 
This project uses the `tiny` Whisper model due to its small size. You can change it to a larger model for better output quality. 

The available models are: `tiny`, `base`, `small`,`medium`, `large`.

To change the model, update the model name in the `model_name` variable in `main.py` file.

To get more info visit: [Whisper GitHub Repository](https://github.com/openai/whisper)
