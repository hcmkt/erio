FROM python:3.10

ENV TZ=Asia/Tokyo \
  LANG=ja_JP.UTF-8 \
  LANGUAGE=ja_JP:ja \
  LC_ALL=ja_JP.UTF-8

RUN apt-get update \
  && apt-get -y install --no-install-recommends \
    locales \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* \
  && locale-gen ja_JP.UTF-8 \
  && localedef -f UTF-8 -i ja_JP ja_JP.UTF-8 \
  && python3 -m pip install --upgrade pip
