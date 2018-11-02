FROM alpine
LABEL \
	maintainer="Davide Alberani <da@erlug.linux.it>"

RUN \
	apk add --no-cache git fortune python3 py3-cffi py3-six py3-requests py3-cryptography && \
	pip3 install python-telegram-bot && \
	cd / && \
	git clone https://github.com/alberanid/fortunes-spam.git
COPY fortunes-spam-bot.py /fortunes-spam

WORKDIR /fortunes-spam

ENTRYPOINT ["python3", "fortunes-spam-bot.py"]

