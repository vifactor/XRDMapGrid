from matplotlib.axes import Axes as MplAxes
from matplotlib.projections import register_projection

class CustomMplAxes(MplAxes):
    name = "CustomMplAxes"
    
#register new axes type
register_projection(CustomMplAxes)
