# XTTS-v2 Cloud MLOps Deployment

Production-ready deployment of Coqui XTTS-v2 voice cloning model on GPU infrastructure (AWS/Azure/GCP) with MLOps best practices.

**Live Demo:** `https://xyz.com`

## 🎯 Overview

Complete MLOps deployment pipeline for XTTS-v2 (Text-to-Speech with Voice Cloning) on cloud GPU infrastructure. Supports AWS, Azure, and GCP with GPU acceleration, containerization, and SSL/TLS security.

## 🏗️ Architecture
```
Client → NGINX (HTTPS:443) → FastAPI (8000) → XTTS-v2 Model (GPU)
```

## ✨ Features

- ✅ GPU Acceleration (CUDA 12.1)
- ✅ Docker + NVIDIA Container Toolkit
- ✅ HTTPS with Let's Encrypt SSL
- ✅ Auto-restart with systemd
- ✅ RESTful API endpoints
- ✅ Health monitoring

## 🚀 Quick Start

### Prerequisites

- GPU-enabled VM (AWS P3/P4, Azure NC-series, or GCP A2)
- Ubuntu 22.04 LTS
- NVIDIA GPU with 16GB+ VRAM
- Domain name (or use self-signed cert)

### Installation

**1. Clone Repository**
```bash
git clone https://github.com/yourusername/xtts-v2-cloud-mlops-deployment.git
cd xtts-v2-cloud-mlops-deployment
```

**2. Setup NVIDIA Container Toolkit**
```bash
chmod +x scripts/setup-nvidia-toolkit.sh
sudo ./scripts/setup-nvidia-toolkit.sh
```

**3. Setup SSL Certificate**
```bash
chmod +x scripts/ssl-setup.sh
sudo ./scripts/ssl-setup.sh xyz.com your@email.com
```

**4. Update Configuration**
```bash
# Edit nginx/nginx.conf - replace domain name
sed -i 's/xtts.kubegrind.com/xyz.com/g' nginx/nginx.conf
```

**5. Deploy**
```bash
docker compose build
docker compose up -d
```

**6. Verify**
```bash
curl https://xyz.com/health
```

## 📡 API Endpoints

### Health Check
```bash
GET /health
```

**Response:**
```json
{
  "status": "healthy",
  "model": "xtts_v2",
  "device": "cuda",
  "gpu_available": true
}
```

### Voice Cloning
```bash
POST /tts
Content-Type: multipart/form-data

Parameters:
- text: string (required)
- speaker_audio: file (required, WAV format)
- language: string (optional, default "en")
```

**Response:** Audio file (WAV)

## 🔧 Usage Examples

### cURL
```bash
curl -X POST https://xyz.com/tts \
  -F "text=Hello, this is a test of voice cloning" \
  -F "speaker_audio=@reference_voice.wav" \
  -o output.wav
```

### Python
```python
import requests

files = {'speaker_audio': open('reference.wav', 'rb')}
data = {'text': 'Your text here'}
response = requests.post('https://xyz.com/tts', files=files, data=data)

with open('output.wav', 'wb') as f:
    f.write(response.content)
```

### Node.js
```javascript
const FormData = require('form-data');
const fs = require('fs');
const axios = require('axios');

const form = new FormData();
form.append('text', 'Your text here');
form.append('speaker_audio', fs.createReadStream('reference.wav'));

const response = await axios.post('https://xyz.com/tts', form, {
  headers: form.getHeaders(),
  responseType: 'arraybuffer'
});

fs.writeFileSync('output.wav', response.data);
```

## 📊 Technical Stack

| Component | Technology |
|-----------|------------|
| **Infrastructure** | AWS/Azure/GCP GPU VMs |
| **GPU** | NVIDIA (CUDA 12.1) |
| **OS** | Ubuntu 22.04 LTS |
| **Container** | Docker + NVIDIA Toolkit |
| **ML Framework** | PyTorch 2.2.0 |
| **Model** | Coqui XTTS-v2 |
| **API** | FastAPI 0.104.1 |
| **Web Server** | NGINX with SSL |

## 🛠️ Management

**View Logs:**
```bash
docker compose logs -f
```

**Restart Service:**
```bash
docker compose restart
```

**Stop Service:**
```bash
docker compose down
```

**Monitor GPU:**
```bash
nvidia-smi
```

## 📈 Performance

- **First request:** ~10-15s (model warm-up)
- **Subsequent requests:** ~3-8s
- **Recommended load:** 1-3 concurrent requests

## 🐛 Troubleshooting

**Service not responding:**
```bash
docker compose ps
docker compose logs app
```

**GPU not detected:**
```bash
nvidia-smi
docker run --rm --gpus all nvidia/cuda:12.0.0-base-ubuntu22.04 nvidia-smi
```

**SSL certificate issues:**
```bash
sudo certbot certificates
sudo certbot renew
```

## 📄 License

MIT License - see [LICENSE](LICENSE) file

## 🤝 Contributing

Contributions welcome! Please open an issue or submit a pull request.

## 📧 Contact

- **Portfolio:** kubegrind.com
- **Email:** your@email.com
- **GitHub:** [@yourusername](https://github.com/yourusername)

## 🙏 Acknowledgments

- [Coqui TTS](https://github.com/coqui-ai/TTS) for the XTTS-v2 model
- NVIDIA for GPU acceleration tools