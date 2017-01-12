from numpy import pi, exp

(x0,p0,sigmax,sigmap) = (-4.0, 3.0, 0.1, 0.1)
Z = 1./(2.*pi*sigmax*sigmap)

def f0(x,p):
    """Normalised information field (distribution function)"""
    global Z, x0, p0, sigmax, sigmap
    return Z*exp(-((x-x0)**2/(2.*sigmax**2)+(p-p0)**2/(2.*sigmap**2)))