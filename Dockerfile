FROM python:2.7

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
         git\
    && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install -r requirements.txt
RUN git clone https://github.com/davidmon/Fundamentos_Tp1_Entrega1.git
EXPOSE 5000
CMD ["python", "tp1/run.py", "runserver", "0.0.0.0:5000"]