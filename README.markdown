# Diploma Project: System Monitoring and Voice Assistant Application

This repository contains the source code for my 2021 diploma project developed during my studies at **RTU MIREA**. The project is a desktop application that includes system monitoring widgets (e.g., CPU temperature) and a voice assistant with various functionalities.

![Application Screenshot](images/screenshot.png)

*Note*: Replace `images/screenshot.png` with the actual screenshot of your application.

## Table of Contents
- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Authentication](#authentication)
- [Running the Application](#running-the-application)
- [Directory Structure](#directory-structure)
- [Notes](#notes)

## Overview
This application provides system monitoring capabilities, including a CPU temperature widget, and integrates a voice assistant for executing commands and managing tasks. It was developed as part of my diploma project in 2021 at RTU MIREA.

## Prerequisites
Before running the application, ensure you have the following:
- Python 3.x installed
- Administrator privileges (required for the CPU temperature widget)
- All dependencies listed in `requirements.txt`

## Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```

2. **Install Dependencies**:
   Install the required Python packages using:
   ```bash
   pip install -r requirements.txt
   ```
   **Note**: Ensure all dependencies are correctly installed. If issues arise, verify the `requirements.txt` file for completeness.

3. **Set Up Environment Variables**:
   Create a `.env` file in the project root with the following content:
   ```plaintext
   API_KEY="xxxxxxxxxxxxxxxxxxxxxxxxxx"
   WEATHER_API_KEY="xxxxxxxxxxxxxxxxxxxxxxxxx"
   ```
   Replace the placeholder values with your actual API keys.

## Configuration
1. **Config Files**:
   - **config.json**: Specify your `base_dir` and other configurations to minimize errors and improve project structure. Example:
     ```json
     {
       "base_dir": "/path/to/your/directory"
     }
     ```
   - **config.csv**: Used for additional configuration settings. Ensure it aligns with your project setup.

2. **Database**:
   - The application uses a `users.db` database for user data.
   - Default credentials are provided (see [Authentication](#authentication)).
   - Optionally, implement a registration window or directly modify `users.db` for new users.

3. **User Data**:
   - The `user_data.pcl` file stores "Remember Me" data for the authentication window.
   - It automatically saves login data (even without selecting "Remember Me") for 8 hours, after which the file is deleted.

## Authentication
To access the application:
- Open the authentication window.
- Enter the default credentials:
  - **Login**: `admin`
  - **Password**: `admin`

**Note**: The application does not currently support user registration. You can extend it by adding a registration window or modifying `users.db` directly.

## Running the Application
1. Ensure the `.env` file and configurations are set up.
2. For the CPU temperature widget, run the application with administrator privileges:
   - On Windows: Right-click `main.py` and select "Run as Administrator."
   - Without admin privileges, the widget may display errors in the console.
3. Start the application:
   ```bash
   python main.py
   ```

## Directory Structure
- **admin_logs/**: Stores logs accessible via the admin panel. Includes data for creating cryptographic keys (e.g., for USB drives) or use pre-existing data.
- **backups/**: Used by the voice assistant for creating file backups.
- **images/**: Contains icons and images used in the application.
- **model/**: Stores models for speech synthesis.
- **results/**: Used by the voice assistant for the neural code editor.
- **sounds/**: System sound files.
- **ui_components/**: Components designed with Qt Designer for the user interface.
- **unique_csv/**: CSV files for generating charts and other data visualizations.
- **voice_assistant/**: Contains functions, commands, and sounds for the voice assistant.
- **widgets/**: Most application widgets. Some widgets are currently in `main.py` but can be restructured for better organization.

## Notes
- The CPU temperature widget requires administrator privileges to function correctly. If errors occur, consider alternative solutions for monitoring system metrics.
- The project can be further structured for better modularity. Contributions are welcome to refactor widgets and other components.
- For API key issues, verify the `.env` file and ensure valid keys are used.