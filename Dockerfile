FROM python:3.7.6-slim-stretch
WORKDIR /app
ADD sygnal/. /app 
RUN pip install gunicorn
RUN pip install "jaeger-client>=4.0.0"
RUN pip install service-identity
RUN python setup.py install
EXPOSE 5000
CMD ["python", "-m", "sygnal.sygnal"]
