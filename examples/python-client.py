import requests

def clone_voice(text: str, speaker_audio_path: str, output_path: str = "output.wav"):
    """
    Clone voice using XTTS-v2 service
    
    Args:
        text: Text to synthesize
        speaker_audio_path: Path to reference speaker audio file
        output_path: Path to save generated audio
    
    Returns:
        Path to generated audio file
    """
    url = "https://xyz.com/tts"
    
    files = {
        'speaker_audio': open(speaker_audio_path, 'rb')
    }
    data = {
        'text': text
    }
    
    response = requests.post(url, files=files, data=data)
    response.raise_for_status()
    
    with open(output_path, 'wb') as f:
        f.write(response.content)
    
    return output_path

# Example usage
if __name__ == "__main__":
    # Test health endpoint
    health = requests.get("https://xyz.com/health")
    print("Health check:", health.json())
    
    # Clone voice
    output = clone_voice(
        text="Hello, this is a test of voice cloning",
        speaker_audio_path="reference_voice.wav",
        output_path="cloned_output.wav"
    )
    print(f"Generated audio saved to: {output}")