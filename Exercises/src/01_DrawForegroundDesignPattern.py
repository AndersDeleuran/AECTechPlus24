import System
import Rhino as rc
import Grasshopper as gh
import GhPython.Assemblies.ExecutingComponent as component

class MyComponent(component):
    
    def RunScript(self,Text,Color):
        
        # Assign input variables
        self.txt = Text
        self.col = Color
        self.black = System.Drawing.Color.Black
        
    def DrawForeground(self,sender,arg):
        
        # Check component preview/locked, active GH document and Rhino viewport
        if (not ghenv.Component.Hidden and not ghenv.Component.Locked
            and ghenv.Component.OnPingDocument() == gh.Instances.ActiveCanvas.Document
            and arg.Viewport.Id == arg.RhinoDoc.ActiveDoc.Views.ActiveView.ActiveViewportID):
            
            # Text is drawn in front of mesh
            pt = rc.Geometry.Point2d(180,300)
            arg.Display.Draw2dText(self.txt,self.black,pt,False,100,"Consolas")
            
            # Rectangle is drawn in front of mesh
            rec2d = System.Drawing.Rectangle(50,300,100,100)
            arg.Display.Draw2dRectangle(rec2d,self.black,10,self.col)
            
    def __enter__(self):
        rc.Display.DisplayPipeline.DrawForeground += self.DrawForeground
        
    def __exit__(self):
        rc.Display.DisplayPipeline.DrawForeground -= self.DrawForeground