from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)
CORS(app)

# openai.api_key =   # Use your valid OpenAI API key


@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        text = request.json['text']
        print("Received:", text)

        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            temperature=0,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a strict English teacher. You must be brutally honest. "
                        "If the sentence is grammatically incorrect, say so and provide the corrected version. "
                        "If the sentence does not make sense, say '❌ The sentence is unclear or incorrect.' "
                        "Then suggest a corrected version that conveys a meaningful idea. "
                        "Do not praise correct sentences. Never skip over mistakes."
                    )
                },
                {
                    "role": "user",
                    "content": f"The sentence is: {text}"
                }
            ]
        )

        feedback = response.choices[0].message.content
        return jsonify({"feedback": feedback})

    except Exception as e:
        print("❌ ERROR:", e)
        return jsonify({"feedback": "Server error occurred."}), 500

if __name__ == '__main__':
    app.run(debug=True)