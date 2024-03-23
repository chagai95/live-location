# Dockerfile, Image, Container
# Container with python version 3.10
FROM python:alpine

# Add python file and directory
ADD location.py .
ADD requirements.txt .

# upgrade pip and install pip packages
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt
    # Note: we had to merge the two "pip install" package lists here, otherwise
    # the last "pip install" command in the OP may break dependency resolution...

# run python program
CMD ["python", "location.py"]