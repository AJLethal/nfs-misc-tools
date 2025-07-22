#!/usr/bin/env python3

##    MIT License
##
##    Copyright (c) 2025 and later AJ_Lethal
##
##    Permission is hereby granted, free of charge, to any person obtaining a copy
##    of this software and associated documentation files (the "Software"), to deal
##    in the Software without restriction, including without limitation the rights
##    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
##    copies of the Software, and to permit persons to whom the Software is
##    furnished to do so, subject to the following conditions:
##
##    The above copyright notice and this permission notice shall be included in all
##    copies or substantial portions of the Software.
##
##    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
##    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
##    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
##    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
##    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
##    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
##    SOFTWARE.

import tkinter as tk
from tkinter import StringVar
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import io
import struct

sIconData = b'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAACXBIWXMAAC4jAAAuIwF4pT92AAAAB3RJTUUH6QMLER0hw9+oPgAAABl0RVh0Q29tbWVudABDcmVhdGVkIHdpdGggR0lNUFeBDhcAAAK3SURBVDjLpZLPa1R3FMXP/b7ve5M34xuTGSc/YHTMJDZoaAgIraBVNC4UFEF0ryK4KIEicdNuuxHd9B+om9CNuhEKheIiiy5UUkpbZ2EMTEaQmYxP8ubHe2bme7/XTSwuOm78wNncczmbcwiDyQDw8Gn6NMCgG/fu3d4/N3fOWvv/D0R4vbb2hx4QIPVqlQ1zJeX7Tz422JjUdhyPOq47EjUaPCiAdC43vNXpbDy8fv3OR3d1bHHxu/EDB45EtdrLkWIx58DzQL4P8rz/FJw+Tbt8/2gnimJ/bKwlrmuTzU0+c/fut8Pl8uWtel3X19dDq/UWDV+4gHSphGB2FnCcIjnOcVLqq6DROG/ieCgJQ91XatUwPytPTFzMl0rbnWbzYbi+3k/ncjPaDQL4+/b5nCTXlOtehtYvRKnfFDBFvd5UcX4+lxkdWwDkpInj6O+VlWUzOfnznnz+CmcyWZ0pl7VNku/JdfeDeZG0fr5265b94urVw2Lt07BSeZwqFH5wgyDf3dj4KYzjR6PT09SsVlupbDakvUtL35BSy2LtI4hs7nTfHwIuibU2YX7sMp/QnjcR93r3yXF6AKwnctTPZDY0t9tfA8iDyIPIcRBVIHKIC4WRYGZm3DfmEIh6ENFpomsi4hIRk1Kpd41GU5tWqwlraxCZA1EAkSqI+t0keWZFJsWYEogSiKR2qtwGUV+YR/tRVNO22/1VmL8EMP6hawB1dDrSDsMWgH8BWAC0I4FITqydJ8dZ1pTNvunXakscRSlhNpnZWR40/G6lQuQ4c8rzbpLn/Uiu+6cGgD0LC2g8eDAkzFPt1dW0GNOGtW9FJCGAoNRuKDVDWp8g1x2Dtb+QMb+nDh60lD17FuliEQAQrawAxhSEeVqYSxApQGQXFBGUE5JSf5Gj/tl9aiEGgPjVK3w27wGk5j4Z9FpYrgAAAABJRU5ErkJggg=='
lIconData = b'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'

## check for unsaved changes upon being called on opening
def unsavedChanges():
    global dirtyFlag
    if dirtyFlag == 1:
        confirmChanges = messagebox.askyesnocancel("Confirm exit", "You have unsaved changes, do you want to save before exiting?")
        if confirmChanges is None:
            return
        elif confirmChanges:
            saveFile()
            root.destroy()
        else:
            root.destroy()
    else:
        root.destroy() 

## defining main window
root = tk.Tk()
root.title("NFSHS FEDATA Hidden Flag Editor")
root.protocol('WM_DELETE_WINDOW', unsavedChanges)
root.resizable(False, False)
smallIcon = tk.PhotoImage(data=sIconData)
largeIcon = tk.PhotoImage(data=lIconData)
root.iconphoto(False, largeIcon, smallIcon)

## defining frames
mainFrame = ttk.Frame(root, padding=(5,5,10,10))
mainFrame.grid(row = 0, column = 0)
topFrame = ttk.Frame(mainFrame)
topFrame.grid(row = 0, column = 0, padx = '5', pady = '5', columnspan=4)
bottomFrame = ttk.Frame(mainFrame)
bottomFrame.grid(row = 1, column = 0, padx = '5', pady = '5', columnspan=4)

