import Rhino as rc
import GhPython.Assemblies.ExecutingComponent as component

class MyComponent(component):
    
    def RunScript(self,Curves,Weight,Color):
        
        # Assign input parameters
        self.curves = Curves
        self.weight = Weight
        self.color = Color
        
    def DrawViewportWires(self,arg):
        
        """ Call DrawViewportWires method """
        
        # Draw curves in loop
        for crv in self.curves:
            arg.Display.DrawCurve(crv,self.color,self.weight)