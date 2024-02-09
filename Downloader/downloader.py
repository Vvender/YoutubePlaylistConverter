import os
import re
import threading
import pytube
from ExceptionHandler.exception_handler import CustomExceptionHandler
from PyQt5.QtWidgets import QFileDialog
from moviepy.editor import VideoFileClip


def select_location(main_window):
    try:
        location = QFileDialog.getExistingDirectory(main_window.ui_window, "Select Directory")
        if location:
            main_window.ui.lbl_file_location.setText(location)
    except Exception as e:
        CustomExceptionHandler("Select Location", e)


def update_progress(main_window, current, total, message=None):
    try:
        if message is not None:
            main_window.ui.lbl_info_message.setText(message)
        else:
            main_window.ui.lbl_info_message.setText(f"Play List Progress: {current}/{total}")
    except Exception as e:
        CustomExceptionHandler("Update Progress", e)


def download_video(main_window, video, resolution, download_location, current, total):
    try:
        print("download video")

        # Get all available streams sorted by resolution in descending order
        available_streams = video.streams.filter(progressive=True).order_by('resolution').desc()

        # Find the first stream that matches or has a higher resolution than the selected resolution
        selected_stream = None
        for stream in available_streams:
            if stream.resolution >= resolution:
                selected_stream = stream
                break

        if selected_stream:
            # Sanitize the filename before saving
            sanitized_filename = sanitize_filename(video.title)

            # Download the selected stream
            selected_stream.download(output_path=download_location, filename=sanitized_filename + ".mp4")

            # Update progress
            update_progress(main_window, current, total)

            # Convert to MP3
            convert_to_mp3(os.path.join(download_location, sanitized_filename))
        else:
            highest_resolution_stream = available_streams.first()
            if highest_resolution_stream:
                # Sanitize the filename before saving
                sanitized_filename = sanitize_filename(video.title)
                # Download the highest resolution stream
                highest_resolution_stream.download(output_path=download_location, filename=sanitized_filename + ".mp4")
                # Update progress
                update_progress(main_window, current, total)
                # Convert to MP3
                convert_to_mp3(os.path.join(download_location, sanitized_filename))
            else:
                print(f"No streams available for '{video.title}'.")
                return
            print(
                f"No suitable stream found for '{video.title}' with resolution {resolution} or higher. Downloading the highest available resolution: {highest_resolution_stream.resolution}.")
    except Exception as e:
        CustomExceptionHandler("Download Video", e)


def download_videos(main_window, playlist, resolution, download_location):
    try:
        num_videos = len(playlist.video_urls)
        main_window.ui.pages.setCurrentIndex(1)

        for i, video in enumerate(playlist.videos, start=1):
            download_video(main_window, video, resolution, download_location, i, num_videos)

            # Check if it's the last video
            if i == num_videos:
                update_progress(main_window, i, num_videos, "Download Completed")

    except Exception as e:
        CustomExceptionHandler("Download Videos", e)


def download_playlist(main_window):
    try:
        url = main_window.ui.lineEdit_url.text()
        resolution = get_selected_resolution(main_window)
        download_location = main_window.ui.lbl_file_location.text()
        playlist = pytube.Playlist(url)
        thread = threading.Thread(target=download_videos, args=(main_window, playlist, resolution, download_location))
        thread.start()

    except Exception as e:
        CustomExceptionHandler("Download Playlist", e)


def get_selected_resolution(main_window):
    try:
        if main_window.ui.rb_2160p.isChecked():
            return "2160p"
        elif main_window.ui.rb_1080p.isChecked():
            return "1440p"
        elif main_window.ui.rb_1080p.isChecked():
            return "1080p"
        elif main_window.ui.rb_720p.isChecked():
            return "720p"
        elif main_window.ui.rb_480p.isChecked():
            return "480p"
        elif main_window.ui.rb_360p.isChecked():
            return "360p"
        else:
            # Default resolution
            return "360p"
    except Exception as e:
        CustomExceptionHandler("Get Select resolution", e)


def sanitize_filename(filename):
    # Remove the single quote character
    filename = re.sub(r'[\\:*?"<>|]', '', filename)
    sanitized_filename = filename.replace("'", "")
    return sanitized_filename


def convert_to_mp3(input_filename):
    try:
        # Construct the input filename with the correct path and extension
        input_filename_with_extension = input_filename + ".mp4"

        # Load the video clip using the input filename
        clip = VideoFileClip(input_filename_with_extension)

        # Construct the output filename for the MP3 file
        output_filename = os.path.splitext(input_filename_with_extension)[0] + ".mp3"

        # Write the audio to an MP3 file
        clip.audio.write_audiofile(output_filename)
        clip.close()

        # Delete the original MP4 file
        delete_mp4(input_filename_with_extension)

    except Exception as e:
        CustomExceptionHandler("convert_to_mp3", e)


def delete_mp4(filename):
    try:
        os.remove(filename)
    except Exception as e:
        CustomExceptionHandler("delete_mp4", e)
