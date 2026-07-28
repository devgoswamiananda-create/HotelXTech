"""Purane voice-input script ke liye compatibility wrapper.

Recommended command `python main.py --voice` hai. Yeh file sirf old references break na hon isliye rakhi hai.
"""

# Naya microphone/config code reuse karte hain, taaki old file aur main Jarvis dono ka behavior same rahe.
from jarvis.config import load_settings
from jarvis.services import SpeechInput


def listen() -> str:
    """Configured language mein ek baar mic sunein; infinite thread/recursion use nahi hoti."""
    # `.env` se language (e.g. en-IN) load hoti hai, phir maintained SpeechInput ek utterance capture karta hai.
    return SpeechInput().listen(load_settings().language)


if __name__ == "__main__":
    # Direct run par hi listening start hoti hai; import karne par mic auto-start nahi hoga.
    print(listen())
