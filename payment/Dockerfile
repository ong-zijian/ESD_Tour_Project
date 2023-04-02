FROM python:3-slim
WORKDIR /usr/src/app
COPY requirements.txt ./
COPY templates /usr/src/app/templates
COPY static /usr/src/app/static
COPY .env /usr/src/app/
RUN python -m pip install --no-cache-dir -r requirements.txt
COPY ./payment.py ./
CMD [ "python", "./payment.py" ]