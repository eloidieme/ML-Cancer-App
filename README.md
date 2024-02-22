## ML Breast Cancer App

The app can be accessed at: 

This is a Streamlit App that uses logistic regression to predict if a breast mass might be benign or malignant. It has been made for learning purposes and not for real-world use. The goal was to learn how to make and deploy a streamlit app.

### Getting Started

#### Requirements
- Python == 3.11

#### Installing
Quick setup (use of venv recommended)
```
git clone https://github.com/eloidieme/ML-Cancer-App.git
cd ML-Cancer-App
python -m venv .venv
. ./.venv/bin/activate
pip install -r requirements.txt
```

#### Executing program
```
streamlit run app/main.py
```

### Description of the dataset

Features are computed from a digitized image of a fine needle aspirate (FNA) of a breast mass. They describe characteristics of the cell nuclei present in the image.

Attribute Information:

1. ID number
2. Diagnosis (M = malignant, B = benign)

Ten real-valued features are computed for each cell nucleus:

* radius (mean of distances from center to points on the perimeter)
* texture (standard deviation of gray-scale values)
* perimeter
* area
* smoothness (local variation in radius lengths)
* compactness ($perimeter^2 / area - 1.0$)
* concavity (severity of concave portions of the contour)
* concave points (number of concave portions of the contour)
* symmetry
* fractal dimension ("coastline approximation" - 1)

The mean, standard error and "worst" or largest (mean of the three
largest values) of these features were computed for each image,
resulting in 30 features.

All feature values are recoded with four significant digits.

Missing attribute values: none.

Class distribution: 357 benign, 212 malignant.

### Authors

* Eloi Dieme