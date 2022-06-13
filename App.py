import tkinter as tk
from tkinter.constants import TOP
import easygui  # to open the filebox
import os
import matplotlib.pyplot as plt
from tkinter.messagebox import showinfo
from Cartoon import Cartoon


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # configure the root window
        self.geometry('400x400')
        self.title('Cartoonify Your Image !')
        self.configure(background='white')

        # Useful variable
        self.__cartoon=None
        self.__images=None
        self.__imagePath=None

        # Create button to cartoonify image()
        self.create_button_cartoonify_image()

    def create_button_cartoonify_image(self):
        """ Button to cartoonify the image"""
        self.button_upload=tk.Button(self,text="Cartoonify an Image",command=self.upload,padx=10,pady=5)
        self.button_upload.configure(background='#364156', foreground='white',font=('calibri',10,'bold'))
        self.button_upload.pack(side=TOP,pady=50)

    
    def upload(self):
        """ Open the box to choose file"""
        self.__imagePath = easygui.fileopenbox()
        self.__cartoon=Cartoon(self.__imagePath)
        self.__images = self.__cartoon.cartoonify()
        self.plotting()

    def plotting(self):
        """ Plotting the whole transition """
        fig, axes = plt.subplots(3, 2, figsize=(8, 8), subplot_kw={
                                'xticks': [], 'yticks': []}, gridspec_kw=dict(hspace=0.1, wspace=0.1))
        for i, ax in enumerate(axes.flat):
            ax.imshow(self.__images[i], cmap='gray')

        save1 = tk.Button(self, text="Save cartoon image", command=lambda: self.save(self.__images[5], self.__imagePath), padx=30, pady=5)
        save1.configure(background='#364156', foreground='white',
                        font=('calibri', 10, 'bold'))
        save1.pack(side=TOP, pady=50)

        plt.show()

    def save(self,ReSized6, ImagePath):
        """ saving an image using imwrite() """  

        newName = "cartoonified_Image"
        path1 = os.path.dirname(ImagePath)
        extension = os.path.splitext(ImagePath)[1]
        path = os.path.join(path1, newName+extension)
        self.__cartoon.save(path,ReSized6)
        I = "Image saved by name " + newName + " at " + path
        showinfo(title=None, message=I)

    

if __name__=="__main__":
    app=App()
    app.mainloop()