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

sIconData = b'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAACXBIWXMAAC4jAAAuIwF4pT92AAAAB3RJTUUH6QMLEiscEO3LAwAAABl0RVh0Q29tbWVudABDcmVhdGVkIHdpdGggR0lNUFeBDhcAAAM6SURBVDjLjZNdaFtlGMf/z3venNOzNE2TLs3H2lrsSkobtbqqzDkEZeiWUVDphUZRpgPxxgu9GYg3vVC8EKYIelO8EARxuA1coR2MKsW1XVsb4weumcFF22xN2nznnPOe9/ViWIZM8Hf7wJ/f8/D8CbcIHX/g+EvRYDSC25BSyqWrS9+nr6fPAZC4AxwAjo4efX7yxcn3Y10xUlC7QyLCxdWLm6kPUhkAV/8zoLuzOxTqDNGl9KVyfiu/qpRijLEDyQeT3r5QXyDRk3g6k898BKD57wANAIQjxryG98iFpQtzp785PT67NnsmeSA5PhAdCMe6YrxULd01/+v8lwCqdzJInHzqZGri8AT6w/0P5Qq5Z5dzy2dNw3R1ruP85fPW1MzUpwAqADy33aIbgMnj4XgCoF7OdEipAl6z/XVGvNyyLG800IPHEo8bH7/2yan8Vv6FarNaFK6wpJIy6Avuv7aZ3SQAnmfGJt6dTL335k6tjGqzKonIbdp1fnDoEDHGAAU0rDoadgOMGEx9D4Tr4Nzi12v8w/vnnLXi3M3phdl6bG9E/LOb5djtxVJVK1Q2YAtbTq+enbtRLvzUYXb0PTk6fuxaYZ1dyS7+weuiPBz3jSULK3++tVK//BcAONJq67+na9KxaGB5fUE8PPgo/zH7SzZ9fXl+MDJs3bfvkHuzVMqeWfjqDTo19NnbjNirjLQvlFJ7AMBVorntz57QGPPWNqRz90jEG/H3cOG64BrHTnMLmfRv+Sjf/wSviGKYwD53lZhhxAYBtIR0buTyv/fqZI70GvGppSs/+Khj8XCn2fVIza6s6DX/UNAI76uJ7VFecUozjrRPAGoYIAaAAfAHWNRlpA2U7MJz7bq/iBZxYTFhqIAiRoWyU/Qx0gq84VanlVI5QOn4H0hI3XKbLzPSVj1MX+SWaImSs5ERygk5ym4T0t5RSlbHgkd2S7G28x2Esk1Onns9zEjpzGhxMt5xhN2kY+FXsLctip8rC8xRdq+Qdlwop1sql+StpzMZWFgjHtEYb3HSpznxb0c6Dtrr5TSozzMMU/PtKnq4By1UPVLJoILqBJQHoAYjViSwiiaMXbNtp4C/AXEWe8V+FIoTAAAAAElFTkSuQmCC'
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
root.title("NFS2/3/HS BNK Horn Loop Tweaker")
root.protocol('WM_DELETE_WINDOW', unsavedChanges)
root.resizable(False, False)
smallIcon = tk.PhotoImage(data=sIconData)
largeIcon = tk.PhotoImage(data=lIconData)
root.iconphoto(False, largeIcon, smallIcon)

## variables
bnkSourcePath = StringVar()
loopStart = tk.IntVar()
loopEnd = tk.IntVar()
sampleLoopStart = 0
sampleLoopEnd = 0
filePathStr = tk.StringVar()
bnkTypeStr = tk.StringVar()
dirtyFlag = 0

## defining frames
mainFrame = ttk.Frame(root, padding=(3,3,12,12))
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

## sets dirty flag for signalling changes to the file
def dirtyFlagSet(*args):
    global dirtyFlag
    dirtyFlag = 1

## "About" dialog
def aboutDlg():
    aboutMsg = messagebox.showinfo("About NFS2/3/HS BNK Horn Loop Tweaker",
                                   "NFS2/3/HS BNK Horn Loop Tweaker v1.1 \n"
                                    "(c) 2025 and later AJ_Lethal\n\n"
                                    "Licensed under the MIT License")

## sets fileLabel to active file
def openFileLabel():
    fileLabel['textvariable'] = filePathStr
    filePathStr.set(f'File: {bnkSourcePath}')

## function to validate characters inputted in text boxes
def inputCallback(input):
    if input.isdigit() and len(input) <= 5:
        dirtyFlagSet()
        return True
    
    elif input == "":
        return True

    else:
        return False
            
## function to open and load BNK file
def openFile():
    global bnkSourcePath
    global bnkSourcePathPrev
    global dirtyFlag
    if dirtyFlag == 1:
        confirmChanges = messagebox.askyesnocancel("Confirm changes", "You have unsaved changes, do you want to save?")
        if confirmChanges is None:
            return
        elif confirmChanges:
            saveFile()
    if bnkSourcePath != "":
        bnkSourcePathPrev = bnkSourcePath
    bnkSourcePath = filedialog.askopenfilename(title="Open NFS2/3/HS .bnk file", filetypes=[("NFS2/3/HS sound bank", "*.bnk")])
    if bnkSourcePath == "":
        bnkSourcePath = bnkSourcePathPrev
        return
    readOffsets()
    with open (bnkSourcePath, 'rb') as file:
        file.seek(sampleLoopStart)
        loopStart.set(struct.unpack('>H', file.read(2))[0])
        file.seek(sampleLoopEnd)
        loopEnd.set(struct.unpack('>H', file.read(2))[0])

    saveButton.state(['!disabled'])
    saveAsButton.state(['!disabled'])
    startLabel.state(['!disabled'])
    startInput.state(['!disabled'])
    endLabel.state(['!disabled'])
    endInput.state(['!disabled'])
    
    openFileLabel()

