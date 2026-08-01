FROM python:3.11-slim

# Install system dependencies for Scapy and libpcap
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpcap-dev \
    gcc \
    net-tools \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Pre-train ML models during image build
RUN python ml_models/train_model.py
RUN python scripts/seed_demo_data.py

EXPOSE 5000

ENV PYTHONUNBUFFERED=1
ENV FLASK_ENV=production

CMD ["python", "run.py"]
