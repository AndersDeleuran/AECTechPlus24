import Grasshopper as gh

def updateComponent(interval):
    
    """ Update this component similar to using a grasshopper timer """
    
    def callBack(e):
        ghenv.Component.ExpireSolution(False)
        
    ghenv.Component.OnPingDocument().ScheduleSolution(interval,
    gh.Kernel.GH_Document.GH_ScheduleDelegate(callBack))

# Instantiate or reset persistent counter variable
if "count" not in globals() or Reset:
    count = 0

# Update the variable and component
if Run and not Reset and count < Target:
    count +=1
    updateComponent(Interval)

# Output counter
Counter = count