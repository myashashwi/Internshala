from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data (replace this with a real news API)
news_data = [
    {"id": 1, "title": "News Article 1", "category": "Tech"},
    {"id": 2, "title": "News Article 2", "category": "Sports"},
    # Add more articles here
]

# Sample user preferences (replace with a real database)
user_preferences = {}

@app.route("/api/news", methods=["GET"])
def get_news():
    # Get user preferences (replace with actual user authentication)
    user_id = request.args.get("user_id")
    preferences = user_preferences.get(user_id, [])

    # Filter news based on user preferences
    personalized_news = [article for article in news_data if article["category"] in preferences]

    return jsonify(personalized_news)

if __name__ == "__main__":
    app.run(debug=True)
