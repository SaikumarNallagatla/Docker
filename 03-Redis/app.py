from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    with open("logs.txt", "a") as f:
        f.write("Visited homepage\n")
    return "✅ Logged visit!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
