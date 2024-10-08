# Step 1: Use Python 3.13.0 as the base image
FROM python:3-alpine3.13

# Step 2: Label the maintainer
LABEL maintainer="ahmedmagdy.tech"

# Step 3: Set environment variables
ENV PYTHONUNBUFFERED=1

# Step 4: Copy the requirements files to a temporary location
COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt

# Step 5: Copy the application code to the container
COPY ./ashtray_meny /ashtray_meny

# Step 6: Create a non-root user
RUN adduser --disabled-password --no-create-home django-user

# Step 7: Change ownership of the working directory
RUN chown -R django-user:django-user /ashtray_meny

# Step 8: Set the working directory
WORKDIR /ashtray_meny

# Step 9: Expose the application port
EXPOSE 7128

# Step 10: Set the argument for development mode
ARG DEV=false

# Step 11: Create a virtual environment
RUN python -m venv /py

# Step 12: Upgrade pip
RUN /py/bin/pip install --upgrade pip

# Step 13: Install PostgreSQL client
RUN apk add --update --no-cache postgresql-client

# Step 14: Install build dependencies
RUN apk add --update --no-cache --virtual .tmp-build-dev \
    build-base postgresql-dev musl-dev

# Step 15: Install Python requirements
RUN /py/bin/pip install -r /tmp/requirements.txt

# Step 16: Install development requirements if in DEV mode
RUN if [ "${DEV}" = "true" ]; then \
    /py/bin/pip install -r /tmp/requirements.dev.txt; \
    fi

# Step 17: Clean up temporary files and remove build dependencies
RUN rm -rf /tmp && \
    apk del .tmp-build-dev

# Step 18: Update the PATH environment variable
ENV PATH="/py/bin:$PATH"

# Step 19: Switch to the non-root user
USER django-user
