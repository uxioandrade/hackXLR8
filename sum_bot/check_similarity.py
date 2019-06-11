import numpy as np 
from scipy.ndimage import gaussian_filter


def mse(image , test): 

    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
	err /= float(imageA.shape[0] * imageA.shape[1])
	
	return err

def crop(ar, crop_width, copy=False, order='K'):

    ar = np.array(ar, copy=False)
    crops = _validate_lengths(ar, crop_width)
    slices = [slice(a, ar.shape[i] - b) for i, (a, b) in enumerate(crops)]

    if copy:
        cropped = np.array(ar[slices], order=order, copy=True)
    else:
        cropped = ar[slices]
    return cropped



def compute_ssim(x, y, win_size=11, sigma=1.5, L=255, K1=0.01, K2=0.03):
    ''' 
    Structural similarity index as described by Wang et al (read paper for more info)
    '''
    C1 = (K1 * L)**2
    C2 = (K2 * L)**2

    ux = gaussian_filter(x, sigma)
    uy = gaussian_filter(y, sigma)

    uxx = gaussian_filter(x * x, sigma)
    uyy = gaussian_filter(y * y, sigma)
    uxy = gaussian_filter(x * y, sigma)

    vx = uxx - ux * ux
    vy = uyy - uy * uy
    vxy = uxy - ux * uy

    ssim = ((2 * ux * uy + C1) * (2 * vxy + C2)) / ((ux**2 + uy**2 + C1)*(vx + vy + C2))

    pad = (win_size - 1) // 2
    mssim = crop(ssim, pad).mean()

    return mssim, ssim

if __name__ == '__main__':
  img_a = 'hacker-mujer-krfE-U501747500576TDH-624x385@RC.jpg'
  img_b = '0_zGTsdKzkJ4ZHVxJg.jpeg'

  test = compute_ssim(img_a , img_b)
  print(test)
