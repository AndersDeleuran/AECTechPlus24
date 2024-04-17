"""
Get Geometry on Rhino Layer. Dynamically recomputes on changes in Rhino document.
    Inputs:
        Layer: Name of Rhino layer to get Geometry from {item,str}
    Outputs:
        Geometry: Geometry that is on Rhino Layer {list,geometry}
    Remarks:
        Author: Anders Holden Deleuran (BIG IDEAS)
        Rhino: 7.12.21299.13001
        Version: 211028
"""

ghenv.Component.Name = "GetRhinoGeometry"
ghenv.Component.NickName = "GRG"

import Rhino as rc
import GhPython.Assemblies.ExecutingComponent as component

class GetRhinoGeometry(component):
    
    runs = 0
    def RunScript(self,Layer):
        if Layer:
            self.runs += 1
            self.Message = "Recomputes: " + str(self.runs)
            Geometry = []
            for obj in rc.RhinoDoc.ActiveDoc.Objects.FindByLayer(Layer):
                Geometry.append(obj.Geometry)
            return Geometry
        else:
            return []
            
    def callBack(self,e):
        self.ExpireSolution(False)
        
    def updateComponent(self,sender,e):
        self.OnPingDocument().ScheduleSolution(1,self.callBack)
        
    def __enter__(self):
        rc.RhinoDoc.AddRhinoObject += self.updateComponent
        rc.RhinoDoc.DeleteRhinoObject += self.updateComponent
        rc.RhinoDoc.UndeleteRhinoObject += self.updateComponent
        rc.RhinoDoc.ModifyObjectAttributes += self.updateComponent
        
    def __exit__(self):
        rc.RhinoDoc.AddRhinoObject -= self.updateComponent
        rc.RhinoDoc.DeleteRhinoObject -= self.updateComponent
        rc.RhinoDoc.UndeleteRhinoObject -= self.updateComponent
        rc.RhinoDoc.ModifyObjectAttributes -= self.updateComponent