# Mini CSPM Dashboard (Cloud Security Posture Management)

A simplified Cloud Security Posture Management (CSPM) application that scans AWS resources, evaluates them against security policies, and visualizes risk via a web dashboard.

This project demonstrates a **production mindset**, focusing on clean architecture, security, and clarity over excessive features.

---

## Features

### Backend
- Scans live AWS resources using Boto3
- Supports:
  - EC2 instances
  - S3 buckets
- Applies security policies to detect high-risk resources
- Stateless API (no database, no credential storage)

### Frontend
- Simple and clean React dashboard
- Secure credential input
- Summary view of total assets and high-risk assets
- Asset inventory table with risk highlighting
- Filter to view only high-risk resources

---

## Architecture Overview

- Frontend triggers a scan by sending AWS credentials
- Backend creates a **temporary AWS session**
- Resources are fetched live and evaluated in memory
- No credentials or scan results are persisted

---

## Security Considerations

- During **local development**, communication occurs over `http://localhost`, which is safe as traffic does not leave the local machine.
- In a **production deployment**, all client-server communication would be enforced over **HTTPS (TLS)** using an Application Load Balancer and ACM certificates.
- AWS credentials:
  - Are transmitted securely in production via TLS
  - Are used only in memory to create a temporary AWS session
  - Are never logged, stored, or persisted in any database

---

## Tech Stack

### Backend
- Python
- FastAPI
- Boto3

### Frontend
- React
- Vanilla CSS
- Fetch API

### Cloud
- AWS (EC2, S3)

---

## Setup Instructions

### Prerequisites
- Python 3.9+
- Node.js 18+
- AWS account with EC2 / S3 access

---

## Backend Setup

## For Windows
```bash
cd backend
py -3 -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```
---
## For Mac
```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
---
### Development Dependencies
pytest is included as a development-only dependency and is not required for runtime. if you need pytest run

```bash
pip install -r requirements-dev.txt
```

## Run the server:

```bash
uvicorn app.main:app --reload
```

## Backend will be available at:

http://localhost:8000

---
## Swagger API docs:

http://localhost:8000/docs
---
## Frontend Setup
```bash
cd frontend
npm install
npm start
```

## Frontend will be available at:

-http://localhost:3000

---

## AWS Credentials Setup

- Create an IAM user with read-only permissions

  - AmazonEC2ReadOnlyAccess

  - AmazonS3ReadOnlyAccess

- Generate:

  - Access Key ID

  - Secret Access Key

- Use a region where your resources exist (e.g., ap-south-1)

---

## API Reference

POST /api/v1/scan

Request Body
```json
{
  "access_key": "xxxx",
  "secret_key": "xxxxxxxx",
  "region": "ap-south-1"
}
```

Response
```json
{
  "total_assets": 5,
  "high_risk_assets": 2,
  "resources": [
    {
      "id": "i-012345",
      "type": "EC2",
      "status": "running",
      "risk": "High Risk"
    },
    {
      "name": "new-bucket",
      "type": "S3",
      "risk": "Low Risk"
    }
  ]
}
```
---

## Security Policies Implemented
- EC2 Policy
- High Risk if:
  - Instance is running
  - AND instance is public-facing
- S3 Policy
- High Risk if any of the following are true:
  - Server-side encryption is disabled
  - Bucket is publicly accessible
  - Access logging is disabled
  - Versioning is disabled

---

## Error Handling
- Invalid AWS credentials → Proper error message
- Missing permissions → Gracefully handled
- UI displays errors without crashing

---
  
## Bonus Enhancements
- Docker Compose support for one-command setup
- Unit tests for security policy engine
- Graceful handling of AWS authentication and permission errors
- Clear and readable UI with visual risk indicators

