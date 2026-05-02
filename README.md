# Drox Temp Mail API

Professional Temporary Email API built with FastAPI and integrated with 1secmail.

## Developer Information
- **Developer**: drox
- **Instagram**: rayan_71x
- **Credit**: It was developed by drox gpt

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Returns developer and status info |
| `/generate` | GET | Generates a new random temp email |
| `/messages?email=...` | GET | Lists all messages for an email |
| `/message?email=...&id=...` | GET | Fetches full content of a specific message |

## Deployment
This project is configured for seamless deployment on Vercel using the `@vercel/python` runtime.