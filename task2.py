from flask import Flask, jsonify, request 
from task1 import search, merge, sort, video_titles



# Task 2:

#Develop a REST API endpoint using Flask that allows users to search for videos by their titles using the binary search 
    
#developed in Task 1. This API should accept a search query via query parameter, POST request, or dynamic route, as input and return the matching videos, if any.

app = Flask(__name__)

@app.route("/search", methods=['GET'])
def search():
    title = request.args.get('title')
    
    if not title:
        return jsonify({"error": "Please provide a title to search for."}), 400

    sort(video_titles)

    index = search(video_titles, title)

    if index != -1:
        return jsonify({"message": f"'{title}' found at index {index}."}), 200
    else:
        return jsonify({"message": f"'{title}' not found."}), 404

if __name__ == "__main__":
    app.run(debug=True)