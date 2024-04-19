"""
Capture the Rhino viewport to a PNG file. Places the image in a folder called
Captures in the same directory as the GH definition. Names the image the same as 
the GH defintion followed by _hourMinuteSecond. Note: Do not use this script with
the GH button as this can freeze up the canvas.
    Inputs:
        Width: Width of PNG in pixels {item,int,optional}
        Height: Height of PNG in pixels {item,int,optional}
        Grid: Capture Rhino grid {item,bool,optional}
        Axes: Capture Rhino world axes {item,bool,optional}
        Open: Opens PNG in default application {item,bool,optional}
        Write: Write the captured bitmap to PNG file {item,bool}
    Outputs:
        Path: Path of captured PNG {item,str}
    Remarks:
        Author: Anders Holden Deleuran
        Version: 230830
"""

ghenv.Component.Name = "ViewportCapturePNG"
ghenv.Component.NickName ="VCPNG"

import os
import datetime
import System
import scriptcontext as sc
import Rhino as rc

def checkOrMakeFolder():
    
    """ Check/makes a "Captures" folder in the GH def folder """
    
    if ghdoc.Path:
        folder = os.path.dirname(ghdoc.Path)
        captureFolder = folder + "\\Captures"
        if not os.path.isdir(captureFolder):
            os.makedirs(captureFolder)
        return captureFolder

def makeFileName():
    
    """ Make a string with the gh def name + current hourMinuteSecond """
    
    # Make hour minute seconds string
    n = datetime.datetime.now()
    ho,mt,sc = str(n.hour),str(n.minute),str(n.second)
    if len(ho) == 1:
        ho = "0"+ ho
    if len(mt) == 1:
        mt = "0"+mt
    if len(sc) == 1:
        sc = "0"+ sc
    hms = ho+mt+sc
    
    # Get name of GH def
    ghDef = ghenv.LocalScope.ghdoc.Name.strip("*")
    
    # Concatenate and return
    fileName = ghDef + "_" + hms
    
    return fileName

def captureActiveViewToFile(width,height,path,grid,worldAxes,cplaneAxes):
    
    """ Capture active view to .PNG file at path """
    
    # Define view capture settings (you might want to edit these)
    vc = rc.Display.ViewCapture()
    vc.Width = width
    vc.Height = height
    vc.DrawGrid = grid
    vc.DrawGridAxes = grid
    vc.DrawAxes = worldAxes
    vc.TransparentBackground = False
    vc.ScaleScreenItems = False
    
    # Perform the capture
    try:
        bitmap = vc.CaptureToBitmap(rc.RhinoDoc.ActiveDoc.Views.ActiveView)
        System.Drawing.Bitmap.Save(bitmap,path)
        rc.RhinoApp.WriteLine(path)
        return path
    except:
        raise Exception("Capture failed, check path")

# Capture
if Write:
    if not Width:
        Width = System.Windows.Forms.Screen.PrimaryScreen.WorkingArea.Width  
    if not Height:
        Height = System.Windows.Forms.Screen.PrimaryScreen.WorkingArea.Height
    folder = checkOrMakeFolder()
    fileName = makeFileName()
    try:
        path = os.path.join(folder,fileName + ".png")
        Path = captureActiveViewToFile(Width,Height,path,Grid,Axes,Grid)
        if Open:
            os.startfile(path)
    except:
        raise Exception(" Capture failed, save the GH definition")
else:
    Path = []