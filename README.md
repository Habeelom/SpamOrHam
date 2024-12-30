# Spam Email Detector

A machine learning-powered web application that classifies emails as spam or legitimate (ham) using logistic regression. The application provides a clean, intuitive interface for users to paste email content and receive instant classification results.

## Features

- Real-time email content analysis
- Clean, modern user interface
- Responsive design that works on all devices
- Visual feedback with color-coded results
- High accuracy spam detection (96.5% on test data)

## Technologies Used

- **Frontend:** HTML, CSS, Font Awesome
- **Backend:** Flask, Python
- **Machine Learning:** 
  - scikit-learn
  - TF-IDF Vectorization
  - Logistic Regression
- **Data Processing:** pandas, numpy

## How It Works

The application uses a machine learning model trained on a dataset of 5,572 pre-classified emails. The process involves:

1. Text preprocessing using TF-IDF (Term Frequency-Inverse Document Frequency) vectorization
2. Training a logistic regression model on the processed data
3. Real-time classification of user-input email content
4. Visual presentation of results with appropriate styling

## Model Performance

- Training Accuracy: 96.49%
- Testing Accuracy: 96.59%
- Feature Extraction: TF-IDF Vectorization with English stop words removal

## Usage

1. Access the web interface through your browser
2. Paste the email content into the text area
3. Click "Analyze Content"
4. View the classification result with color-coded feedback
   - Green for legitimate emails (ham)
   - Red for spam emails

## Model Training

The model was trained on a dataset containing:
- Total emails: 5,572
- Features: Email message content
- Labels: Spam (0) or Ham (1)
- Training/Test split: 80/20
- scikit-learn community for machine learning tools
