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
        hitMeshes = []
        hitParams = []
        for m in Meshes:
            t = rc.Geometry.Intersect.Intersection.MeshRay(m,ray)
            if t >= 0.0:
                hitMeshes.append(m)
                hitParams.append(t)
                
        # Get closest hit mesh and return it
        if hitParams:
            return hitMeshes[hitParams.index(max(hitParams))]
        else:
            return []
            
    def __enter__(self):
        self.mouse = MyMouseCallback()
        self.mouse.Enabled = True
        
    def __exit__(self):
        self.mouse.Enabled = False
        del self.mouse