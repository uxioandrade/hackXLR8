################################################################################
#   Project: FastForward
#   File: interface_scrape_frame.py
#   Authors:
#           (c) Uxio Garcia Andrade - uxiog21@gmail.com
#           (c) Xabier Garcia Andrade - xabi.ag.7@gmail.com
#           (c) Alejandro Santorum Varela - alejandro.santorum@gmail.com
#           (c) Borja Docampo Alvarez - bdoc42@gmail.com
#   Date: June 12, 2019
################################################################################

# Importing libraries
from skimage.measure import compare_ssim
from scipy.ndimage import imread
from skimage.transform import resize
import threading as thr
import matplotlib.pyplot
import numpy as np
import youtube_dl
import cv2
import time

# Specify resized image sizes
height = 1024
width = 1024

# Dictionary that links video resolutions with its FPS by default
RES_FPS_DIC = {'144p':30 , '240p':30 , '360p':30 , '480p':30 , '720p60':60 , '1080p60':60}

################################################################################
#   FUNCTION NAME: get_histogram
#   INPUT:
#       · img - image
#   OUTPUT:
#       · histogram of an image
#   DESCRIPTION:
#       · It gets the histogram of an image. For an 8-bit, grayscale image, the
#         histogram will be a 256 unit vector in which the nth value indicates
#         the percent of the pixels in the image with the given darkness level.
#         The histogram's values sum to 1.
################################################################################
def get_histogram(img):
  h, w = img.shape
  hist = [0.0] * 256
  for i in range(h):
    for j in range(w):
      hist[img[i, j]] += 1
  return np.array(hist) / (h * w)


################################################################################
#   FUNCTION NAME: normalize_exposure
#   INPUT:
#       · img - image
#   OUTPUT:
#       · normalized image
#   DESCRIPTION:
#       · It normalizes the exposure of a given image
################################################################################
def normalize_exposure(img):
    img = img.astype(int)
    hist = get_histogram(img)
    # get the sum of vals accumulated by each position in hist
    cdf = np.array([sum(hist[:i+1]) for i in range(len(hist))])
    # determine the normalization values for each unit of the cdf
    sk = np.uint8(255 * cdf)
    # normalize each position in the output image
    height, width = img.shape
    normalized = np.zeros_like(img)
    for i in range(0, height):
        for j in range(0, width):
            normalized[i, j] = sk[img[i, j]]
    return normalized.astype(int)


################################################################################
#   FUNCTION NAME: get_img
#   INPUT:
#       · path - image path
#   OUTPUT:
#       · image
#   DESCRIPTION:
#       · It reads and prepares an image for image processing
################################################################################
def get_img(path, norm_size=True, norm_exposure=False):
    # Flatten returns a 2d grayscale array
    img = matplotlib.pyplot.imread(path).astype(int)
    # Resizing returns float vals 0:255; convert to ints for downstream tasks
    if norm_size:
        img = resize(img, (height, width), anti_aliasing=True, preserve_range=True)
    if norm_exposure:
        img = normalize_exposure(img)
    return img


################################################################################
#   FUNCTION NAME: structural_sim
#   INPUT:
#       · model_img_path - uploaded image path
#       · frame - scraped video frame
#       · resolution (optional) - video resolution
#   OUTPUT:
#       · similarity (float \in [-1,1]) between the model image and the frame
#   DESCRIPTION:
#       · It measures the structural similarity between two images
################################################################################
def structural_sim(model_img, frame):
    sim, diff = compare_ssim(model_img, frame, full=True, multichannel=True)
    return sim


def _get_capture_url(video_url, resolution):
    # Youtube options
    ydl_opts = {}
    # Create youtube-dl object
    ydl = youtube_dl.YoutubeDL(ydl_opts)
    # Set video url, extract video information
    info_dict = ydl.extract_info(video_url, download=False)
    # Get video formats available
    formats_lst = info_dict.get('formats',None)

    for format in formats_lst:
        # Getting the desired resolution
        if format.get('format_note',None) == resolution:
            # Get the video url
            url = format.get('url',None)
            return url
    return None


def search_image(video_url, uploaded_img_path, resolution='144p', tolerance=0.18, n_threads=4):
    seconds_of_coinc_lst = []
    # Getting URL video to capture
    url = _get_capture_url(video_url, resolution)
    if url == None:
        raise ValueError("Unable to get URL video to capture")

    # Open url with OpenCV
    cap = cv2.VideoCapture(url)

    # Check if url was opened
    if not cap.isOpened():
        raise ValueError("Unable to open the given video")

    # Getting uploaded model image
    uploaded_img = get_img(uploaded_img_path)
    # Getting total number of frames
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))


    print("TOTAL FRAMES: ", total_frames)


    # Initializing frame counter
    frame_counter = 0

    while True:
        # Choose desired frame
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_counter)
        # Read frame
        ret, frame = cap.read()
        # Check if frame is empty
        if not ret:
            break

        print("Comparing frames... "+str(frame_counter))
        frame = resize(frame, (height, width, 4), anti_aliasing=True, preserve_range=True)
        # Comparing two images (uploaded image and frame)
        tol = structural_sim(uploaded_img, frame)
        if tol >= tolerance:
            moment_secs = np.floor(frame_counter/RES_FPS_DIC.get(resolution))
            print("COINCIDENCE!!! => Tolerance: "+str(tol)+" At "+str(moment_secs))
            seconds_of_coinc_lst.append(moment_secs)

        # Getting one frame per second
        frame_counter += RES_FPS_DIC.get(resolution)
        if frame_counter >= total_frames:
            break

    # release VideoCapture
    cap.release()
    cv2.destroyAllWindows()
    return seconds_of_coinc_lst



# Testing
if __name__ == "__main__":
    video_url = 'https://www.youtube.com/watch?v=YpSTAF6iNoI'
    model_img_path = "lol_similarity_screenshot.png"

    print(search_image(video_url, model_img_path))
