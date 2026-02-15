# AI Text Enhancer API

A containerized FastAPI microservice that enhances, transforms, and reformats text using AI. This service exposes a REST API that can improve tone, summarize content, and rewrite text in different styles.

The system is designed with production-ready architecture, including Docker containerization, environment-based configuration, graceful fallback handling, and structured API responses.

---

## Live Demo

Public API Documentation (Swagger UI):

https://ai-text-enhancer-j4sb.onrender.com/docs

Health Check Endpoint:

https://ai-text-enhancer-j4sb.onrender.com/

You can test the `/generate` endpoint directly from the Swagger interface without installing anything locally.

---

## Features

- FastAPI-based REST API
- AI-powered text transformation
- Mock mode for offline/demo usage (no billing required)
- Graceful fallback when AI quota is unavailable
- Docker container support
- Environment variable configuration
- Automatic API documentation via Swagger UI
- Public cloud deployment on Render
- Fully containerized microservice architecture

---

## Architecture

```
Client → FastAPI → AI Service Layer → OpenAI API (or Mock Mode)
             ↓
          Docker Container
             ↓
         Cloud Deployment (Render)
```

---

## API Endpoint

### POST `/generate`

Enhances or transforms text based on the specified mode.

**Request Body**

```json
{
  "text": "I want to improve my backend skills.",
  "mode": "professional"
}
```

**Response**

```json
{
  "result": "Enhanced version of the text...",
  "source": "mock"
}
```

**source values:**

- `"mock"` → fallback mode (no billing required)
- `"openai"` → real AI response

---

## Modes Supported

- professional
- summarize
- improve
- custom modes (extensible)

---

## Local Development (Docker Recommended)

### 1. Clone repository

```bash
git clone https://github.com/WiraAFauzi/AI-Text-Enhancer.git
cd ai-text-enhancer
```

### 2. Create environment file

Create `.env` file:

```
MOCK_MODE=true
OPENAI_API_KEY=your_key_here
```

Mock mode allows testing without OpenAI billing.

---

### 3. Run using Docker

```bash
docker compose up --build
```

API will be available at:

```
http://localhost:8000/docs
```

---

## Running Without Docker (Optional)

Create virtual environment:

```bash
python -m venv venv
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run server:

```bash
uvicorn app.main:app --reload
```

---

## Docker Commands

Start container:

```bash
docker compose up
```

Run in background:

```bash
docker compose up -d
```

Stop container:

```bash
docker compose down
```

View running containers:

```bash
docker ps
```

---

## Environment Variables

| Variable | Description | Required |
|--------|-------------|----------|
| MOCK_MODE | Enables mock fallback mode | Yes |
| OPENAI_API_KEY | OpenAI API key | Only for real AI |

---

## Project Structure

```
ai-text-enhancer/
│
├── app/
│   ├── main.py
│   ├── schemas.py
│   └── services.py
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env
└── README.md
```

---

## Deployment

This service is currently deployed on Render:

https://ai-text-enhancer-j4sb.onrender.com/docs

Supported deployment platforms:

- Render
- Fly.io
- Railway
- AWS
- Azure
- Google Cloud

Docker ensures consistent deployment across environments.

---

## Example Use Cases

- Resume enhancement backend
- Email rewriting service
- Content summarization API
- Writing assistants
- Customer support automation
- SaaS AI integration backend

---

## Technology Stack

- FastAPI
- Python
- Docker
- OpenAI API
- Pydantic
- Uvicorn
- Render (Cloud Hosting)

---

## Design Principles

- Containerized infrastructure
- Environment-driven configuration
- Fault-tolerant fallback logic
- Stateless microservice design
- Cloud-ready deployment model

---

## Future Improvements

- Authentication
- Rate limiting
- Logging
- Database integration
- Request tracking
- Multi-model support
- Frontend interface

---

## License

MIT License

---

## Author

Wira Ahmad Fauzi

Backend Developer | AI Integration | FastAPI | Docker
