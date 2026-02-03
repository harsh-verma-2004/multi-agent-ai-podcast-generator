import pyttsx3
import os
import datetime
from dotenv import load_dotenv
from crewai.tools import tool
from crewai_tools import FileWriterTool, FileReadTool, SerperDevTool


load_dotenv()

file_writer_tool = FileWriterTool()
file_read_tool = FileReadTool()
search_tool = SerperDevTool()

# Load TTS model once
engine = pyttsx3.init()

@tool
def tts_voice_tool(script: str) -> str:
    """
    Converts a podcast script into spoken audio and saves it as a WAV file
    using offline text-to-speech (pyttsx3).
    """
    output_dir = os.path.join(os.getcwd(), "outputs")
    os.makedirs(output_dir, exist_ok=True)

    filename = os.path.join(
        output_dir,
        f"podcast-{datetime.datetime.now().strftime('%Y%m%d-%H%M%S')}.wav"
    )

    engine.save_to_file(script, filename)
    engine.runAndWait()

    return f"Podcast audio generated at {filename}"
