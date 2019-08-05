FROM python:3.5 as devImage

RUN useradd -ms /bin/bash app
RUN chown -R app:app /usr/src
USER app

ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100

# https://github.com/hadolint/hadolint/wiki/DL4006
SHELL ["/bin/bash", "-o", "pipefail", "-c"]
RUN curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python
ENV PATH="${PATH}:/home/app/.poetry/bin"
ENV MONGO_HOST=mongo \
  MONGO_USERNAME=restaurant_api \
  MONGO_PASSWORD=strong_dev_password

RUN "${HOME}/.poetry/bin/poetry" config settings.virtualenvs.in-project true
EXPOSE 5000
WORKDIR /usr/src

FROM devImage
COPY . ./
RUN poetry install

CMD [".venv/bin/gunicorn", "-c", "src/config/gunicorn.py", "src.backend.main:app"]

