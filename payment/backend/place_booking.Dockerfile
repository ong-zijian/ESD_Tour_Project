FROM python:3-slim
WORKDIR /usr/src/app
COPY requirements.txt ./
#COPY http.reqs.txt amqp.reqs.txt ./
RUN python -m pip install --no-cache-dir -r requirements.txt
COPY ./place_booking.py ./invokes.py ./
# RUN python -m pip install --no-cache-dir -r http.reqs.txt -r amqp.reqs.txt
# COPY ./place_booking.py ./invokes.py ./amqp_setup.py ./
CMD [ "python", "./place_booking.py" ]