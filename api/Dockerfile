FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8-slim

WORKDIR /catsession
COPY . .
RUN pip install -r requirements.txt
RUN apt-get update 
RUN apt-get install ffmpeg libsm6 libxext6  -y
#ENV PORT 8000
EXPOSE 8080
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]