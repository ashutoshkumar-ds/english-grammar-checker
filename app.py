from flask import Flask, request, jsonify
from flask_cors import CORS
import openai

app = Flask(__name__)
CORS(app)

openai.api_key = "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"  # Use your valid OpenAI API key

@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        text = request.json['text']
        print("Received:", text)

        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",  # Or gpt-4
            temperature=0,
            messages=[{"role": "user", "content": f"Check this sentence for grammar. Be brutally honest. Highlight mistakes and correct them:\n\n{text}"}]
        )

        feedback = response.choices[0].message.content
        return jsonify({"feedback": feedback})
    except Exception as e:
        print("❌ ERROR:", e)
        return jsonify({"feedback": "Server error occurred."}), 500

if __name__ == '__main__':
    app.run(debug=True)
