from matplotlib.axes import Axes as MplAxes
from matplotlib.projections import register_projection
import xrayutilities as xu

class CustomMplAxes(MplAxes):
    name = "CustomMplAxes"
    
    def __init__(self, *args, **kwargs):
        super(CustomMplAxes, self).__init__(*args, **kwargs)
        
        #contour set created by xx function will be kept in axes
        self.cs = None
        #xrayutilities datagridder is kept in axes
        self.gridder = xu.Gridder2D(25, 25)
        
        #raw data arrays are preserved
        self.Qx_data = None
        self.Qz_data = None
        self.Int_data = None
    
    def rsm(self, qx, qz, intensity):
        self.Qx_data = qx
        self.Qz_data = qz
        self.Int_data = intensity
        
        self.gridder(self.Qx_data, self.Qz_data, self.Int_data)
        LOGINT = xu.maplog(self.gridder.data.transpose(),6,0)

        #draw rsm
        self.cs = self.contourf(self.gridder.xaxis, self.gridder.yaxis, LOGINT, 25, extend='min')

        #annotate axis
        self.set_xlabel(r'$Q_{x}$')
        self.set_ylabel(r'$Q_{z}$')
        
    def set_gridder_resolution(self, nx, ny):
        
        #update gridder
        self.gridder.SetResolution(nx, ny)
        
        #regrid data
        self.gridder(self.Qx_data, self.Qz_data, self.Int_data)
        LOGINT = xu.maplog(self.gridder.data.transpose(),6,0)

        #draw rsm
        cmin, cmax = self.cs.get_clim()
        self.cs = self.contourf(self.gridder.xaxis, self.gridder.yaxis, LOGINT, 25, extend='min')
        self.cs.set_clim(cmin, cmax)
    
    def set_data_limits(self, cmin, cmax):
        self.cs.set_clim(cmin, cmax)
        #TODO if there is a colorbar, deal with it as well
        
        
#register new axes type
register_projection(CustomMplAxes)
