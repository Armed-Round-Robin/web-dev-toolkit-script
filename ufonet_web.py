from flask import Flask, request, render_template_string
import subprocess

app = Flask(__name__)

# Web interface for running UFONet
@app.route("/", methods=["GET", "POST"])
def index():
    output = ""
    if request.method == "POST":
        target_ip = request.form["ip"]
        # Run UFONet with selected target IP
        # Make sure to specify the correct path to your ufonet.py
        try:
            result = subprocess.run(
                ["python3", "ufonet.py", "-x", target_ip],
                capture_output=True,
                text=True
            )
            output = result.stdout
        except Exception as e:
            output = f"Error: {e}"
    return render_template_string('''
        <h2>UFONet Web Control</h2>
        <form method="post">
            Target IP: <input type="text" name="ip" placeholder="Enter target IP">
            <input type="submit" value="Run UFONet">
        </form>
        <pre>{{ output }}</pre>
    ''', output=output)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
