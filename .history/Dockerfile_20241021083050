# Sử dụng image Python chính thức
FROM python:3.10

# Thiết lập thư mục làm việc
WORKDIR /app

# Sao chép file requirements.txt vào image
COPY requirements.txt .

# Cài đặt các thư viện
RUN pip install -r requirements.txt

# Sao chép mã nguồn ứng dụng vào image
COPY app.py .

# Mở port 5000
EXPOSE 5000

# Chạy ứng dụng
CMD ["python", "app.py"]
