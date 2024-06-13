FROM python:3.8


WORKDIR /app




COPY . .
RUN pip install --no-cache-dir -r requirements.txt



EXPOSE 8050


CMD ["python", "app.py"]

