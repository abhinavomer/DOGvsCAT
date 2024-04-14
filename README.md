# Dog vs Cat Image Recognition

This is a simple image recognition app built using Streamlit and TensorFlow. The app takes an image of a dog or a cat as input and predicts whether the image contains a dog or a cat. It also provides the confidence score for the prediction.

## Usage

1. **Upload Image**: Click on the "Browse Files" button to upload an image containing either a dog or a cat.
2. **Prediction**: After uploading the image, click on the "Predict" button to see the predicted class (dog or cat) and the confidence score.

## Requirements

- Python (version 3.x)
- Streamlit (version 0.85.1)
- TensorFlow (version 2.x)
- NumPy
- PIL (Python Imaging Library)

## Installation

1. Clone this repository:

   ```bash
   git clone <repository-url>
2. Install the required Python packages:

- pip install -r requirements.txt
- Download the pre-trained model (dogvscat.h5) and place it in the root directory of the project.

3. Running the App
Run the following command to start the Streamlit app:

- streamlit run app.py
- This will launch the app in your default web browser.

4. Acknowledgements
The pre-trained model used in this app was trained on a dataset containing images of dogs and cats. The model was trained using TensorFlow and is capable of accurately classifying images as either dogs or cats.Model is taken from kaggle.
