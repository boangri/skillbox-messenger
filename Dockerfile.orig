FROM python:3
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
ENV TZ Europe/Moscow
CMD ["python", "./server.py"]
