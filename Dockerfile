FROM python:2.7

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    git\
    && rm -rf /var/lib/apt/lists/*
WORKDIR /usr/src/app
COPY requirements.txt ./
EXPOSE 5000
RUN pip install -r requirements.txt
RUN git clone https://github.com/davidmon/Fund_Tp1.git

CMD ["python", "Fund_Tp1/run.py"]