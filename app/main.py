from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from fastapi.responses import FileResponse
from TTS.api import TTS
import torch
import os
import tempfile
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="XTTS-v2 Inference Service")

# Initialize TTS model
device = "cuda" if torch.cuda.is_available() else "cpu"
logger.info(f"Using device: {device}")

try:
    # Initialize TTS and move to device
    tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)
    logger.info("XTTS-v2 model loaded successfully")
except Exception as e:
    logger.error(f"Failed to load model: {e}")
    raise

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "model": "xtts_v2",
        "device": device,
        "gpu_available": torch.cuda.is_available()
    }

@app.post("/tts")
async def text_to_speech(
    text: str = Form(...),
    speaker_audio: UploadFile = File(...),
    language: str = Form("en")
):
    """
    Generate speech from text using speaker voice cloning
    """
    try:
        # Save uploaded speaker audio
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as speaker_file:
            content = await speaker_audio.read()
            speaker_file.write(content)
            speaker_path = speaker_file.name

        # Generate output
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as output_file:
            output_path = output_file.name

        # Run TTS
        tts.tts_to_file(
            text=text,
            speaker_wav=speaker_path,
            language=language,
            file_path=output_path
        )

        # Cleanup speaker file
        os.unlink(speaker_path)

        return FileResponse(
            output_path,
            media_type="audio/wav",
            filename="output.wav",
            background=lambda: os.unlink(output_path)
        )

    except Exception as e:
        logger.error(f"TTS generation failed: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/clone")
async def clone_voice(
    text: str = Form(...),
    speaker_audio: UploadFile = File(...),
    language: str = Form("en")
):
    """
    Alias for /tts endpoint with language support
    """
    return await text_to_speech(text, speaker_audio, language)