import cv2  # for image processing
import numpy as np  # to store image


import sys


class Cartoon:
    def __init__(self,imagePath):
        self.__imagePath=imagePath
        self.__originalImage=None
        self.__grayScaleImage=None
        self.__smoothGrayScale=None
        self.__getEdge=None
        self.__colorImage=None

       
    def readImage(self):
        """ Read Image """ 

        self.__originalImage = cv2.imread(self.__imagePath)
        self.__originalImage = cv2.cvtColor(self.__originalImage, cv2.COLOR_BGR2RGB)
        # print("Original image : \n", originalImage)  # image is stored in form of numbers

        # confirm that image is chosen
        if self.__originalImage is None:
            print("Can not find any image. Choose appropriate file")
            sys.exit()

        ReSized1 = cv2.resize(self.__originalImage, (960, 540))
        #plt.imshow(ReSized1, cmap='gray')

        return ReSized1

    
    def image_to_grayscale(self):
        """ Converting image to grayscale"""

        self.__grayScaleImage = cv2.cvtColor(self.__originalImage, cv2.COLOR_BGR2GRAY)
        ReSized2 = cv2.resize(self.__grayScaleImage, (960, 540))
        #plt.imshow(ReSized2, cmap='gray')

        return ReSized2

    
    def median_blur(self):
        """ Applying median blur to smoothen an image """

        self.__smoothGrayScale = cv2.medianBlur(self.__grayScaleImage, 5)
        ReSized3 = cv2.resize(self.__smoothGrayScale, (960, 540))
        #plt.imshow(ReSized3, cmap='gray')

        return ReSized3

    
    def edges(self):
        """ retrieving the edges for cartoon effect by using thresholding technique """

        self.__getEdge = cv2.adaptiveThreshold(self.__smoothGrayScale, 255,
                                        cv2.ADAPTIVE_THRESH_MEAN_C,
                                        cv2.THRESH_BINARY, 9, 9)

        ReSized4 = cv2.resize(self.__getEdge, (960, 540))
        #plt.imshow(ReSized4, cmap='gray')

        return ReSized4

    
    def bilateral_filter(self):
        """ applying bilateral filter to remove noise and keep edge sharp as required """
        
        self.__colorImage = cv2.bilateralFilter(self.__originalImage, 9, 300, 300)
        ReSized5 = cv2.resize(self.__colorImage, (960, 540))
        #plt.imshow(ReSized5, cmap='gray')

        return ReSized5 

    def masking_edge(self):
        """ masking edged image with our "BEAUTIFY" image """ 

        cartoonImage = cv2.bitwise_and(self.__colorImage, self.__colorImage, mask=self.__getEdge)
        ReSized6 = cv2.resize(cartoonImage, (960, 540))
        #plt.imshow(ReSized6, cmap='gray')

        return ReSized6

    def cartoonify(self):
        """ Transform image to cartoon """
        ReSized1 = self.readImage()
        ReSized2 = self.image_to_grayscale()
        ReSized3 = self.median_blur()
        ReSized4 = self.edges()
        ReSized5 = self.bilateral_filter()
        ReSized6 = self.masking_edge()
        images = [ReSized1, ReSized2, ReSized3, ReSized4, ReSized5, ReSized6]

        return images

    def save(self,path,ReSized6):
        cv2.imwrite(path, cv2.cvtColor(ReSized6, cv2.COLOR_RGB2BGR))