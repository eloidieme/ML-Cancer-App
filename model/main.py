import pandas as pd
from sklearn.base import TransformerMixin
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.pipeline import Pipeline

class ColumnProcessor(TransformerMixin):
    def __init__(self) -> None:
        super().__init__()

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        return X.drop(['Unnamed: 32'], axis=1)

def train_model(X, y):
    pass

def preprocess_data():
    data = pd.read_csv("data/data.csv")
    X = data.drop(['diagnosis'], axis=1)
    y = data['diagnosis']
    X_train, y_train, X_test, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    X_pipeline = Pipeline([
        ('column_processor', ColumnProcessor()),
        ('imputer', SimpleImputer(strategy='median')),
        ('std_scaler', StandardScaler())
    ])
    y_pipeline = Pipeline([
        ('label_encoder', LabelEncoder())
    ])

    X_train = X_pipeline.fit_transform(X_train)
    X_test = X_pipeline.transform(X_test)
    y_train = y_pipeline.fit_transform(y_train)
    y_test = y_pipeline.transform(y_test)

    return X_train, y_train, X_test, y_test

def main():
    X_train, y_train, X_test, y_test = preprocess_data()

    model = train_model(X_train, y_train)

if __name__ == '__main__':
    main()