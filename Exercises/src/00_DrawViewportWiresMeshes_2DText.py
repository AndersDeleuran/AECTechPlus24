import Rhino as rc
import GhPython.Assemblies.ExecutingComponent as component

class MyComponent(component):
    
    def RunScript(self,Text,Color,Height,Point,Font):
        
        # Assign input parameters
        self.text = Text
        self.color = Color
        self.height = Height
        self.point = rc.Geometry.Point2d(Point.X,Point.Y)
        self.font = Font
        
    def DrawViewportWires(self,arg):
        
        """ Call DrawViewportWires method """
        
        # Draw 2D text
        arg.Display.Draw2dText(self.text,self.color,
        self.point,False,self.height,self.font)