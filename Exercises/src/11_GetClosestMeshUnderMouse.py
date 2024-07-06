"""
Get closest mesh under mouse location.
Author: Anders Holden Deleuran
Version: 240706
"""

import Rhino as rc
import GhPython.Assemblies.ExecutingComponent as component

class MyMouseCallback(rc.UI.MouseCallback):
    
    def __init__(self):
        self.move = None
        
    def OnMouseMove(self,arg):
        self.move = arg
        ghenv.Component.ExpireSolution(True)

class MyComponent(component):
    
    def RunScript(self,Meshes):
        
        # Get mouse viewport position
        mpt = rc.RhinoDoc.ActiveDoc.Views.ActiveView.ScreenToClient(rc.UI.MouseCursor.Location)
        
        # Make ray along frustum line at mouse
        r,fl = rc.RhinoDoc.ActiveDoc.Views.ActiveView.ActiveViewport.GetFrustumLine(mpt.X,mpt.Y)
        ray = rc.Geometry.Ray3d(fl.From,fl.Direction)
        
        # Shot ray onto meshes
        hits = []
        for i,m in enumerate(Meshes):
            t = rc.Geometry.Intersect.Intersection.MeshRay(m,ray)
            if t >= 0.0:
                hits.append((t,i,m))
                
        # Get closest hit index/mesh and return those
        if hits:
            hits.sort(reverse=True)
            t,i,m = hits[0]
            return i,m
        else:
            return [],[]
            
    def __enter__(self):
        self.mouse = MyMouseCallback()
        self.mouse.Enabled = True
        
    def __exit__(self):
        self.mouse.Enabled = False
        del self.mouse