import cv2
import numpy as np



class GaborFilter:
    def __init__(self):
        pass

    def get_kernel(self, width, height, sigma, theta, Lambda, gamma, psi):
        """Gabor feature extraction."""
        sigma_x = sigma
        sigma_y = float(sigma) / gamma

        # Bounding box
        nstds = 3  # Number of standard deviation sigma
        c = np.cos(theta)
        s = np.sin(theta) 
        
        if width>0:
            xmax = np.floor(width/2)
        else:
            xmax = max(abs(nstds * sigma_x *c), abs(nstds * sigma_y * s))
            xmax = np.ceil(max(1, xmax))
        
        if height>0:
            ymax = np.floor(height/2)
        else:
            ymax = max(abs(nstds * sigma_x * s), abs(nstds * sigma_y * c))
            ymax = np.ceil(max(1, ymax))

        xmin = -xmax
        ymin = -ymax
    

        scale = 1
        ex = -0.5/(sigma_x**2)
        ey = -0.5/(sigma_y**2)
        cscale = 2*np.pi/ Lambda

        (y, x) = np.meshgrid(np.arange(ymin, ymax + 1), np.arange(xmin, xmax + 1))

        # Rotation
        x_theta = x*c + y*s
        y_theta = -x*s + y*c
        gb = scale*np.exp(ex*(x_theta**2) + ey*(y_theta**2))*np.sin(cscale* x_theta + psi)
        return gb