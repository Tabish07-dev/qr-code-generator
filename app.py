from flask import Flask, render_template, request
import base64
from io import BytesIO
import qrcode

app = Flask(__name__)


def generate_qr_code(data: str) -> str:
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    image = qr.make_image(fill_color="black", back_color="white")
    buffer = BytesIO()
    image.save(buffer, format="PNG")
    buffer.seek(0)

    return base64.b64encode(buffer.getvalue()).decode("utf-8")


@app.route("/", methods=["GET", "POST"])
def home():
    qr_image = None
    website_url = ""

    if request.method == "POST":
        website_url = request.form.get("website_url", "").strip()
        if website_url:
            qr_image = generate_qr_code(website_url)

    return render_template(
        "index.html",
        qr_image=qr_image,
        website_url=website_url,
    )


if __name__ == "__main__":
    app.run(debug=True)