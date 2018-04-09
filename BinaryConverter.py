from tkinter import Frame, Canvas, Button, Label, Menu, Entry #include more tkinter widgets here
from tkinter.filedialog import * 
from tkinter.messagebox import * 

from ColourImage import ColourImage
from BinaryImage import BinaryImage
    
## GUI for binary image creator
class BinaryConverter(Frame):
    
    CANVAS_SIZE = 500  # Square Region size used to display images

    def __init__(self, master=None):

        Frame.__init__(self, master)

        #create left canvas
        self.canvasLeft = Canvas(self.master, background="blue", width=500, height=500, )
        self.canvasLeft.grid(column=1, row=3, sticky="w", columnspan="3")

        #create right canvas
        self.canvasRight = Canvas(self.master, background="green", width=500, height=500)
        self.canvasRight.grid(column=4, row=3, sticky="w", columnspan="3") 

        #set grid layout
        self.grid()  # use the grid manager

        #title for window
        self.master.title("Binary Image Creator")

        menubar = Menu(self)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Open", command=self.openFile)
        filemenu.add_command(label="Save", command=self.saveFile)
        filemenu.add_command(label="Close", command=self.closeApplication)
        menubar.add_cascade(label="File", menu=filemenu)

        #filepath label
        self.filepath = Label(self.master, text=self.openFile)
        self.filepath.grid(column=1, row=2, columnspan=2, sticky="w")

        #filename label
        self.fileName = Label(self.master, text="File: ")
        self.fileName.grid(column=1, row=1, columnspan=2, sticky="w")

        #select threshold option label
        self.thresholdLabel = Label(self.master, text="Select threshold 0-255")
        self.thresholdLabel.grid(column=4, row=2, sticky="w")

        #threshold selection - entry
        self.thresholdEntry = Entry(self.master)
        self.thresholdEntry.insert(0, "97")
        self.thresholdEntry.grid(column=5, row=2, sticky="w")

        #button for processing
        self.thresholdProcess = Button(self.master, text="Process")
        self.thresholdProcess.grid(column=6, row=2, sticky="w")

        self._imagedata = None     # Store here the loaded Image Data, i.e. an object of class GreyScaleImage or ColourImage. 
		                           # This will not change until a new data file is loaded. 
        self._processedData = None # Store here a BinaryImage object that is the result of binarising the loaded data.
        self._pixelSize = 2        # This is used to size the pixels in our display. See method _display()

    def openFile(self):
        self.filechooser = askopenfilename()
        print(self.filechooser[-4:])
        self.vals = []
        self.typeOfImage = ""
        self.threshold = []

        if self.filechooser[-4:] == ".txt":
            try:
                
            except:
                self.filepath.config(text="Invalid: please select appropriate file")

    def saveFile(self):
        file = asksaveasfilename()
        for i in n:
            text = str()
            for n in i:
                text = str(n) + ", "
            file.write(text)
        file.close()

    def closeApplication(self):
        self.master.destroy()
        
    def processThreshold(self):
        self.canvasRight.delete("all")
        if self.threshold.get().firstDigit():
            self.filepath.config(text=self.filechooser)
            if self.typeOfImage == "Greyscale Image":
                self.binaryOutput = GreyScaleImage().BinariseImage(self.vals, self.threshold.get())
                self._display(self.canvasRight, self.binaryOutput)
            elif typeofImage == "Colour Image":
                self.binaryOutput = ColourImage().BinariseImage(self.vals, self.threshold.get())
        else:
            self.filepath.config(text="Invalid: please select appropriate file")

    def _display(self, canvas, inputPts): 
          s = self._pixelSize # renaming so that the last line of this method is shorter and easier to read
          for pt in inputPts:
              [x,y,v]=pt    # x and y are both integers.
                            # v is a string, which comes from the output of _determineColorValue
              canvas.create_rectangle(s*x, s*y, s*(x+1), s*(y+1), fill=v, width=0)
  
if __name__ == "__main__":
    BinaryConverter().mainloop()
