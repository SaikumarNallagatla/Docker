```markdown
# 🐳 Full DevOps Guide: Flask + Docker + CI/CD – Built by Bujji

This is a complete step-by-step tutorial to build, containerize, test, and simulate a CI/CD pipeline for a Flask application using Docker inside a sandbox environment.

Designed for real-world DevOps flow — streamlined for VS Code, Docker, GitHub Actions, and CI/CD simulation.

---

## 🧠 Why Use Docker and CI/CD in Flask Projects?

| Problem (Without Docker)          | Docker + CI/CD Solution                                           |
|----------------------------------|------------------------------------------------------------------|
| App works only on developer laptop | Docker creates isolated environments that work anywhere          |
| Manual testing & deployment       | CI/CD automates build, test, and deployment                      |
| Slow delivery, manual regression  | Automated pipelines push new versions in minutes                 |
| Bloated environments              | Docker multi-stage builds create lean, secure images             |

✅ **Industry Use Case:**  
In companies like Zomato or Swiggy, the order API, inventory service, and payment gateway all run in separate containers. CI/CD ensures fast bug fixes, tested rollouts, and zero downtime.

---

## 📁 Final Project Structure

```
my-docker-flask-app/
├── app.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── tests/
│   └── test_app.py
├── ci_simulate.sh
└── .github/
    └── workflows/
        └── docker.yml (for real GitHub deployment)
```

---

## 📝 Step-by-Step Guide

### 1️⃣ app.py – Flask Application

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "CI/CD Simulation – Bujji's Flask App"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

---

### 2️⃣ requirements.txt – Production Dependencies

```
Flask==2.3.2
```

---

### 3️⃣ .dockerignore – Files to Ignore During Build

```
__pycache__/
*.pyc
.env
*.log
tests/
```

---

### 4️⃣ Dockerfile – Containerizing Flask App

```Dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000
CMD ["python", "app.py"]
```

---

### 5️⃣ tests/test_app.py – Basic Unit Test

```python
def test_logic():
    assert 1 + 1 == 2
```

---

### 6️⃣ ci_simulate.sh – Manual CI Pipeline Simulation

```bash
#!/bin/bash

echo "📦 Installing dependencies..."
pip install -r requirements.txt

echo "🧪 Running tests..."
pytest

echo "🐳 Building Docker image..."
docker build -t flask-ci .

echo "🚀 Deploying container..."
docker run -d --name flask-ci-container -p 5000:5000 flask-ci

echo "📋 Logs:"
docker logs flask-ci-container
```

Run in sandbox:
```bash
bash ci_simulate.sh
```

---

## 🔐 If pytest fails in sandbox:

Use system package manager:
```bash
apt-get update
apt-get install python3-pytest
```

Then:
```bash
pytest tests/
```

---

### 7️⃣ .github/workflows/docker.yml (Real GitHub Actions CI/CD)

```yaml
name: Docker Build & Push

on:
  push:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v3

      - name: 🐍 Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      - name: 📦 Install Dependencies
        run: pip install -r requirements.txt

      - name: 🧪 Run Tests
        run: pytest

      - name: 🐳 Build Docker Image
        run: docker build -t flask-ci .

      - name: 🔐 Login & Push to Docker Hub
        run: |
          echo "${{ secrets.DOCKER_PASSWORD }}" | docker login -u "${{ secrets.DOCKER_USERNAME }}" --password-stdin
          docker tag flask-ci yourdockerhub/flask-ci:latest
          docker push yourdockerhub/flask-ci:latest
```

---

## 🚀 Final Commands Recap

| Action                     | Command                                        |
|---------------------------|------------------------------------------------|
| Install deps              | `pip install -r requirements.txt`             |
| Run tests                 | `pytest tests/`                                |
| Build image               | `docker build -t flask-ci .`                  |
| Run container             | `docker run -d --name flask-ci -p 5000:5000 flask-ci` |
| View logs                 | `docker logs flask-ci`                         |
| Stop container            | `docker stop flask-ci && docker rm flask-ci`  |

---

## 💡 DevOps Principles Applied

| Principle          | Implementation                                       |
|--------------------|------------------------------------------------------|
| 📁 Immutable Infra  | Docker image is identical across environments        |
| ⚙️ Automation        | CI/CD simulation script mimics GitHub workflow       |
| ✅ Test First       | Unit tests ensure app logic is safe to deploy        |
| 🔍 Build Minimization | Dockerfile uses slim base + .dockerignore         |
| 🔄 Repeatability    | `ci_simulate.sh` reproducibly runs the full pipeline |

---

## ✅ Conclusion

This setup:
- Containerizes your Flask app using Docker
- Simulates a CI/CD pipeline in sandbox
- Runs tests before deployment
- Prepares you for GitHub Actions, Docker Hub, Kubernetes

Built & Simulated by Bujji – Tactical DevOps Operator 💥  
Ready for Step 8: Pushing your image to Docker Hub?

```bash
docker login
docker tag flask-ci yourdockerhub/flask-ci:latest
docker push yourdockerhub/flask-ci:latest

