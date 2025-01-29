import os
import tempfile
import subprocess
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/run-tests', methods=['POST'])
def run_tests():
    try:
        # Parse the input JSON
        data = request.json
        script = data.get("script", "")
        tests = data.get("tests", "")

        # Ensure both script and tests are provided
        if not script or not tests:
            return jsonify({"error": "Both script and tests must be provided"}), 400

        # Create a temporary directory to store files
        with tempfile.TemporaryDirectory() as temp_dir:
            script_path = os.path.join(temp_dir, "script.py")
            tests_path = os.path.join(temp_dir, "test_script.py")

            # Write the script and tests to files
            with open(script_path, "w") as script_file:
                script_file.write(script)

            with open(tests_path, "w") as tests_file:
                tests_file.write(tests)

            # Run pytest in the temporary directory
            result = subprocess.run(
                ["pytest", tests_path],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                cwd=temp_dir,
            )

            # Return the output and errors
            return jsonify({
                "stdout": result.stdout,
                "stderr": result.stderr,
                "returncode": result.returncode,
            })
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(host=os.environ.get("HOST", '0.0.0.0'), port=int(os.environ.get("PORT", 5000)))
