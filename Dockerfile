FROM python:3.11

COPY . .

RUN pip3 install --no-cache-dir -r requirements.txt

ENV PATH="/root/.local/bin:${PATH}"

EXPOSE 8080

CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:app"]