import Rhino as rc
import Grasshopper as gh
import System.Drawing as sd
import GhPython.Assemblies.ExecutingComponent as component

class MyMouseCallback(rc.UI.MouseCallback):
    
    def __init__(self):
        self.down = None
        
    def OnMouseDown(self,arg):
        self.down = arg
        ghenv.Component.ExpireSolution(True)

class MyComponent(component):
    
    def RunScript(self,Text,Color):
        self.txt,self.c1,self.c2 = Text,Color,sd.Color.Black
        
    def DrawForeground(self,sender,arg):
        if (not ghenv.Component.Hidden and not ghenv.Component.Locked 
            and ghenv.Component.OnPingDocument() == gh.Instances.ActiveCanvas.Document
            and arg.Viewport.Id == arg.RhinoDoc.ActiveDoc.Views.ActiveView.ActiveViewportID):
            
            # Define rectangle swatch to draw
            rec = sd.Rectangle(50,100,100,100)
            
            # Check if left mouse button is clicked and inside rectangle 
            leftClicked = False
            if self.mouse.down:
                if self.mouse.down.MouseButton == rc.UI.MouseButton.Left:
                    mx,my = self.mouse.down.ViewportPoint.X,self.mouse.down.ViewportPoint.Y
                    if rec.X + rec.Width > mx > rec.X and rec.Y + rec.Height > my > rec.Y:
                        leftClicked = True
                    
            # Draw left clicked or normal state
            if leftClicked:
                recPt = rc.Geometry.Point2d(rec.X + rec.Width+10,rec.Y)
                arg.Display.Draw2dRectangle(rec,self.c2,10,sd.Color.DodgerBlue)
                arg.Display.Draw2dText(self.txt,self.c2,recPt,False,100,"Consolas")
            else:
                arg.Display.Draw2dRectangle(rec,self.c2,10,self.c1)
                
    def __enter__(self):
        rc.Display.DisplayPipeline.DrawForeground += self.DrawForeground
        self.mouse = MyMouseCallback()
        self.mouse.Enabled = True
        
    def __exit__(self):
        rc.Display.DisplayPipeline.DrawForeground -= self.DrawForeground
        self.mouse.Enabled = False
        del self.mouse