import Rhino as rc
import Grasshopper as gh
import System.Drawing.Color as dc
import GhPython.Assemblies.ExecutingComponent as component

class MyComponent(component):
    
    def RunScript(self,Radius):
        self.rad = Radius
        
    def get_ClippingBox(self):
        return rc.RhinoDoc.ActiveDoc.Views.ActiveView.ActiveViewport.GetFrustumBoundingBox()
        
    def DrawForeground(self,sender,arg):
        if (not ghenv.Component.Hidden and not ghenv.Component.Locked
            and ghenv.Component.OnPingDocument() == gh.Instances.ActiveCanvas.Document
            and arg.Viewport.Id == arg.RhinoDoc.ActiveDoc.Views.ActiveView.ActiveViewportID):
            
            # Get frustum line/camera plane at top left corner
            r1,fl = arg.Viewport.GetFrustumLine(0,0)
            r2,cf = arg.Viewport.GetCameraFrame()
            pt = fl.PointAt(0.5)
            cf.Origin = pt
            
            # Get and print scaling factor to divide by
            r3,s = arg.Viewport.GetWorldToScreenScale(pt)
            
            # Draw concentric circles
            for i in range(10,500,10):
                crc = rc.Geometry.Circle(cf,i*self.rad/s)
                arg.Display.DrawCircle(crc,dc.DodgerBlue,i/30)
                
    def __enter__(self):
        rc.Display.DisplayPipeline.DrawForeground += self.DrawForeground
        
    def __exit__(self):
        rc.Display.DisplayPipeline.DrawForeground -= self.DrawForeground