```markdown
# ⚙️ Step 3: Mastering Docker Containers – Run, Manage, Name & Persist

Welcome to Chapter 3, future DevOps leader 🚀  
In this section, you’ll **learn how to work with live containers**: how to run, inspect, name, stop, restart, remove them — and how to persist data using volumes. This is where your Docker image comes to life!

By the end, you’ll explain container lifecycle to an interview panel, debug real issues in seconds, and design container setups like a pro.

---

## 🐳 What Are Docker Containers?

A **Docker container** is a live, running instance of your Docker image.  
- Your image is the blueprint 📦  
- The container is the live execution 🖥️  

Think of it like:
> 💡 *Image = recipe*  
> 💡 *Container = baked cake from that recipe*

Containers are isolated from each other, reproducible, and instantly killable or restartable.

---

## 🔄 Lifecycle Commands (With Explanations)

Here’s how we guide our audience 👇

### ▶️ Run a container:
```bash
docker run -d -p 5000:5000 flask-app
```
- `-d`: Run in **detached** mode (in background)
- `-p`: Maps host port 5000 to container port 5000
- `flask-app`: The name of your built image

---

### 📋 See running containers:
```bash
docker ps
```

### 📋 See all containers (including stopped ones):
```bash
docker ps -a
```

### 🛑 Stop a container:
```bash
docker stop <container_id or name>
```

### 🔁 Restart a stopped container:
```bash
docker start <container_id or name>
```

### ❌ Remove a container completely:
```bash
docker rm <container_id or name>
```

---

## 🏷️ Naming Your Container

Naming helps you identify, reference, and automate your workflows.

### ✅ Recommended Format:
```bash
docker run -d --name python-container -p 5000:5000 flask-app
```
Now you can run:
```bash
docker stop python-container
docker start python-container
docker inspect python-container
```

💡 **Tip**: Choose meaningful names — like `auth-service`, `api-v1`, or `flask-staging`

---

## 📦 Adding Volumes for Persistence

Let’s guide our audience through real-world examples.

Without volumes, if the container stops or is removed, your data vanishes. Use volumes to **persist user files, logs, or databases**.

### 🔄 Volume Bind Mount
Mount your current directory into the container:
```bash
docker run -d -p 5000:5000 -v $(pwd):/app flask-app
```

Or on Windows PowerShell:
```bash
docker run -d -p 5000:5000 -v ${PWD}:/app flask-app
```

Now any changes to `app.py` in your local system will instantly reflect inside the container. 🧠

---

## 🧪 Bonus Commands to Explore

### 📌 Rename an existing container:
```bash
docker rename old-name new-name
```

### 🕵️ Inspect container metadata:
```bash
docker inspect python-container
```

### 📦 List all Docker volumes:
```bash
docker volume ls
```

### 📂 Create a named volume:
```bash
docker volume create flask-volume
```

### 🧷 Use a named volume:
```bash
docker run -d -p 5000:5000 -v flask-volume:/app flask-app
```

---

## 🧠 Quiz Questions

1. What happens when a container is removed without using volumes?
2. Why is naming containers useful in scripting or automation?
3. What's the difference between `docker ps` and `docker ps -a`?
4. How do you mount a host directory inside a container?

---

## 💼 Interview Prep

**Q:** What is a container lifecycle in Docker?  
**A:** It includes creation, running, stopping, restarting, and deletion stages. Each is controlled via Docker CLI and essential for CI/CD pipelines.

**Q:** How do volumes work in Docker?  
**A:** Volumes allow data persistence beyond the container’s life. They’re mounted into containers and can be shared or backed up across container runs.

**Q:** Why is `--name` important while running containers?  
**A:** Naming makes it easy to reference containers in scripts, logs, monitoring tools, and during debugging sessions.

---

## 📄 Summary

In this chapter, you’ve:
- Run and managed live containers
- Used lifecycle commands like stop, start, remove
- Named your containers for clarity and scripting
- Added volumes to store persistent data
- Practiced in a sandbox and prepped for interviews

Your containers are no longer just running — they’re strategic. And you? You’re architecting operations like *The Professor* 🧠💣

---

## ⏭️ What's Next?

