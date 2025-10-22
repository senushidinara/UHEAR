from flask import Flask, request, jsonify
from twilio.twiml.voice_response import VoiceResponse
from voice_processor import process_voice
from sms_gateway import process_sms
from backend_storage.points import add_points

app = Flask(__name__)

@app.route("/voice", methods=["POST"])
def voice_input():
    user_id = request.form['From']
    audio_url = request.form['RecordingUrl']
    text = process_voice(audio_url)
    advice, points = process_sms(text, user_id)  # reuse logic for scenario
    add_points(user_id, points)
    resp = VoiceResponse()
    resp.say(advice)
    return str(resp)

@app.route("/sms", methods=["POST"])
def sms_input():
    user_id = request.form['From']
    text = request.form['Body']
    advice, points = process_sms(text, user_id)
    add_points(user_id, points)
    return jsonify({"message": advice, "points": points})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
