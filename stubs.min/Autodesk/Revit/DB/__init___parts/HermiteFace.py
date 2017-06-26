class HermiteFace(Face,IDisposable):
 """ A cubic hermite spline face of a 3d solid or open shell. """
 def Dispose(self):
  """ Dispose(self: APIObject,A_0: bool) """
  pass
 def ReleaseManagedResources(self,*args):
  """ ReleaseManagedResources(self: APIObject) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: GeometryObject) """
  pass
 def __enter__(self,*args):
  """ __enter__(self: IDisposable) -> object """
  pass
 def __exit__(self,*args):
  """ __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 MixedDerivs=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Mixed derivatives of the surface.

Get: MixedDerivs(self: HermiteFace) -> IList[XYZ]

"""

 Points=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Interpolation points of the surface.

Get: Points(self: HermiteFace) -> IList[XYZ]

"""


