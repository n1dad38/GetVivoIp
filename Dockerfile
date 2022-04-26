FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN apt update && apt install tzdata -y
ENV TZ="America/Sao_Paulo"

CMD [ "python", "./myIp.py" ]
