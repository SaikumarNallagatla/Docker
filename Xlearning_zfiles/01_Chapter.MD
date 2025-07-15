# 🧱 Step 1: Introduction to Docker

## 🚀 What is Docker?
Docker is an open-source platform that enables developers to build, package, and deploy applications as containers. Containers are lightweight, portable, and consistent across environments.

## 🌐 Why Docker Matters in Real World
- Ensures code works the same on developer machines and production servers.
- Ideal for CI/CD pipelines, microservices, and scalable cloud apps.
- Used by companies like Netflix, Spotify, and PayPal for fast deployments.

## ⚙️ Core Concepts
| Term            | Description                                                                 |
|-----------------|-----------------------------------------------------------------------------|
| Docker Engine   | Core part that runs and manages containers.                                 |
| Docker Image    | A snapshot of your application and its dependencies.                        |
| Docker Container| A running instance of an image.                                             |

## 🐳 Hands-On in Sandbox
Try these in the Oreilly Docker lab:
```bash
# Run Redis container
docker run redis

# Stop container (use Ctrl + C)

# Show running containers
docker ps

# List images
docker images

# Check Docker version
docker version
