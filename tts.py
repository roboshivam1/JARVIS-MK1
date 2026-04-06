from TTS.api import TTS
import os
import subprocess

class JarvisMouth:
    def __init__(self, model_name: str = "tts_models/en/vctk/vits"):
        """
        Initializes the text to speech engine using coqui tts
        """
        print("[System] Warming up JARVIS's voice...")
        self.tts = TTS(model_name=model_name, progress_bar=False, gpu=False)
    
    def speak(self, text: str, speaker_id: str = "p230") -> None:
        """
        Converts text to speech and plays it out loud.
        """
        print(f"JARVIS: {text}")
        output_file = "response.wav"

        self.tts.tts_to_file(text=text, file_path=output_file, speaker=speaker_id)

        subprocess.run(["afplay", output_file])

        if os.path.exists(output_file):
            os.remove(output_file)