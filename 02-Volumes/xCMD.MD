👇 Rebuild your image
bash
docker build -t flask-log .
📦 Run With a Volume (on local system)
bash
docker run -p 5000:5000 -v $(pwd):/app flask-log
✔ The container mounts your current folder to /app so logs.txt will appear on your host system.

If you’re inside the O'Reilly Sandbox, bind mounts may not work due to platform restrictions — but named volumes can still be