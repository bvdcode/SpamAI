# Spam Detection API

This project is a simple web API for spam detection using a pre-trained model. It is built with Flask and utilizes the Hugging Face Transformers library for text classification.

## Project Structure

```
spam-detection-api
├── app.py               # Main entry point of the application
├── model_utils.py       # Model loading and prediction logic
├── Dockerfile            # Dockerfile for containerization
├── requirements.txt      # Python dependencies
├── .dockerignore         # Files to ignore in Docker build
└── README.md             # Project documentation
```

## Installation

To run this project locally, you need to have Python installed. You can install the required dependencies using pip:

```
pip install -r requirements.txt
```

## Running the Application

You can run the application using the following command:

```
python app.py
```

The API will be available at `http://127.0.0.1:5000/predict`.

## API Endpoint

### POST /predict

This endpoint accepts a JSON body with the following structure:

```json
{
  "text": "Your text here"
}
```

It returns a JSON response indicating whether the text is classified as spam:

```json
{
  "result": true
}
```

### Downloading the Model

If you want to download the model, you can run the application with the argument `download-model`:

```
python app.py download-model
```

This will download the necessary model files to your local environment.

## Docker Deployment

To build and run the application in a Docker container, use the following commands:

1. Build the Docker image:

```
docker build -t spam-detection-api .
```

2. Run the Docker container:

```
docker run -p 5000:5000 spam-detection-api
```

The API will be accessible at `http://localhost:5000/predict`.

## License

This project is licensed under the MIT License.