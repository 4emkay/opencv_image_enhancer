FROM python:3.9-alpine

COPY config /home

RUN chmod +x /home/*.sh

WORKDIR usr/src/enhance_api

COPY requirements.txt .
#RUN apt-get install libgl1-mesa-glx

RUN pip install --no-cache-dir -r requirements.txt
COPY . .

ENTRYPOINT ["/home/entrypoint.sh"]
