import subprocess
import os
import ollama

def analyze_screen(query: str) -> str:
    """
    Takes a screenshot of the user's current screen and analyzes it to answer a question.
    Use this tool ONLY when the user explicitly asks you to "look at the screen", "read the screen", or asks a question about what is currently visible on their monitor.
    
    :param query: The specific question or instruction about the screen (e.g., 'What is this error message?' or 'Summarize this document').
    """

    image_path = "temp_screen.jpg"

    try:
        subprocess.run(["screencapture", "-x", "-t", "jpg", image_path], check=True)

        response = ollama.generate(
            model='llava',
            prompt=query,
            images=[image_path]
        )

        if os.path.exists(image_path):
            os.remove(image_path)
        
        return f"Screen Analysis: {response['response']}"
    
    except Exception as e:
        if os.path.exists(image_path):
            os.remove(image_path)
        return f"Error analyzing screen: {e}"
    
VISION_TOOLS = {
    "analyze_screen": analyze_screen
}