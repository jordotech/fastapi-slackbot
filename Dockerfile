FROM python:3.10.11-alpine
COPY ./.bashrc /root/.bashrc
COPY ./app /app
ENV PYTHONPATH=/app
WORKDIR /app
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
CMD ["uvicorn", "main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "80"]
