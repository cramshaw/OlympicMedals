FROM python:3.11.4-slim AS base

# Don't write .pyc files
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update

# Avoid installing pipenv in final image
RUN pip install --user pipenv
ENV PIPENV_VENV_IN_PROJECT=1

WORKDIR /usr/src
ADD Pipfile.lock Pipfile ./
# Ensure requirements are regenerated whenever rebuilt
RUN /root/.local/bin/pipenv requirements --dev > requirements.txt
# TODO: split up for dev and prod builds

# Install dev deps
FROM base AS dev

WORKDIR /app
COPY . /app

# Copy pip deps from base
COPY --from=base /usr/src/requirements.txt /app/
# TODO: Improve requirements install
RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["manage.py","runserver","0.0.0.0:8000"]
