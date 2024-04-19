""" Offset Polyline (Retains Topology, No Fancy Clipping)
Author: Anders Holden Deleuran (BIG IDEAS) """

import Rhino as rc
import Grasshopper.Kernel.Types as gkt

def offsetPolyline(polyline,distance,plane):
    
    """ Offset polyline by distance within plane, retains topology """
    
    # Get and offset segments
    offSegs = []
    for lA in polyline.GetSegments():
        vec = lA.To-lA.From
        vec.Unitize()
        vec.Rotate(rc.RhinoMath.ToRadians(90),plane.ZAxis)
        vec = vec*distance
        lB = rc.Geometry.Line(lA.From+vec,lA.To+vec)
        offSegs.append(lB)
        
    # Construct offset vertices: Case A
    if polyline.IsClosed:
        
        # Intersect segments
        vts = []
        for i in range(len(offSegs)):
            if i < len(offSegs)-1:
                r,tA,tB = rc.Geometry.Intersect.Intersection.LineLine(offSegs[i],offSegs[i+1])
            else:
                r,tA,tB = rc.Geometry.Intersect.Intersection.LineLine(offSegs[i],offSegs[0])
            vts.append(offSegs[i].PointAt(tA))
            
        # Add last vertex
        vts.append(vts[0])
        
    # Construct offset vertices: Case B
    else:
        
        # Intersect segments
        vts = [offSegs[0].From]
        for i in range(len(offSegs)-1):
            r,tA,tB = rc.Geometry.Intersect.Intersection.LineLine(offSegs[i],offSegs[i+1])
            vts.append(offSegs[i].PointAt(tA))
            
        # Add last vertex
        vts.append(offSegs[-1].To)
        
    # Make offset polyline
    return rc.Geometry.Polyline(vts)

Offsets= []
for plc in Polylines:
    test,pl = plc.TryGetPolyline()
    if Plane:
        offPl = offsetPolyline(pl,Distance,Plane)
    else:
        pln = rc.Geometry.Plane(pl[0],pl[1],pl[2])
        offPl = offsetPolyline(pl,Distance,pln)
     
    Offsets.append(gkt.GH_Curve(offPl.ToNurbsCurve()))