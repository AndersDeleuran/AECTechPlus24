"""
Draw Meshes with an environment map.
    Inputs:
        Meshes: Meshes to draw {list,mesh}
        Environment: A Rhino native map is selected when value is number, 
        an image on disk is used if value is text/path {item,float or string}
        EdgeWidth: Width of mesh edges {item,float}
        EdgeColor: Color of mesh edges {item,color}
    Outputs:
    Remarks:
        Author: Anders Holden Deleuran (BIG CPH)
        Rhino: 7.37.24107.15001
        Version: 240703
"""

ghenv.Component.Name = "MeshEnvironmentMap"
ghenv.Component.NickName = "EMAP"

import os
import Rhino as rc
import GhPython.Assemblies.ExecutingComponent as component

class MyComponent(component):
    
    def RunScript(self,Meshes,Environment,EdgeWidth,EdgeColor):
        
            # Assign input parameters
            self.meshes = Meshes
            self.edgeWidth = EdgeWidth
            self.edgeColor = EdgeColor
            if Meshes and Environment:
                
                # Get local Rhino environment map to use
                if type(Environment) is float:
                    temFolder = rc.ApplicationSettings.FileSettings.TemplateFolder
                    envFolder = temFolder.replace("Template Files","Environment Maps")
                    envFile =  os.path.join(envFolder,os.listdir(envFolder)[int(Environment)])
                    
                # Or use a string defining file path
                elif type(Environment) is str and os.path.isfile(Environment):
                    envFile = Environment
                    
                # Make display material
                self.dm = rc.Display.DisplayMaterial()
                self.dm.SetBitmapTexture("",True)
                self.dm.SetEnvironmentTexture(envFile,True)
                
    def DrawViewportMeshes(self,arg):
        for m in self.meshes:
            if m:
                arg.Display.DrawMeshShaded(m,self.dm)
                
    def DrawViewportWires(self,arg):
        if self.edgeWidth and self.edgeColor:
            for m in self.meshes:
                if m:
                    arg.Display.DrawMeshWires(m,self.edgeColor,self.edgeWidth)