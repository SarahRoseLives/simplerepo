import os
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

# Specify the directory to scan and the allowed file types
scan_directory = '/home/rose/Downloads'
allowed_file_types = ['.deb']

# Flask app configuration
flask_host = '0.0.0.0'  # Change this to the desired host
flask_port = 5000       # Change this to the desired port

# Scan the directory for allowed file types
repo_files = [f for f in os.listdir(scan_directory) if f.endswith(tuple(allowed_file_types))]
repo_file_info = []

# Function to format file size in a human-readable format
def format_size(size_bytes):
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024.0

# Get additional information for each file
for file in repo_files:
    file_path = os.path.join(scan_directory, file)
    file_info = {
        'name': file,
        'size': format_size(os.path.getsize(file_path)),
        'last_modified': os.path.getmtime(file_path)
    }
    repo_file_info.append(file_info)

# Define the route to serve the repository index
@app.route('/')
def index():
    return render_template('index.html', files=repo_file_info, flask_host=flask_host, flask_port=flask_port)

# Define the route to serve the repository files
@app.route('/repo/<filename>')
def repo(filename):
    return send_from_directory(scan_directory, filename)

# Generate the repository index
def generate_repo_index():
    index_content = "\n".join(repo_files)
    with open(os.path.join(scan_directory, 'Packages.simplerepo'), 'w') as index_file:
        index_file.write(index_content)

# Run the Flask app
if __name__ == '__main__':
    generate_repo_index()
    app.run(host=flask_host, port=flask_port)
