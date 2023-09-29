from flask import Flask, request, redirect, render_template
import shortuuid

app = Flask(__name__)
url_mapping = {}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/shorten", methods=["POST"])
def shorten_url():
    long_url = request.form.get("url")
    if not long_url:
        return "Invalid URL", 400

    short_url = generate_short_url()
    url_mapping[short_url] = long_url

    return render_template("result.html", short_url=f"{request.host_url}{short_url}")


@app.route("/<short_url>")
def redirect_to_long_url(short_url):
    long_url = url_mapping.get(short_url)
    if long_url:
        return redirect(long_url)
    else:
        return "URL not found", 404


def generate_short_url():
    return shortuuid.uuid()[:8]


if __name__ == "__main__":
    app.run(debug=True)
