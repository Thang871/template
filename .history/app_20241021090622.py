from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "!CHÀO MỪNG BẠN ĐẾN VỚI THỜI TRANG BLOG APP"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
