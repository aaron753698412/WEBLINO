from flask import Flask, request, Response
import requests

app = Flask(__name__)

@app.route('/', defaults={'path': ''}, methods=['GET', 'POST'])
@app.route('/<path:path>', methods=['GET', 'POST'])
def proxy(path):
    target_url = f"http://youtube.com/{path}"  # Change target URL as needed
    headers = {key: value for key, value in request.headers if key != 'Host'}

    if request.method == 'POST':
        resp = requests.post(target_url, data=request.get_data(), headers=headers)
    else:
        resp = requests.get(target_url, headers=headers)

    return Response(resp.content, status=resp.status_code, headers=dict(resp.headers))

if __name__ == '__main__':
    app.run(port=8080)
