"""
Disease information database for plant disease detection system.
"""

disease_info = {
    "Apple___Apple_scab": {
        "common_name": "Apple Scab",
        "scientific_name": "Venturia inaequalis",
        "symptoms": [
            "Dark olive-green spots on leaves",
            "Dark, scabby lesions on fruit",
            "Deformed fruit",
            "Premature leaf drop"
        ],
        "prevention": [
            "Plant resistant varieties",
            "Proper tree spacing for good air circulation",
            "Regular pruning to improve airflow",
            "Clean up fallen leaves in autumn"
        ],
        "risk_factors": [
            "Wet spring weather",
            "Poor air circulation",
            "History of disease in the orchard",
            "Susceptible varieties"
        ]
    },
    "Tomato___Late_blight": {
        "common_name": "Tomato Late Blight",
        "scientific_name": "Phytophthora infestans",
        "symptoms": [
            "Dark brown spots on leaves with white fuzzy growth",
            "Blackened stems with dark streaks",
            "Firm, dark, greasy spots on fruits",
            "Rapid plant collapse in wet conditions"
        ],
        "prevention": [
            "Use disease-resistant varieties",
            "Improve air circulation",
            "Water at the base of plants",
            "Remove infected plants immediately"
        ],
        "risk_factors": [
            "Cool, wet weather",
            "Poor air circulation",
            "Overhead irrigation",
            "Presence of volunteer potato/tomato plants"
        ]
    },
    "Grape___Black_rot": {
        "common_name": "Grape Black Rot",
        "scientific_name": "Guignardia bidwellii",
        "symptoms": [
            "Tan spots with dark borders on leaves",
            "Black, sunken lesions on berries",
            "Mummified fruit",
            "Circular lesions on stems"
        ],
        "prevention": [
            "Remove mummified fruit",
            "Prune for good air circulation",
            "Apply fungicides during growing season",
            "Control weeds around vines"
        ],
        "risk_factors": [
            "Warm, humid weather",
            "Poor sanitation",
            "Inadequate pruning",
            "History of disease"
        ]
    }
}

treatment_info = {
    "Apple___Apple_scab": [
        "Apply protective fungicides early in the growing season",
        "Use copper-based fungicides for organic control",
        "Remove and destroy infected leaves and fruit",
        "Maintain good orchard sanitation"
    ],
    "Tomato___Late_blight": [
        "Apply copper-based fungicides preventatively",
        "Remove and destroy infected plant material",
        "Improve drainage and air circulation",
        "Consider using resistant varieties in future plantings"
    ],
    "Grape___Black_rot": [
        "Apply fungicides according to local recommendations",
        "Practice good sanitation by removing infected material",
        "Maintain open canopy through proper pruning",
        "Time irrigation to minimize leaf wetness duration"
    ]
}
