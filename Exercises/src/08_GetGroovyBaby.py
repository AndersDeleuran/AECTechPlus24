import Rhino as rc
import Grasshopper as gh
import System.Drawing.Color as dc
import GhPython.Assemblies.ExecutingComponent as component

class SampleMouseCallback(rc.UI.MouseCallback):
    
    def OnMouseMove(self,arg):
        ghenv.Component.ExpireSolution(True)

class MyComponent(component):
    
    def RunScript(self,Radius):
        self.rad = Radius
        
    def get_ClippingBox(self):
        return rc.RhinoDoc.ActiveDoc.Views.ActiveView.ActiveViewport.GetFrustumBoundingBox()
        
    def DrawForeground(self,sender,arg):
        
        # Check component preview/locked, active GH document and Rhino viewport
        if (not ghenv.Component.Hidden and not ghenv.Component.Locked
            and ghenv.Component.OnPingDocument() == gh.Instances.ActiveCanvas.Document
            and arg.Viewport.Id == arg.RhinoDoc.ActiveDoc.Views.ActiveView.ActiveViewportID):
            
            # Call clipping box method when draw events are triggered
            self.get_ClippingBox()
            
            # Get frustum line/camera plane at top left corner
            r1,fl = arg.Viewport.GetFrustumLine(0,0)
            r2,cf = arg.Viewport.GetCameraFrame()
            pt = fl.PointAt(0.5)
            cf.Origin = pt
            
            # Get/print scaling factor to divide by
            r3,s = arg.Viewport.GetWorldToScreenScale(pt)
            rc.RhinoApp.WriteLine(str(s))
            
            # Get/draw mouse location in viewport screen space
            mpt = rc.RhinoDoc.ActiveDoc.Views.ActiveView.ScreenToClient(rc.UI.MouseCursor.Location)
            arg.Display.Draw2dText(str(mpt),dc.Black,mpt,False,30,"Consolas")
            
            # Draw concentric circles
            for i in range(15,int(mpt.X/2),15):
                crc = rc.Geometry.Circle(cf,i*self.rad/s*2)
                c = rc.Display.ColorHSV(i/(mpt.X/1.25),1.0,1.0).ToArgbColor()
                arg.Display.DrawCircle(crc,c,(i+109)/50)
                
    def __enter__(self):
        rc.Display.DisplayPipeline.DrawForeground += self.DrawForeground
        self.mouseMove = SampleMouseCallback()
        self.mouseMove.Enabled = True
        
    def __exit__(self):
        rc.Display.DisplayPipeline.DrawForeground -= self.DrawForeground
        self.mouseMove.Enabled = False
        del self.mouseMove