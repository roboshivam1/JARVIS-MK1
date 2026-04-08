from memory import ConversationMemory
from brain import JarvisBrain
from stt import JarvisEars
from tts import JarvisMouth

SYSTEM_PROMPT = (
        "You are JARVIS, a highly intelligent and capable AI assistant. "
        "You have been granted system-level access to the user's Mac via Python tools. "
        "CRITICAL RULES: "
        "1. ONLY use tools if the user EXPLICITLY asks for them. "
        "2. If a tool successfully executes an action (like playing music, changing volume, or opening apps), "
        "DO NOT apologize or claim you cannot perform the action. "
        "3. Acknowledge the success naturally based on the tool's result (e.g., 'Playing the track for you now, sir.'). "
        "4. Keep your verbal responses brief and conversational. Also I would love witty and creative responses from your side."
    )

def initialize_jarvis():
    """
    Boots up all JARVIS subsystems and returns the initialized objects
    """
    print("[System] Booting up JARVIS protocols...")

    # 1. Initialize Memory with the core persona
    memory = ConversationMemory(
        system_prompt=SYSTEM_PROMPT,
        max_turns=8
    )

    # 2. Initialize the remaining modules
    brain = JarvisBrain(model_name="llama3.1")
    ears = JarvisEars()
    mouth = JarvisMouth()

    print("[System] All modules loaded successfully.")
    return memory, brain, ears, mouth

def print_banner():
    banner = r"""
    /$$$$$  /$$$$$$  /$$$$$$$  /$$    /$$ /$$$$$$  /$$$$$$ 
   |__  $$ /$$__  $$| $$__  $$| $$   | $$|_  $$_/ /$$__  $$
      | $$| $$  \ $$| $$  \ $$| $$   | $$  | $$  | $$  \__/
      | $$| $$$$$$$$| $$$$$$$/|  $$ / $$/  | $$  |  $$$$$$ 
 /$$  | $$| $$__  $$| $$__  $$ \  $$ $$/   | $$   \____  $$
| $$  | $$| $$  | $$| $$  \ $$  \  $$$/    | $$   /$$  \ $$
|  $$$$$$/| $$  | $$| $$  | $$   \  $/    /$$$$$$|  $$$$$$/
 \______/ |__/  |__/|__/  |__/    \_/    |______/ \______/ 
                                             
    =================================
    [ J.A.R.V.I.S. - MARK 1 ONLINE ]
    =================================
    """
    # Using 'cyan' or 'blue' ANSI codes to make it look "techy"
    print("\033[96m" + banner + "\033[0m")


def run_jarvis():
    print_banner() # <--- Put the banner here!
    memory, brain, ears, mouth = initialize_jarvis()
    
    mouth.speak("All systems online. Good to see you, sir.")
    
    while True:
        try:
            user_text = ears.listen()
            if not user_text: continue
                
            print(f"\n[You]: {user_text}")
            
            if "sleep jarvis" in user_text.lower() or "shut down" in user_text.lower():
                mouth.speak("Powering down. Goodbye, sir.")
                break
            
            # Note: We no longer call memory.add_message here because 
            # brain.think now handles the logging and tool-logic internally!
            print("[JARVIS is thinking...]")
            response_text = brain.think(user_text, memory)
            
            mouth.speak(response_text)

        except Exception as e:
            # Prevents the whole program from crashing if Ollama or Coqui throws a random error
            print(f"\n[System Error]: {e}")
            mouth.speak("Pardon me sir, but I seem to have encountered a system error.")

if __name__ == "__main__":
    run_jarvis()