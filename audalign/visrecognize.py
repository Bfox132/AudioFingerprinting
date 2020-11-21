import cv2
from skimage.metrics import structural_similarity as ssim
from skimage.metrics import mean_squared_error
import matplotlib.pyplot as plt
import numpy as np

from audalign.fingerprint import fingerprint
from audalign.filehandler import read


def visrecognize(target_file_path: str, against_file_path: str):
    # With frequency of 44100
    # Each frame is 0.0929 seconds with an overlap ratio of .5,
    # so moving over one frame moves 0.046 seconds
    # 1 second of frames is 21.55 frames.

    results = {}
    target_samples, _ = read(target_file_path)
    target_arr2d = fingerprint(target_samples, retspec=True)
    transposed_target_arr2d = np.transpose(target_arr2d)

    against_samples, _ = read(against_file_path)
    against_arr2d = fingerprint(against_samples, retspec=True)
    transposed_against_arr2d = np.transpose(against_arr2d)

    # print(f"target max = {np.amax(target_arr2d)}")
    # print(f"against max = {np.amax(against_arr2d)}")

    th, tw = target_arr2d.shape
    ah, aw = against_arr2d.shape

    print(f"Target height: {th}, target width: {tw}")
    print(f"against height: {ah}")
    print(f"length of target: {len(target_arr2d)}")

    m = mean_squared_error(
        transposed_target_arr2d[0:4000], transposed_against_arr2d[0:4000]
    )
    s = ssim(transposed_target_arr2d[0:4000], transposed_against_arr2d[0:4000])

    print(s)
    print(m)

    plot_two_images(target_arr2d, against_arr2d, mse=m, ssim_value=s)

    return results


def visrecognize_directory(target_file_path: str, against_directory: str):
    results = {}
    return results


"""
def mse(imageA, imageB):
    # the 'Mean Squared Error' between the two images is the
    # sum of the squared difference between the two images;
    # NOTE: the two images must have the same dimension
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])

    # return the MSE, the lower the error, the more "similar"
    # the two images are
    return err
"""


def plot_two_images(imageA, imageB, title="Comparison", mse=None, ssim_value=None):
    # setup the figure

    fig = plt.figure(title)
    if mse or ssim_value:
        plt.suptitle(f"MSE: {mse:.4f}, SSIM: {ssim_value:.4f}")
    # show first image
    ax = fig.add_subplot(1, 2, 1)
    plt.imshow(imageA)  # , cmap=plt.cm.gray)
    plt.gca().invert_yaxis()
    # plt.axis("off")
    # show the second image
    ax = fig.add_subplot(1, 2, 2)
    plt.imshow(imageB)  # , cmap=plt.cm.gray)
    plt.gca().invert_yaxis()
    # plt.axis("off")
    # show the images
    plt.show()