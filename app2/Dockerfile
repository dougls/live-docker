FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && \
    apt-get install curl -y

COPY . .

EXPOSE 5000

# RUN chmod +x entrypoint.sh
# ENTRYPOINT ["./entrypoint.sh"]
CMD ["python", "app.py"]