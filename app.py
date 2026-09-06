from flask import Flask, render_template, request

app = Flask(__name__)

items = [
    {
        "name": "Python Programming",
        "category": "Technology",
        "interests": ["python", "coding", "programming", "technology"]
    },
    {
        "name": "Artificial Intelligence",
        "category": "Technology",
        "interests": ["ai", "artificial intelligence", "machine learning", "technology"]
    },
    {
        "name": "Machine Learning",
        "category": "Technology",
        "interests": ["machine learning", "ai", "python", "data science"]
    },
    {
        "name": "Cybersecurity",
        "category": "Technology",
        "interests": ["cybersecurity", "security", "hacking", "technology"]
    },
    {
        "name": "Football",
        "category": "Sports",
        "interests": ["football", "sports", "fitness"]
    },
    {
        "name": "Cricket",
        "category": "Sports",
        "interests": ["cricket", "sports", "fitness"]
    },
    {
        "name": "Gaming",
        "category": "Entertainment",
        "interests": ["gaming", "games", "entertainment"]
    },
    {
        "name": "Music",
        "category": "Entertainment",
        "interests": ["music", "songs", "entertainment"]
    }
]


def calculate_similarity(user_interests, item_interests):
    matches = set(user_interests) & set(item_interests)
    return len(matches)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/recommend", methods=["POST"])
def recommend():

    user_input = request.form.get("interests", "").lower()

    user_interests = [
        interest.strip()
        for interest in user_input.split(",")
        if interest.strip()
    ]

    recommendations = []

    for item in items:

        score = calculate_similarity(
            user_interests,
            item["interests"]
        )

        if score > 0:
            recommendations.append({
                "name": item["name"],
                "category": item["category"],
                "score": score
            })

    recommendations.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return render_template(
        "index.html",
        recommendations=recommendations,
        user_input=user_input
    )


if __name__ == "__main__":
    app.run(debug=True)