mainFrame.columnconfigure(0, weight=1)
mainFrame.rowconfigure(0, weight=1)
topFrame.columnconfigure(0, weight=1)
topFrame.columnconfigure(1, weight=1)
topFrame.columnconfigure(2, weight=1)
topFrame.columnconfigure(3, weight=1)
bottomFrame.columnconfigure(0, weight=1)
bottomFrame.columnconfigure(1, weight=1)
bottomFrame.columnconfigure(2, weight=1)

## variables
fedataPath = tk.StringVar()
specialFlags = 0
enginePosition = 0
dlcCar = 0
filePathStr = tk.StringVar()
dirtyFlag = 0

spFlagValues = [
                ['Color select: ON / Open top roof: NO',
                'Color select: ON / Open top roof: YES',
                'Color select: OFF / Open top roof: NO',
                'Color select: OFF / Open top roof: YES'],
                [1,2,193,194]
               ]
engPosValues = [
                ["Front",
                 "Mid",
                 "Rear"],
                [0,1,2]
               ]
dlcFlag = [
                ["No",
                 "Yes"],
                [2,6]
               ]

## sets dirty flag for signalling changes to the file
def dirtyFlagSet(*args):
    global dirtyFlag
    dirtyFlag = 1

## "About" dialog
def aboutDlg():
    aboutMsg = messagebox.showinfo("About NFSHS FEDATA Hidden Flag Editor",
                                   "NFSHS FEDATA Hidden Flag Editor v1.2 Rev. A \n"
                                    "(c) 2025 and later AJ_Lethal\n\n"
                                    "Licensed under the MIT License")

## sets fileLabel to active file
def openFileLabel():
    fileLabel['textvariable'] = filePathStr
    filePathStr.set(f'File: {fedataPath}')

## function to open file, read flag values and set them in the fields
def openFile():
    global dirtyFlag
    if dirtyFlag == 1:
        confirmChanges = messagebox.askyesnocancel("Confirm changes", "You have unsaved changes, do you want to save?")
        if confirmChanges is None:
            return
        elif confirmChanges:
            saveFile()
    global fedataPath
    global fedataPathPrev
    if fedataPath != "":
        fedataPathPrev = fedataPath
    fedataPath = filedialog.askopenfilename(title="Open NFSHS FEDATA file", filetypes=[("NFSHS Frontend Data files", "*.eng *.fre *.ger *.ita *.spa *.swe *.bri *.ENG *.FRE *.GER *.ITA *.SPA *.SWE *.BRI")])
    if fedataPath == "":
        fedataPath = fedataPathPrev
        return
    with open (fedataPath, 'rb') as file:
        file.seek(891)
        specialFlags = struct.unpack('B', file.read(1))[0]
        if specialFlags == spFlagValues[1][0]:
            spFlagsCbox.current(0)
        elif specialFlags == spFlagValues[1][1]:
            spFlagsCbox.current(1)
        elif specialFlags == spFlagValues[1][2]:
            spFlagsCbox.current(2)
        else:
            spFlagsCbox.current(3)
        file.seek(955)
        enginePosition = (struct.unpack('B', file.read(1))[0])
        if enginePosition == engPosValues[1][0]:
            engPosCbox.current(0)
        elif enginePosition == engPosValues[1][1]:
            engPosCbox.current(1)
        else:
            engPosCbox.current(2)  
        file.seek(890)
        dlcCar = (struct.unpack('B', file.read(1))[0])
        if dlcCar == dlcFlag[1][0]:
            dlcCbox.current(0)
        else:
            dlcCbox.current(1)
            
    saveButton.state(['!disabled'])
    saveAsButton.state(['!disabled'])
    spFlagsLabel.state(['!disabled'])
    spFlagsCbox.state(['!disabled'])
    spFlagsCbox.state(['readonly'])
    engPosLabel.state(['!disabled'])
    engPosCbox.state(['!disabled'])
    engPosCbox.state(['readonly'])
    dlcLabel.state(['!disabled'])
    dlcCbox.state(['!disabled'])
    dlcCbox.state(['readonly'])

    dirtyFlag = 0
    openFileLabel()

## function to gather values from fields and save the file
def saveFile():
    global dirtyFlag
    global fedataPath
    if fedataPath:
        with open (fedataPath, 'r+b') as file:
            fedataOpen = file.read()
            file.seek(891)
            if spFlagsCbox.current() == 0:
                specialFlags = spFlagValues[1][0]
            elif spFlagsCbox.current() == 1:
                specialFlags = spFlagValues[1][1]
            elif spFlagsCbox.current() == 2:
                specialFlags = spFlagValues[1][2]
            else:
                specialFlags = spFlagValues[1][3]
            file.write(struct.pack('B',specialFlags))
            file.seek(955)
            if engPosCbox.current() == 0:
                enginePosition = engPosValues[1][0]
            elif engPosCbox.current() == 1:
                enginePosition = engPosValues[1][1]
            else:
                enginePosition = engPosValues[1][2]
            file.write(struct.pack('B',enginePosition))
            file.seek(890)
            if dlcCbox.current() == 0:
                dlcCar = dlcFlag[1][0]
            else:
                dlcCar = dlcFlag[1][1]
            file.write(struct.pack('B',dlcCar))
            file.close()

        dirtyFlag = 0
        fileLabel['textvariable'] = filePathStr
        filePathStr.set(f'File saved to: {fedataPath}')
        fileLabel.after(5000, openFileLabel)

