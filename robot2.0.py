"""Purane text-to-speech script ke liye compatibility wrapper.

Recommended command `python main.py` hai. Yeh file old projects/imports ko compatible rakhne ke liye hai.
"""

# Naya secure TTS/config code reuse karte hain, taaki temp audio cleanup aur error handling duplicate na ho.
from jarvis.config import load_settings
from jarvis.services import SpeechOutput


def Speak(text: str) -> None:
    """Ek non-empty message ko configured Edge voice mein bolkar sunayein."""
    # Voice `.env` se select hoti hai; source code edit kiye bina voice badli ja sakti hai.
    settings = load_settings()
    SpeechOutput().speak(text, settings.voice_name)


if __name__ == "__main__":
    # Direct execution par example speech chalegi; import par audio auto-play nahi hoga.
    Speak("Welcome to the world of Jarvis.")
