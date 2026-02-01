#!/bin/bash

# Test health endpoint
echo "==> Testing health endpoint"
curl https://xyz.com/health | jq

# Test voice cloning
echo -e "\n==> Testing voice cloning endpoint"
curl -X POST https://xyz.com/tts \
  -F "text=Hello, this is a test of the voice cloning service" \
  -F "speaker_audio=@test_voice.wav" \
  -o output.wav

echo -e "\n==> Generated audio saved to output.wav"
ls -lh output.wav