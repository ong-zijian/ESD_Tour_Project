FROM python:3-slim
WORKDIR /usr/src/app
COPY requirements.txt amqp.reqs.txt ./
COPY templates /usr/src/app/templates
COPY static /usr/src/app/static
COPY .env /usr/src/app/
COPY ./payment.py ./invokes.py ./amqp_setup.py ./
RUN python -m pip install --no-cache-dir -r requirements.txt -r amqp.reqs.txt
CMD [ "python", "./payment.py" ]