# Diabetes Prediction Web App

A web application for predicting diabetes risk using machine learning with an easy, interactive interface.

## Overview

This project utilizes Python libraries such as **NumPy**, **Pandas**, **Seaborn**, and **Scikit-learn** for data cleaning, visualization, and model building. The web front-end is powered by **Flask**, allowing users to enter personal health metrics and get instant predictions on diabetes risk.

## Features

- **Interactive Web Interface**: Simple and fast predictions for users
- **Comprehensive ML Pipeline**: Data exploration, preprocessing, training, and prediction
- **Visualizations**: Built-in analysis with Seaborn and Pandas
- **Pre-trained Model**: Quick results using a deployed ML model
- **Extensible Structure**: Ready for updates with new data or additional features

## Demo

Try the live app:  
[diabetes-prediction-web-app-2j21.onrender.com](https://diabetes-prediction-web-app-2j21.onrender.com/)

## Tech Stack

- Python
- Jupyter Notebook
- NumPy
- Pandas
- Seaborn
- Scikit-learn
- Flask

## Project Structure

```
static/                      # Assets (CSS, images, etc.)
templates/                   # HTML templates for Flask
Diabetes Prediction Web App.ipynb    # Notebook: EDA & model training
diabetes.csv                 # Dataset for model training
app.py                       # Flask app entry point
diabetes_model.pkl           # Saved ML model for prediction
scaler.pkl                   # Feature scaler for user input
requirements.txt             # Package dependencies
```

## Getting Started

### Prerequisites

- Python 3.x
- Packages listed in `requirements.txt`

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/jesyvinoliyaj-design/Diabetes-Prediction-Web-App.git
   cd Diabetes-Prediction-Web-App
   ```

2. **Install required packages:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app locally:**

   ```bash
   python app.py
   ```

4. **Open the browser:**  
   Go to `http://127.0.0.1:5000`

## File Descriptions

- `Diabetes Prediction Web App.ipynb` - Data exploration, feature engineering, and training notebook.
- `diabetes.csv` - Dataset containing health metrics and diabetes status.
- `app.py` - Backend Flask logic for serving predictions.
- `diabetes_model.pkl` - Trained ML model for inference.
- `scaler.pkl` - Scaler object for input normalization.
- `requirements.txt` - Python dependency list.

## Contributing

Feel free to fork the project, submit issues, or send pull requests to help improve the app.

## License

Unlicensed. For commercial use or questions, please contact the repository author.

***

**Author:** [jesyvinoliyaj-design](https://github.com/jesyvinoliyaj-design)

***

[1](https://github.com/jesyvinoliyaj-design/Diabetes-Prediction-Web-App)
