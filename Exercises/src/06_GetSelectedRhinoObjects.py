"""
Get Selected Rhino Geometry. Dynamically recomputes on changes in Rhino document.
    Inputs:
    Outputs:
        Geometry: Selected Rhino geometry {list,geometry}
    Remarks:
        Author: Anders Holden Deleuran 
        Rhino: 7.12.21299.13001
        Version: 230929
"""

ghenv.Component.Name = "GetSelectedGeometry"
ghenv.Component.NickName = "GSG"

import Rhino as rc
import GhPython.Assemblies.ExecutingComponent as component

class GetRhinoGeometry(component):
    
    runs = 0
    def RunScript(self):
        self.runs += 1
        self.Message = "Recomputes: " + str(self.runs)
        Geometry = []
        for obj in rc.RhinoDoc.ActiveDoc.Objects.GetSelectedObjects(True,False):
            Geometry.append(obj.Geometry)
        return Geometry
        
    def callBack(self,e):
        self.ExpireSolution(False)
        
    def updateComponent(self,sender,e):
        self.OnPingDocument().ScheduleSolution(1,self.callBack)
        
    def __enter__(self):
        rc.RhinoDoc.SelectObjects += self.updateComponent
        rc.RhinoDoc.DeselectObjects += self.updateComponent
        rc.RhinoDoc.DeselectAllObjects += self.updateComponent
        
    def __exit__(self):
        rc.RhinoDoc.SelectObjects -= self.updateComponent
        rc.RhinoDoc.DeselectObjects -= self.updateComponent
        rc.RhinoDoc.DeselectAllObjects -= self.updateComponent