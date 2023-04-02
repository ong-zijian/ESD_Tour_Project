FROM python:3-slim
WORKDIR /usr/src/app
COPY telegramRequirements.txt ./
RUN python -m pip install --no-cache-dir -r telegramRequirements.txt
CMD [ "python", "./bot.py" ]