FROM public.ecr.aws/lambda/python:3.8

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1
# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

COPY requirements.txt  .
RUN python -m pip install --no-cache-dir --upgrade pip && \
    pip3 install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

# Copy function code
COPY app.py ./

# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
# format: file_name.function_name
CMD [ "app.lambda_handler" ] 