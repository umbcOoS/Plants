import requests
import os
from requests_toolbelt.multipart.encoder import MultipartEncoder
import mimetypes

maxBytes = 50000000  # 50 MB for requests

api_key = "YOUR_API_KEY"  # Replace with your API key
noReject = False  # Set to True if you want to exclude rejected results

base_url = "https://my.plantnet.org/api/identify/all?organs=auto"  # Replace with the appropriate URL for your use case
main_folder_path = "path/to/main/folder"  # Replace with the path to your main folder
output_files_path = "path/to/output/folder"  # Replace with the path to your output folder
projects = ["all", "the-plant-list"]  # List of projects to query
results_limit = 10  # Number of top results to include in the CSV
max_parallel_queries = 5  # Number of parallel queries to send

tasks = []
results = []


def main():
    sub_folders = os.listdir(main_folder_path)
    for sub_folder in sub_folders:
        sub_folder_path = os.path.join(main_folder_path, sub_folder)
        stats = os.stat(sub_folder_path)
        # exclude non-folders
        if not stats.st_isdir():
            continue
        expected_species_lowercase = sub_folder.replace('_', ' ').lower()
        print('== ' + expected_species_lowercase + ' ==')
        files = os.listdir(sub_folder_path)
        for file_name in files:
            file_path = os.path.join(sub_folder_path, file_name)
            sf_stats = os.stat(file_path)
            # is it another subfolder?
            if sf_stats.st_isdir():
                # multi-images identification request
                print('==== (multi) ' + file_name)
                sub_files = os.listdir(file_path)
                images = []
                for sub_file_name in sub_files:
                    sub_file_path = os.path.join(file_path, sub_file_name)
                    mime_type, encoding = mimetypes.guess_type(sub_file_path)
                    # exclude non-images (JPEG / PNG)
                    if mime_type and mime_type.startswith('image/'):
                        images.append(sub_file_path)
                if images:
                    for project in projects:
                        url = base_url + '&project=' + project + '&noReject=' + str(noReject).lower()
                        organs = ['auto'] * len(images)
                        send_multi_post(url, images, organs, expected_species_lowercase, file_name, project)
            else:
                # single image identification request
                mime_type, encoding = mimetypes.guess_type(file_path)
                # exclude non-images (JPEG / PNG)
                if mime_type and mime_type.startswith('image/'):
                    for project in projects:
                        url = base_url + '&project=' + project + '&noReject=' + str(noReject).lower()
                        organ = 'auto'
                        send_post(url, file_path, organ, expected_species_lowercase, file_name, project)

    # process remaining parallel tasks if any
    if tasks:
        process_tasks()

    # convert to CSV
    csv_data = 'subfolder;image;project;is top1;in top5;rank;genus top1;genus top5;genus rank;match score'  # headers
    for i in range(results_limit):
        csv_data += f';r{i+1} name; r{i+1} score'
    csv_data += '\n'
    for r in results:
        csv_data += ';'.join(r) + '\n'

    # write
    output_file =
