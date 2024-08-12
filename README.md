# Mushroom Classification Project

This project is a web-based application designed to classify mushrooms as either edible or poisonous based on various features. The application is built using Python and Flask, with a machine learning model trained using `scikit-learn`.

## Project Details

This project uses a trained machine learning model to predict whether a mushroom is edible or poisonous based on the following features:

- **Bruises**: Whether the mushroom has bruises or not.
- **Odor**: The smell of the mushroom.
- **Gill Size**: The size of the mushroom's gills.
- **Gill Color**: The color of the mushroom's gills.
- **Stalk Shape**: The shape of the mushroom's stalk.
- **Spore Print Color**: The color of the mushroom's spore print.
- **Population**: The distribution pattern of the mushroom population.

Users interact with the application by selecting options for each feature, and the model predicts the classification based on the selected inputs.

## Implementation Details

The application is structured using Flask to serve HTML templates and handle user input. The machine learning model and encoders are loaded from pre-trained `pickle` files.

### Project Structure

```plaintext
PoisonousMushroomClassification/
│
├── templates/
│   ├── index.html       # Main form for user input
│   ├── result.html      # Displays the classification result
│
├── static/
│   ├── style/
│   │   └── main.css      # Custom CSS for styling
│   ├── images/           # Optional images for visual representation
│
├── mushroom_classification_UI.py  # Main Flask application
├── finalModel.pkl       # Trained machine learning model
├── ecoders.pkl          # Encoders for categorical features
└── README.md            # Project documentation
```

### Required Python Modules
To run this project locally, you'll need to have Python installed along with the following modules:

Flask: A lightweight WSGI web application framework.
Pandas: A powerful data manipulation and analysis library.
Scikit-learn: A machine learning library for Python.
You can install the necessary packages using pip:

```bash
pip install flask pandas scikit-learn
```

### How it works

1. User Input: The user selects options for various mushroom features on the web page.
2. Data Processing: The selected options are encoded using pre-trained label encoders.
3. Prediction: The encoded data is passed to the machine learning model, which predicts whether the mushroom is edible or poisonous.
4. Result Display: The result is displayed back to the user on a new web page.

### Developed By

This project was developed by **Aditya Goyal** and co-developed by **Sanyam Garg**.
