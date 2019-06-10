import io
import os
import requests

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

from googleapiclient.http import MediaIoBaseDownload

def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "0"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "client_secret.json"

    # Get credentials and create an API client
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey='AIzaSyCb5APsEU1wXEX77u1x-wjgb6cdu8twJyE')
    '''
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)
    '''
    request = youtube.captions().download(
        id="aKEjCC_x9w0gnNkJ_FqkfyPFtTJkdHF6idIXt8R13kg"
    )
    # TODO: For this request to work, you must replace "YOUR_FILE"
    #       with the location where the downloaded content should be written.
    fh = io.FileIO("downloaded_transcript.txt", "wb")

    download = MediaIoBaseDownload(fh, request)
    complete = False
    while not complete:
      status, complete = download.next_chunk()


if __name__ == "__main__":
    main()
