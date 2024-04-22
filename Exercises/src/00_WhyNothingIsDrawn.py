import Rhino as rc
import GhPython.Assemblies.ExecutingComponent as component
from System.Drawing.Color import Red

class MyComponent(component):
    
    def RunScript(self):
        
        # Make point grid
        self.pts = []
        for i in range(10):
            for j in range(10):
                self.pts.append(rc.Geometry.Point3d(i,j,0))
                
    def DrawViewportWires(self,args):
        
        # Draw point grids as red hearts
        args.Display.DrawPoints(self.pts,rc.Display.PointStyle.Heart,10,Red)
        
    def IsPreviewCapable(self):
        
        # Make component draw without input/output parameters
        return True
        
    def get_ClippingBox(self):
        
        # Define bounding box containing geometry to draw
        return rc.Geometry.BoundingBox(self.pts)