FROM alpine
LABEL \
	maintainer="Davide Alberani <da@mimante.net>"

RUN \
	apk add --no-cache git fortune python3 py3-cffi py3-six py3-requests py3-cryptography py3-pip && \
	pip3 install --break-system-packages python-telegram-bot && \
	cd / && \
	git clone https://github.com/alberanid/fortunes-spam.git
COPY fortunes-spam-bot.py /fortunes-spam

VOLUME /fortunes

WORKDIR /fortunes-spam

ENTRYPOINT ["python3", "fortunes-spam-bot.py"]