## function to gather values from fields and save as another file
def saveFileAs():
    global dirtyFlag
    global fedataPath
    global fedataPathPrev
    fedataSave = filedialog.asksaveasfilename(title="Save NFSHS FEDATA", filetypes=[("NFSHS Frontend Data files", "*.eng *.fre *.ger *.ita *.spa *.swe *.bri *.ENG *.FRE *.GER *.ITA *.SPA *.SWE *.BRI")], defaultextension=[".eng"])
    if fedataSave == "":
        fedataPath = fedataPathPrev
        return
    with open (fedataPath, 'rb') as file:
        fedataOpen = file.read()
        with open (fedataSave, 'wb') as fileSave:
            fileSave.write(fedataOpen)
            fileSave.seek(891)
            if spFlagsCbox.current() == 0:
                specialFlags = spFlagValues[1][0]
            elif spFlagsCbox.current() == 1:
                specialFlags = spFlagValues[1][1]
            elif spFlagsCbox.current() == 2:
                specialFlags = spFlagValues[1][2]
            else:
                specialFlags = spFlagValues[1][3]
            fileSave.write(struct.pack('B',specialFlags))
            fileSave.seek(955)
            if engPosCbox.current() == 0:
                enginePosition = engPosValues[1][0]
            elif engPosCbox.current() == 1:
                enginePosition = engPosValues[1][1]
            else:
                enginePosition = engPosValues[1][2]
            fileSave.write(struct.pack('B',enginePosition))
            file.seek(890)
            if dlcCbox.current() == 0:
                dlcCar = dlcFlag[1][0]
            else:
                dlcCar = dlcFlag[1][1]
                file.write(struct.pack('B',dlcCar))
                
            fileSave.close()
            fedataPath = fedataSave

        dirtyFlag = 0    
        fileLabel['textvariable'] = filePathStr
        filePathStr.set(f'File saved to: {fedataSave}')
        fileLabel.after(5000, openFileLabel)

## defining window buttons
openButton = ttk.Button(topFrame, text="Open", command=openFile)
openButton.grid(row = 0, column = 0)
saveButton = ttk.Button(topFrame, text="Save", command=saveFile, state='disabled')
saveButton.grid(row = 0, column = 1)
saveAsButton = ttk.Button(topFrame, text="Save as...", command=saveFileAs, state='disabled')
saveAsButton.grid(row = 0, column = 2)
aboutButton = ttk.Button(topFrame, text="About", command=aboutDlg)
aboutButton.grid(row = 0, column = 3)
fileLabel = ttk.Label(bottomFrame, textvariable=filePathStr)
fileLabel.grid(row = 0, column = 0, columnspan = 3, sticky="WE", pady=5)
spFlagsLabel = ttk.Label(bottomFrame, text="Special flags", state='disabled')
spFlagsLabel.grid(row = 1, column = 0, sticky="WE")
spFlagsCbox = ttk.Combobox(bottomFrame, values=spFlagValues[0], state='disabled', width=50)
spFlagsCbox.grid(row = 2, column = 0, columnspan = 3, sticky="WE")
engPosLabel = ttk.Label(bottomFrame, text="Engine position", state='disabled')
engPosLabel.grid(row = 4, column = 0, sticky="WE")
engPosCbox = ttk.Combobox(bottomFrame ,values=engPosValues[0], state='disabled')
engPosCbox.grid(row = 5, column = 0, columnspan = 3, sticky="WE")
dlcLabel = ttk.Label(bottomFrame, text="DLC (savedata\cars) car?", state='disabled')
dlcLabel.grid(row = 6, column = 0, sticky="WE")
dlcCbox = ttk.Combobox(bottomFrame ,values=dlcFlag[0], state='disabled')
dlcCbox.grid(row = 7, column = 0, columnspan = 3, sticky="WE")

spFlagsCbox.bind('<<ComboboxSelected>>', dirtyFlagSet)
engPosCbox.bind('<<ComboboxSelected>>', dirtyFlagSet)
dlcCbox.bind('<<ComboboxSelected>>', dirtyFlagSet)

root.mainloop()
