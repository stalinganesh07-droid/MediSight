import os
from gtts import gTTS
from elevenlabs.client import ElevenLabs
from elevenlabs import save
from playsound import playsound

# Get ElevenLabs API key from environment
ELEVENLABS_API_KEY = os.environ.get("ELEVENLABS_API_KEY", "").strip()


def text_to_speech(input_text, output_filepath="tts_output.mp3", eleven_voice="Rachel"):
    """
    Convert text to speech and play audio.
    Primary: ElevenLabs TTS
    Fallback: gTTS if ElevenLabs fails
    """
    # -----------------------------
    # Try ElevenLabs first
    # -----------------------------
    if ELEVENLABS_API_KEY:
        try:
            client = ElevenLabs(api_key=ELEVENLABS_API_KEY)
            audio = client.generate(
                text=input_text,
                voice=eleven_voice,
                output_format="mp3_22050_32",  # MP3 output
                model="eleven_turbo_v2"
            )

            # Save using official helper (handles generator)
            save(audio, output_filepath)
            print(f"[INFO] Played ElevenLabs voice: {eleven_voice}")

            # Play audio cross-platform
            playsound(output_filepath)
            return

        except Exception as e:
            print(f"[WARN] ElevenLabs TTS failed: {e}")

    # -----------------------------
    # Fallback to gTTS
    # -----------------------------
    try:
        tts = gTTS(text=input_text, lang="en", slow=False)
        tts.save(output_filepath)
        print("[INFO] Played fallback gTTS voice")
        playsound(output_filepath)
    except Exception as e:
        print(f"[ERROR] gTTS fallback failed: {e}")


# -----------------------------
# Example usage
# -----------------------------
if __name__ == "__main__":
    doctor_response = "Hello! I am your AI doctor. How can I help you today?"
    text_to_speech(doctor_response)


#http://127.0.0.1:7860
