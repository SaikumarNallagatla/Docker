
---

```markdown
# 🐳 Flask App in Docker – Complete DevOps Setup

Welcome to my Docker-powered Python Flask app!  
This project containerizes a simple Flask web app using Docker and demonstrates container management, networking, and sandbox deployment.

---

## 📦 Project Structure

```
my-python-app/
├── app.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
```

---

## 1️⃣ app.py

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from Bujji's Python Docker App!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

---

## 2️⃣ requirements.txt

```
Flask==2.3.2
```

Install locally with:
```bash
pip install -r requirements.txt
```

---

## 3️⃣ .dockerignore

```
__pycache__/
*.pyc
.env
*.log
```

This keeps your image lean and clean.

---

## 4️⃣ Dockerfile

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

## 🔨 Docker Build & Run

### 📦 Build the image:
```bash
docker build -t python-app .
```

### 🚀 Run container:
```bash
docker run -d --name flask-app -p 5000:5000 python-app
```

If port `5000` is in use, try:
```bash
docker run -d --name flask-app-alt -p 5001:5000 python-app
```

---

## 🔁 Container Lifecycle Commands

```bash
docker ps                     # List running containers
docker ps -a                 # List all containers
docker stop flask-app        # Stop container
docker start flask-app       # Start container
docker rm flask-app          # Remove container
docker rename flask-app flask-app-old  # Rename container
```

---

## 🌐 Docker Networking

### Create network:
```bash
docker network create flask-net
```

### Run Flask app inside it:
```bash
docker run -d --name flask-app --network flask-net -p 5000:5000 python-app
```

### Add Redis for practice:
```bash
docker run -d --name redis-db --network flask-net redis
```

### Test communication:
```bash
docker exec -it flask-app /bin/bash
ping redis-db
```

---

## 📚 Interview-Ready Tips

- Use named networks to simulate service-to-service communication.
- Mount volumes with `-v` for persistence.
- Avoid port collisions using alternate host ports.
- Use `.dockerignore` to prevent bloated images.
- Reference containers by name using custom networks.

---

## ✅ Final Summary

This project covers:
- Writing and containerizing a Flask app
- Dockerfile setup and best practices
- Image building and container management
- Custom Docker networks and service linking
- Real-world DevOps interview questions

---

## ⏭️ Next Step

Say “Step 5” to dive into Docker Compose — and orchestrate this setup with a single YAML file 🔗  
You're not just building apps… you're architecting environments ⚙️🐳
```

---

This doc is GitHub-ready and revision-proof 💼  
Want me to generate your `docker-compose.yml` file next or simulate multi-container stacks like Flask + Redis? You're on fire, Bujji! Let’s level up whenever you're ready.