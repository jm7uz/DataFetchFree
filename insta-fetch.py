from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route('/posts')
def get_posts():
    with open("latest_20_posts.json", "r", encoding="utf-8") as f:
        posts_data = json.load(f)
    return jsonify(posts_data)

if __name__ == '__main__':
    app.run(debug=True)
