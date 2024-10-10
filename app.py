from flask import Flask, render_template, request
import numpy as np
import pandas as pd
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import StandardScaler
from sklearn.feature_extraction.text import TfidfVectorizer
import re  # Import regex for cleaning text

app = Flask(__name__)

# Load the dataset
data = pd.read_csv("RecipeNLG_dataset.csv")

# Preprocess Ingredients
vectorizer = TfidfVectorizer()
X_ingredients = vectorizer.fit_transform(data['NER'])

# Train KNN Model
knn = NearestNeighbors(n_neighbors=5, metric='euclidean')
knn.fit(X_ingredients)

# Function to truncate text
def truncate(text, length):
    if len(text) > length:
        return text[:length] + "..."
    else:
        return text

# Function to ensure links have http/https
def ensure_absolute_url(link):
    if not link.startswith(('http://', 'https://')):
        return 'https://' + link
    return link

# Function to clean and format directions and ingredients
def format_text(text):
    # Remove square brackets and double quotes
    text = re.sub(r'[\[\]"]', '', text)
    return text.strip()

# Recipe recommender function
def recipe_recommender(input_features):
    input_ingredients_transformed = vectorizer.transform([input_features])
    distances, indices = knn.kneighbors(input_ingredients_transformed)
    recommendations = data.iloc[indices[0]]
    
    # Ensure all recipe links are absolute
    recommendations['link'] = recommendations['link'].apply(ensure_absolute_url)
    
    # Format directions and ingredients
    recommendations['directions'] = recommendations['directions'].apply(format_text)
    recommendations['ingredients'] = recommendations['ingredients'].apply(format_text)
    
    return recommendations[['title', 'directions', 'link', 'ingredients']].head(5)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        ingredients = request.form['ingredients']
        recommendations = recipe_recommender(ingredients)
        return render_template('index.html', recommendations=recommendations.to_dict(orient='records'), truncate=truncate)
    return render_template('index.html', recommendations=[])

if __name__ == '__main__':
    app.run(debug=True)
