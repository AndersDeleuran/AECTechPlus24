"""
Implementation of the Rhino Zebra analysis mode for meshes.
    Inputs:
        Meshes: {list,mesh}
        BackColor: Background color {item,color}
        StripeColor: Color of zebra stripes {item,color}
        EdgeColor: Color of mesh edges {item,color,optional}
        Thickness: Thickness of zebra stripes (0:fat, 6:thin) {item,float}
    Outputs:
    Remarks:
        Author: Anders Holden Deleuran (BIG CPH)
        Rhino: 7.37.24107.15001
        Version: 240702
"""

ghenv.Component.Name = "MeshZebraAnalysis"
ghenv.Component.NickName = "MZA"


import Rhino as rc
import GhPython.Assemblies.ExecutingComponent as component

class MyComponent(component):
    
    def RunScript(self,Meshes,BackColor,StripeColor,EdgeColor,Thickness):
            
            # Assign input parameters
            self.meshes = Meshes
            self.edgeColor = EdgeColor
            self.backColor = BackColor
            
            # Set global stripe properties
            rc.ApplicationSettings.ZebraAnalysisSettings.StripeColor = StripeColor
            rc.ApplicationSettings.ZebraAnalysisSettings.StripeThickness = Thickness
            
    def DrawViewportMeshes(self,arg):
        for m in self.meshes:
            if m:
                arg.Display.DrawZebraPreview(m,self.backColor)
                
    def DrawViewportWires(self,arg):
        if self.edgeColor:
            for m in self.meshes:
                if m:
                    arg.Display.DrawMeshWires(m,self.edgeColor,1)