## function to read file offsets to determine game type and horn sample loop offsets
def readOffsets():
    global bnkSourcePath
    global sampleLoopStart
    global sampleLoopEnd
    if bnkSourcePath:
        with open (bnkSourcePath, 'rb') as file:
            s = file.read()
            sStartPos = 0
            sampleInfoStart = 0
            sampleInfoEnd = 0
            loopsample = 0
            file.seek(0)
            ## checks if it's a NFSHS BNK file, else it will assume it's a NFS2/3 BNK
            if s.find(b'\xFF\xFF\xFF\xFF', 16, 24) != -1:
                typeLabel['textvariable'] = bnkTypeStr
                bnkTypeStr.set('BNK type: NFSHS')
                while sampleInfoStart != -1 and loopsample < 2:
                    sampleInfoStart = s.find(b'\x50\x54\x00\x00', sStartPos)
                    sStartPos = sampleInfoStart + 1
                    sampleInfoEnd = s.find(b'\x93\x04\x00\x00\x00\x00\xFF', sStartPos) + 6
                    sampleLoopStart = s.find(b'\x86\x02', sStartPos, sampleInfoEnd) + 2
                    sampleLoopEnd = s.find(b'\x87\x02', sStartPos, sampleInfoEnd) + 2
                    loopsample = loopsample + 1

                    sampleInfoStart = s.find(b'\x50\x54\x00\x00', sStartPos)
                
            else:
                typeLabel['textvariable'] = bnkTypeStr
                bnkTypeStr.set('BNK type: NFS2/3')
                while sampleInfoStart != -1 and loopsample < 2:
                    while sampleInfoStart != -1 and loopsample < 4:
                        sampleInfoStart = s.find(b'\x50\x54\x00\x00', sStartPos)
                        sStartPos = sampleInfoStart + 1
                        sampleInfoEnd = s.find(b'\x8a\x04\x00\x00\x00\x00', sStartPos) + 5
                        sampleLoopStart = s.find(b'\x86\x02', sStartPos, sampleInfoEnd) + 2
                        sampleLoopEnd = s.find(b'\x87\x02', sStartPos, sampleInfoEnd) + 2
                        loopsample = loopsample + 1
                        
                        sampleInfoStart = s.find(b'\x50\x54\x00\x00', sampleInfoEnd)

## function to gather values from fields and save the file
def saveFile():
    global dirtyFlag
    if bnkSourcePath:
        with open (bnkSourcePath, 'r+b') as file:
            bnkOpen = file.read()
            file.seek(sampleLoopStart)
            file.write(struct.pack('>H',loopStart.get()))
            file.seek(sampleLoopEnd)
            file.write(struct.pack('>H',loopEnd.get()))
            file.close()

        dirtyFlag = 0
        fileLabel['textvariable'] = filePathStr
        filePathStr.set(f'File saved to: {bnkSourcePath}')
        fileLabel.after(5000, openFileLabel)

## function to gather values from fields and save as another file
def saveFileAs():
    global dirtyFlag
    global bnkSourcePath
    global bnkSourcePathPrev
    bnkSave = filedialog.asksaveasfilename(title="Save NFSHS .bnk file as", filetypes=[("NFSHS sound bank", ".bnk")], defaultextension=".bnk")
    if bnkSave == "":
        bnkSourcePath = bnkSourcePathPrev
        return
    if bnkSave:
        with open (bnkSourcePath, 'rb') as file:
            bnkOpen = file.read()
            with open (bnkSave, 'wb') as fileSave:
                fileSave.write(bnkOpen)
                fileSave.seek(sampleLoopStart)
                fileSave.write(struct.pack('>H',loopStart.get()))
                fileSave.seek(sampleLoopEnd)
                fileSave.write(struct.pack('>H',loopEnd.get()))
                fileSave.close()
                bnkSourcePath = bnkSave
                
        dirtyFlag = 0
        fileLabel['textvariable'] = filePathStr
        filePathStr.set(f'File saved to: {bnkSave}')
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
startLabel = ttk.Label(bottomFrame, text="Loop start (samples)", state='disabled')
startLabel.grid(row = 1, column = 0, sticky='W')
startInput = ttk.Entry(bottomFrame, textvariable=loopStart, state='disabled')
startInput.grid(row = 2, column = 0, sticky='W')
typeLabel = ttk.Label(bottomFrame, textvariable=bnkTypeStr, width=20, anchor="center")
typeLabel.grid(row = 2, column = 1, sticky='WE', padx=5)
endLabel = ttk.Label(bottomFrame, text="Loop end (samples)", state='disabled')
endLabel.grid(row = 1, column = 2, sticky='E')
endInput = ttk.Entry(bottomFrame, textvariable=loopEnd, state='disabled', justify="right")
endInput.grid(row = 2, column = 2, sticky='E')

## calls the input validation and sets its parameters (only numbers allowed)
reg = root.register(inputCallback)
startInput.config(validate="key", validatecommand=(reg, '%P'))
endInput.config(validate="key", validatecommand=(reg, '%P'))

root.mainloop()
