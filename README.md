# Recipe Recommendation System

## Project Overview

The **Recipe Recommendation System** is designed to offer personalized dietary suggestions for individuals, especially gym enthusiasts, based on their nutritional goals. The system focuses on recommending recipes that align with users' desired macronutrient intake (calories, fat, carbohydrates, protein) and other nutritional factors such as cholesterol, sodium, and fiber. By leveraging machine learning algorithms like K-Nearest Neighbors (KNN) and TF-IDF vectorization, the system ensures that users can maintain their fitness goals while enjoying diverse, exciting, and healthy meal options.

## Key Features
- **Personalized Recipe Recommendations**: Users can input ingredients and get recipe suggestions tailored to their nutritional requirements.
- **Macronutrient and Nutritional Considerations**: Recommendations align with users' macronutrient goals (calories, fat, protein, carbs) as well as micronutrient needs (fiber, sodium, cholesterol).
- **KNN and TF-IDF Machine Learning Approaches**: The system uses KNN to recommend recipes with similar nutritional profiles and TF-IDF to analyze the overlap in ingredient lists, ensuring the most relevant recipe suggestions.

## Project Architecture

The Recipe Recommendation System is developed using Python (Flask) for the backend and HTML/CSS (Bootstrap) for the frontend.

1. **Flask (Backend)**: Handles routing, data processing, and machine learning model integration.
2. **HTML/CSS (Frontend)**: Provides a simple user interface for inputting ingredients and viewing recipe recommendations.
3. **Pandas**: Used for data manipulation and processing of the recipe dataset.
4. **Scikit-learn**: Implements machine learning techniques (KNN, TF-IDF vectorization) for recipe recommendations.

## Machine Learning Techniques

- **K-Nearest Neighbors (KNN)**: This algorithm is employed to identify similar recipes based on their nutritional profiles (calories, fats, proteins, etc.). When users input their ingredients, the system searches for recipes that are nutritionally similar to the user’s goals.
  
- **TF-IDF Vectorization**: This technique analyzes the textual ingredients in the recipes. It calculates the importance of ingredients across all recipes and helps recommend new recipes with similar ingredients that align with the user’s input.

Here’s the updated **Dataset** section with the redirection link included:

### Dataset

The system uses the **RecipeNLG Dataset**, which contains various recipes with detailed ingredient lists, directions, and nutritional information (calories, fats, proteins, carbohydrates, etc.). The dataset can be downloaded from Kaggle [here](https://www.kaggle.com/datasets/paultimothymooney/recipenlg).

The data is processed and transformed to ensure that the recommendations are relevant and nutritionally aligned with the user's input.

## Installation and Setup

### Requirements
- Python 3.x
- Flask
- Pandas
- Numpy
- Scikit-learn
- Bootstrap (for frontend styling)

### Steps

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/recipe-recommendation-system.git
    cd recipe-recommendation-system
    ```

2. **Install Dependencies**:
    Install all required Python libraries by running:
    ```bash
    pip install -r requirements.txt
    ```

3. **Dataset**:
   Download the `RecipeNLG_dataset.csv` and place it in the project root directory.

4. **Run the Application**:
    Start the Flask development server:
    ```bash
    python app.py
    ```

5. **Access the Application**:
   Open a web browser and navigate to `http://127.0.0.1:5000/`.

## Usage

1. Open the application in a web browser.
2. Enter the ingredients you have in the search bar.
3. Click the **Get Recommendations** button.
4. View the list of recommended recipes based on the provided ingredients and click **View Recipe** to see the full recipe on the web.

## Example Usage Scenario

A gym-goer with specific macronutrient goals, for example, high protein and low carbohydrates, can input ingredients such as *chicken breast* and *spinach*. The system will recommend recipes like *Grilled Chicken with Spinach Salad* that meet their nutritional needs while also helping them explore new meal ideas.

## File Structure

```bash
├── app.py                     # Main Flask application file
├── RecipeNLG_dataset.csv       # Recipe dataset file
├── templates
│   └── index.html              # Main HTML template for displaying form and recommendations
├── static
│   └── style.css               # Custom styles (if any)
└── README.md                   # Project documentation
```

## Future Enhancements

- **User Profiles**: Store user preferences and dietary requirements for more personalized recommendations.
- **Nutritional Filters**: Allow users to filter recipes by calories, fat, protein, sodium, etc.
- **Integration with External APIs**: Fetch real-time nutritional data or recipe details from third-party services.

## Conclusion

The **Recipe Recommendation System** is a powerful tool for gym enthusiasts and individuals focused on health and nutrition. It utilizes machine learning to provide highly relevant and personalized recipe suggestions that meet both the user's ingredient input and nutritional goals. This helps users maintain a balanced diet and discover new, satisfying meal options while sticking to their fitness plans.

---

