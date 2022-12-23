from flask import Flask, request
import logging

logging.basicConfig(
    level=logging.info,
    format='%(asctime)s - %(levelname)s - %(message)s', 
    datefmt='%Y-%m-%d %H:%M:%S'
)

app = Flask('log8415-project')
app.logger.setLevel(logging.INFO)
logging.getLogger('werkzeug').setLevel(logging.ERROR)
logging.getLogger('waitress').setLevel(logging.INFO)

@app.route("/ping", methods=["GET"])
def PING() -> tuple[str, int]:
    return 'pong!', 200

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=80)