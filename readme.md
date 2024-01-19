# SimpleRepo - Debian Repository Generator

SimpleRepo is a simple Python application that creates a Debian repository using Flask. It scans a specified directory for Debian package files (.deb), displays them in a web interface, and provides instructions on how to add the repository to `/etc/apt/sources.list`.

## Features

- Scans a directory for .deb files and displays them in a web interface.
- Generates a repository index file (`Packages.simplerepo`) and stores it in the directory specified.
- Makes the repo available at host:post/repo

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/simplerepo.git
   ```

2. Install dependencies:

   ```bash
   pip install Flask
   ```

3. Navigate to the project directory:

   ```bash
   cd simplerepo
   ```

4. Run the application:

   ```bash
   python main.py
   ```

## Configuration

- Set the `scan_directory` variable in `main.py` to the path where your .deb files are located.
- Configure the `flask_host` and `flask_port` variables in `main.py` according to your preferences.
- Note that Usage below assums not change was made to the configuration

## Usage

1. After running the application, open your web browser and go to:

   ```bash
   http://localhost:5000
   ```

2. The web interface will display a table of available .deb files.

3. To add the repository to `/etc/apt/sources.list`, run the following command:

   ```bash
   echo "deb http://localhost:5000/repo/ /" | sudo tee -a /etc/apt/sources.list
   ```


4. Update the package list:

   ```bash
   sudo apt-get update
   ```

5. You can now install packages from your repository using `apt-get`.

