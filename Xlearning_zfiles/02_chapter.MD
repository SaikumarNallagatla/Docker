Chapter 2

```markdown
# 🐳 Python Flask App with Docker – Full Guide

## 📦 What This Is
A simple yet powerful containerized Python application using Flask, packaged in a Docker image that can run consistently across environments — perfect for DevOps beginners, interview prep, and GitHub portfolios.

---

## 🧾 Project Structure
```
my-python-app/
├── Dockerfile
├── .dockerignore
├── requirements.txt
├── app.py
```

---

## 🔧 Step-by-Step Setup

### 1️⃣ Create `app.py`
```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from Bujji's Python App inside Docker!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

### 2️⃣ Create `requirements.txt`
```
Flask==2.3.2
```

### 3️⃣ Create `.dockerignore`
```
__pycache__/
*.pyc
node_modules
.env
```

### 4️⃣ Create `Dockerfile`
```Dockerfile
# Use official Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files
COPY . .

# Expose the port Flask uses
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]
```

---

## 🐳 Docker Commands

### 🔹 Build the Docker Image
```bash
docker build -t flask-app .
```

### 🔹 View Local Images
```bash
docker images
```

### 🔹 Run the Container
```bash
docker run -p 5000:5000 flask-app
```

### 🔹 Test Locally
Open your browser or API client:
```text
http://localhost:5000
```

You should see:
```text
Hello from Bujji's Python App inside Docker!
```

---

## 🔍 Optional: Inspect the Image
```bash
docker inspect flask-app
```

## 🔥 Troubleshooting Tips
- If `npm: command not found` → You're in the wrong image. Use Python base image, not Node.
- If `invalid syntax` → Ensure no Markdown artifacts like ```python are inside `app.py`.
- If `package.json missing` → Not relevant for Python projects; ensure you're using `requirements.txt`.

---

## 🧠 DevOps Interview Questions

### ❓ Q1: What is a Docker image?
**A:** It’s a template containing everything your app needs to run — code, runtime, dependencies.

### ❓ Q2: Why use Docker for Python apps?
**A:** It eliminates "it works on my machine" issues. Dev, staging, prod environments all behave identically.

### ❓ Q3: What does `EXPOSE` do?
**A:** It documents which port the container listens on. While optional, it’s useful for networking clarity.

---

## ✅ Summary
This project helps you:
- Write a production-ready `Dockerfile` for Python apps
- Understand build → run → inspect flow in Docker
- Practice containerizing with Flask in real-time
- Get ready for DevOps interviews with practical questions

---

## ✨ Next Steps
- Connect this to CI/CD tools like Jenkins or GitHub Actions
- Push your image to Docker Hub
- Scale it using Kubernetes (coming soon in Step 4!)

Happy Dockering 🐳  
Built & maintained by *Charan* – The strategic DevOps architect in training 🔥
```

---
