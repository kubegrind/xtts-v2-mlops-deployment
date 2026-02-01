const FormData = require('form-data');
const fs = require('fs');
const axios = require('axios');

async function cloneVoice(text, speakerAudioPath, outputPath = 'output.wav') {
    const form = new FormData();
    form.append('text', text);
    form.append('speaker_audio', fs.createReadStream(speakerAudioPath));
    
    const response = await axios.post('https://xyz.com/tts', form, {
        headers: form.getHeaders(),
        responseType: 'arraybuffer'
    });
    
    fs.writeFileSync(outputPath, response.data);
    return outputPath;
}

async function checkHealth() {
    const response = await axios.get('https://xyz.com/health');
    return response.data;
}

// Example usage
(async () => {
    // Test health endpoint
    const health = await checkHealth();
    console.log('Health check:', health);
    
    // Clone voice
    const output = await cloneVoice(
        'Hello, this is a test of voice cloning',
        'reference_voice.wav',
        'cloned_output.wav'
    );
    console.log(`Generated audio saved to: ${output}`);
})();