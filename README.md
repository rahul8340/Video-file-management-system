# Video-file-management-system

# Django File Upload with FFmpeg Metadata Extraction

## Overview

This project demonstrates a robust file upload system built using Django, integrated with FFmpeg for extracting detailed metadata from uploaded files. It allows users to upload files and view extracted information such as duration, FPS, codec type, bitrate, resolution, and more.

## Features

- **File Upload**: Users can upload files through an intuitive interface.
- **Metadata Extraction**: Automatically extracts and displays video/audio details such as:
  - Duration
  - Frames per second (FPS)
  - Codec type (video and audio)
  - Bitrate
  - Resolution
  - Audio channels
  - Audio sample rate
- **Database Integration**: Extracted data is stored in a database for easy access and retrieval.
- **Dynamic Display**: Uploaded files and their metadata are displayed in a responsive table format.
- **Search Functionality**: Search bar to filter through uploaded files.
- **File Count**: Displays the total number of uploaded files.

## Technologies Used

- **Django**: Backend framework for building the web application.
- **FFmpeg**: Tool for extracting multimedia metadata.
- **HTML/CSS**: For crafting the user interface.
- **MYSQL**: Database for storing file details.

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/django-file-upload-ffmpeg.git
    cd django-file-upload-ffmpeg
    ```

2. **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate
    ```

3. **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Install FFmpeg:**
    - Follow the installation guide for your operating system: https://ffmpeg.org/download.html

5. **Run migrations:**
    ```bash
    python manage.py migrate
    ```

6. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

7. **Visit the application:**
    - Open your web browser and go to `http://127.0.0.1:8000/upload/`

## Usage

1. **Upload a File:**
    - Navigate to the file upload page.
    - Choose a file to upload and provide a description and tags.
    - Click "Upload" to submit the file.

2. **View Uploaded Files:**
    - Uploaded files and their metadata will be displayed in a table.
    - Use the search bar to filter files by name, description, tags, or other metadata.
    - The total count of uploaded files is displayed at the bottom of the table.

## Project Structure
django-file-upload-ffmpeg/
│
├── fileuploadapp/
│ ├── migrations/
│ ├── static/
│ ├── templates/
│ │ └── fileuploadapp/
│ │ ├── upload.html
│ │ └── file_list.html
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── forms.py
│ ├── models.py
│ ├── tests.py
│ └── views.py
│
├── media/
│
├── django_file_upload_ffmpeg/
│ ├── init.py
│ ├── asgi.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
│
├── manage.py
├── requirements.txt
└── README.md
