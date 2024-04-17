import Rhino as rc
import GhPython.Assemblies.ExecutingComponent as component
from System.Drawing import Color

class MyComponent(component):
    
    def RunScript(self,Mesh,FrontColor,BackColor,EdgeColor,EdgeWidth):
            
            # Assign input parameters
            self.mesh = Mesh
            self.edgeColor = EdgeColor
            self.edgeWidth = EdgeWidth
            
            # Set front/back colors
            self.material = rc.Display.DisplayMaterial(Color.Black)
            self.material.Emission = FrontColor
            if BackColor:
                self.material.IsTwoSided = True
                self.material.BackDiffuse = Color.Black
                self.material.BackEmission = BackColor
                
    def DrawViewportMeshes(self,arg):
        arg.Display.DrawMeshShaded(self.mesh,self.material)
        
    def DrawViewportWires(self,arg):
        arg.Display.DrawMeshWires(self.mesh,self.edgeColor,self.edgeWidth)