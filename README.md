# STT Spotify DJ

To Setup:
1. Change .env.example to .env and add a valid OpenAI API Key
2. Run ```poetry install``` to download dependencies 
3. Make sure you have the macOS Spotify app downloaded in your Applications directory. 
4. Run ```poetry run python stt_dj/main.py```

The DJ works by:
1. Collecting user audio with the SpeechRecognition library and converting to text with Google Speech Recognition. 
2. Parsing the user request and formatting as a Python dictionary with LangChain's ChatOpenAI and StructuredOutputParser modules.
3. Controlling the Spotify macOS app to search and play the requested track.  