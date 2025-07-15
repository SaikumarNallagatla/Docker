

---

```markdown
# 🐳 Flask + Redis with Docker & Docker Compose – Complete Guide

This project containerizes a Python Flask application with Redis using Docker and Docker Compose. It demonstrates container creation, networking, service orchestration, and inter-container communication — a solid DevOps sandbox setup.

Built with 💡 by Bujji – tactical strategist in DevOps!

---

## 📁 Project Structure

```
my-flask-docker-app/
├── app.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
└── docker-compose.yml
```

---

## 1️⃣ app.py – Python + Redis App

```python
from flask import Flask
import redis

app = Flask(__name__)
r = redis.Redis(host='redis', port=6379)

@app.route('/')
def hello():
    try:
        visits = r.incr('visits')
    except redis.ConnectionError:
        visits = "Redis not available"
    return f"Hello Bujji! Visit count: {visits}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

✅ Talks to Redis using name `redis` → handled by Compose network.

---

## 2️⃣ requirements.txt

```
flask==2.3.2
redis==5.0.1
```

---

## 3️⃣ .dockerignore

```
__pycache__/
*.pyc
.env
*.log
```

Keeps builds clean and prevents sensitive or bulky files from entering Docker image.

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

✅ Slim base + caching + clean layers.

---

## 5️⃣ docker-compose.yml

```yaml
version: "3.9"

services:
  web:
    build: .
    container_name: flask-app
    ports:
      - "5000:5000"
    depends_on:
      - redis
  redis:
    image: redis
    container_name: redis-service
```

✅ `depends_on` ensures Redis is ready when Flask launches.  
✅ Compose creates default bridge network — allowing `web` to call `redis`.

---

## 🧪 Run Step-by-Step in Your Sandbox

### 1️⃣ Build & Start Containers

```bash
docker compose up --build
```

Visit in browser:  
```
http://localhost:5000
```

### 2️⃣ Stop and Remove All

```bash
docker compose down
```

### 3️⃣ Run in Background

```bash
docker compose up -d
docker compose logs web
```

### 4️⃣ Rebuild After Code Change

```bash
docker compose up --build
```

---

## 🛠️ Debugging Tools

### Show containers:
```bash
docker ps
```

### Check logs:
```bash
docker logs flask-app
```

### Enter container:
```bash
docker exec -it flask-app /bin/bash
```

### Remove name conflicts:
```bash
docker rm flask-app
```

---

## 💡 DevOps Concepts Covered

- Container creation from Python Dockerfile
- Mounting custom networks for inter-service comms
- Redis integration via container alias
- Orchestration using `docker-compose.yml`
- Visit count simulates production cache logic

---

## 🧠 Interview Prep

**Q:** Why use Compose over multiple `docker run` commands?  
> _Simplifies orchestration, creates internal DNS, handles dependencies, and supports scaling._

**Q:** How does Flask connect to Redis in Compose?  
> _Via service name `redis` on the shared Compose network. No manual IPs needed._

**Q:** What does `depends_on` do?  
> _Ensures containers launch in order — though it doesn't wait for readiness._

---

## ✅ Final Summary

You now have a complete microservice setup in Docker:
- Flask + Redis linked via Compose
- Custom Dockerfile & .dockerignore for efficient builds
- Named containers, networks, and orchestration in one YAML
- Ready for CI/CD pipelines or sandbox demo

Built by: **Bujji** 🧠  
Stage: Strategic Execution Mode ✔️

---

## ⏭️ Want More?

