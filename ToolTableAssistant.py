## ------------- Libraries
from posixpath import split
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog

## ------------- Functions

def browseTxtFile():
    global TxtFileName
    TxtFileName = filedialog.askopenfilename(initialdir = "/", title = "Select an text template file", filetypes = (("Text files", "*.txt*"), ("All files",".")))
    labelTxtFile.configure(text = "Text file: " + TxtFileName)

def browseMpfFile():
    global MpfFileName
    MpfFileName = filedialog.askopenfilename(initialdir = "/", title = "Select an MPF data file", filetypes = (("MPF files", "*.mpf*"), ("All files",".")))
    labelMpfFile.configure(text = "MPF file: " + MpfFileName)

def browseOutputDirectory(): 
    global outputDirectoryName
    outputDirectoryName = filedialog.askdirectory()
    labelOutputDirectory.configure(text = "Output directory: " + outputDirectoryName)

def convertNum2Name(pdfTxtPath, pdfMpfPath, pdfOutputPath):
    txtFile = open(pdfTxtPath, 'r')
    toolList = txtFile.readlines()  
    toolList2 = [x[:-1] for x in toolList]
    mpfFile = open(pdfMpfPath, 'r')
    mpfData = mpfFile.read()
    for txtLine in toolList2:
        splitToolList = txtLine.split('=')
        print(splitToolList)
        oldTool = splitToolList[0]
        newTool = "T=" + splitToolList[1]
        mpfData = mpfData.replace(oldTool, newTool)
    mpfOutputPath = outputDirectoryName + "Output.mpf"
    mpfOutput = open(mpfOutputPath, "wt")
    mpfOutput.write(mpfData)
    mpfOutput.close()
    labelNum2Name.configure(text = "Files converted")

# ------------- GUI

root = Tk()
root.title("PDF Assistant")
root.geometry('750x750')

label = Label(root, text = "Please select a Text template, MPF data file and output directory").pack()

browseTxtBtn = Button(root, text = "Browse Text files", command = browseTxtFile).pack()

labelTxtFile = Label(root, text = "Select a Text template file")
labelTxtFile.pack()

browseMpfBtn = Button(root, text = "Browse MPF files", command = browseMpfFile).pack()

labelMpfFile = Label(root, text = "Select a MPF data file")
labelMpfFile.pack()

browseOutputDirectoryBtn = Button(root, text = "Browse output directories", command = browseOutputDirectory).pack()

labelOutputDirectory = Label(root, text = "Select an output directory")
labelOutputDirectory.pack()

convertNum2NameBtn = Button(root, text = "Convert selected files", command = lambda: convertNum2Name(TxtFileName, MpfFileName, outputDirectoryName)).pack() 

labelNum2Name = Label(root, text = "Not done yet")
labelNum2Name.pack()

cancelBtn = Button(root, text = 'Cancel', command = root.destroy).pack(side = 'bottom')

root.mainloop()