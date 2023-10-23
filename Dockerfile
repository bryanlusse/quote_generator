# Use a smaller and more secure base image (Alpine Linux)
FROM python:3.11.6-slim-bullseye

# Create a non-root user to run the application
RUN adduser --system --group appuser

# Set environment variables to control Python and Docker output
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /quote_generator

# Copy just the poetry files first to leverage Docker's build cache
COPY pyproject.toml poetry.lock /quote_generator/

# Install dependencies separately for better caching
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev --no-interaction --no-root

# Copy the rest of the application code
COPY ./quote_gen /quote_generator/quote_gen

# Change the ownership of the /quote_generator directory to the non-root user
RUN chown -R appuser /quote_generator

# Set the user to run the application
USER appuser

# Specify the command to run the application
CMD ["uvicorn", "quote_gen.api.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]