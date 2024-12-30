__all__ = ['analyze_rental_data', 'predict_rental_price']

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, cross_val_score
import statsmodels.api as sm
import seaborn as sns
import matplotlib.pyplot as plt

def load_and_prepare_data(filepath):
    # Read CSV file
    data = pd.read_csv(filepath)
    
    # Create feature matrix X and target variable y
    features = ['Size', 'Bedrooms', 'Bathrooms', 'Basement', 
                'Furnished', 'AC', 'Washer/Dryer', 'Pets OK']
    X = data[features]
    y = data['Price']
    
    return data, X, y

def analyze_rental_data(filepath):
    # Load data
    data, X, y = load_and_prepare_data(filepath)
    
    # 1. Basic Statistics
    print("Basic Statistics:")
    print(data.describe())
    print("\nCorrelation with Price:")
    print(data.corr()['Price'].sort_values(ascending=False))
    
    # 2. Multiple Linear Regression with statsmodels
    X_with_const = sm.add_constant(X)
    model = sm.OLS(y, X_with_const).fit()
    print("\nDetailed Regression Results:")
    print(model.summary())
    
    # 3. Cross-validated R-squared score
    X_scaled = StandardScaler().fit_transform(X)
    lr = LinearRegression()
    cv_scores = cross_val_score(lr, X_scaled, y, cv=5, scoring='r2')
    print("\nCross-validated R-squared scores:", cv_scores)
    print("Mean R-squared:", cv_scores.mean())
    
    # 4. Feature importance
    lr.fit(X_scaled, y)
    feature_importance = pd.DataFrame({
        'Feature': X.columns,
        'Standardized Coefficient': lr.coef_
    })
    print("\nFeature Importance (Standardized Coefficients):")
    print(feature_importance.sort_values(by='Standardized Coefficient', ascending=False))
    
    # 5. Visualization of correlations
    plt.figure(figsize=(10, 8))
    sns.heatmap(data[X.columns.tolist() + ['Price']].corr(), annot=True, cmap='coolwarm')
    plt.title('Correlation Heatmap')
    plt.tight_layout()
    plt.show()
    
    return model, lr, StandardScaler().fit(X)

def predict_rental_price(model_lr, scaler, features):
    """
    Predict rental price for new properties
    
    Parameters:
    features: dict or DataFrame with keys/columns matching training data
    """
    if isinstance(features, dict):
        features = pd.DataFrame([features])
    
    features_scaled = scaler.transform(features)
    prediction = model_lr.predict(features_scaled)
    
    return prediction