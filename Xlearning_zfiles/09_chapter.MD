```markdown
# 🌀 Step 9 – Kubernetes Deployment for Dockerized Flask App (Bujji Edition)

This guide walks through deploying your Dockerized Flask app (`kajallovessai/flask-bujji:v1`) inside a Kubernetes cluster using declarative YAML files. It includes:

- ✅ Deployment for Pod scheduling
- ✅ Service to expose the app
- ✅ Namespace to isolate resources
- 🧠 DevOps best practices

> **Note:** This sandbox doesn't support `kubectl` or Kubernetes. To run this deployment, switch to a Kubernetes-enabled lab (like Minikube or cloud cluster).

---

## 📁 Folder Structure

```
k8s-flask-deploy/
├── flask-namespace.yaml
├── flask-deployment.yaml
├── flask-service.yaml
└── README.md
```

---

## 🧱 1️⃣ `flask-namespace.yaml`

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: bujji-zone
```

Creates an isolated namespace for the app — useful for multi-project clusters.

---

## ⚙️ 2️⃣ `flask-deployment.yaml`

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: flask-deployment
  namespace: bujji-zone
spec:
  replicas: 2
  selector:
    matchLabels:
      app: flask
  template:
    metadata:
      labels:
        app: flask
    spec:
      containers:
        - name: flask-container
          image: kajallovessai/flask-bujji:v1
          ports:
            - containerPort: 5000
```

- Deploys your Docker image with 2 pods
- Ensures high availability, auto-recovery
- Supports rolling updates and scaling

---

## 🌐 3️⃣ `flask-service.yaml`

```yaml
apiVersion: v1
kind: Service
metadata:
  name: flask-service
  namespace: bujji-zone
spec:
  selector:
    app: flask
  type: NodePort
  ports:
    - port: 80
      targetPort: 5000
      nodePort: 30080
```

- Exposes the Flask app via external port
- Access your app at `http://<node-ip>:30080`
- Load balances requests across replicas

---

## 🚀 Deployment Commands

> Run these after switching to a Kubernetes lab:

```bash
kubectl apply -f flask-namespace.yaml
kubectl apply -f flask-deployment.yaml
kubectl apply -f flask-service.yaml
```

Then check status:
```bash
kubectl get all -n bujji-zone
```

And open the app:
```bash
minikube service flask-service -n bujji-zone --url
```

---

## 🧠 DevOps Principles Applied

| Principle                | How It's Used                                   |
|--------------------------|--------------------------------------------------|
| Infrastructure as Code   | YAML manifests define cluster state             |
| Immutable Deployments    | Docker image tags ensure reproducibility        |
| High Availability        | Replicas and auto-heal via Deployment           |
| Service Discovery        | `NodePort` routes traffic to app containers     |
| Namespace Isolation      | Logical separation of app services              |

---

## 🎯 Interview Nuggets

**Q:** Why use a Kubernetes Deployment?
> Manages rollout, replicas, and health of pods over time.

**Q:** What's the role of a Service?
> Provides a stable access point (IP/port) across ephemeral pods.

**Q:** What does the Namespace do?
> Segments resources — helpful for multi-tenant clusters or staging.

---

## 🔚 Final Notes

This setup lets you:
- Deploy your Flask image anywhere Kubernetes runs
- Scale with traffic
- Roll updates safely
- Expose to external users

Built by **Bujji** 💼  
Tag: `kajallovessai/flask-bujji:v1` 🐳  
Namespace: `bujji-zone`  
Port: `30080`


```