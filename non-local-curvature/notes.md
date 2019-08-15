## Speed Notes

#### Math program computed on gpu results
We may want to use GPUs to accelerate the math computations. https://www.researchgate.net/publication/261987861_A_Memory_Efficient_Algorithm_for_Adaptive_Multidimensional_Integration_with_Multiple_GPUs

#### Library for python GPU computing
https://www.researchgate.net/profile/Razvan_Pascanu/publication/228832149_Theano_A_CPU_and_GPU_math_compiler_in_Python/links/004635314aa30be30d000000/Theano-A-CPU-and-GPU-math-compiler-in-Python.pdf

#### Another paper discussing integration technique on GPU
https://onlinelibrary.wiley.com/doi/epdf/10.1002/nme.2661


#### Monte Carlo Integration on GPU
https://link.springer.com/article/10.1140/epjc/s10052-011-1559-8
https://link.springer.com/content/pdf/10.1140%2Fepjc%2Fs10052-011-1559-8.pdf

#### Image calculations done on GPU
https://www.osapublishing.org/oe/fulltext.cfm?uri=oe-20-2-732&id=226157

## Libraries Used

### Shapely

#### What is Shapely?

Shapely is a Python package for set-theoretic analysis and manipulation of planar features using (via Python’s ctypes module) functions from the well known and widely deployed GEOS library. GEOS, a port of the Java Topology Suite (JTS), is the geometry engine of the PostGIS spatial extension for the PostgreSQL RDBMS. The designs of JTS and GEOS are largely guided by the Open Geospatial Consortium’s Simple Features Access Specification [1] and Shapely adheres mainly to the same set of standard classes and operations. Shapely is thereby deeply rooted in the conventions of the geographic information systems (GIS) world, but aspires to be equally useful to programmers working on non-conventional problems. (Source)[https://shapely.readthedocs.io/en/stable/manual.html]

#### Where are we using Shapely?

Shapely offers shape intersection functions that work between curves that are much more straight forward to use than the other libraries that I have tried. As of now I am abusing the fact that we are testing for circles. The library creates a circle based on the radius given. 
```Python
#For now there is no code that grabs the origin
origin = Point(0, 0)
# self.radius refers to the radius given by the user in the config file
self.circle = origin.buffer(self.radius).boundary
```

Intersections are found using:
```Python
#l is the line given from two points
l = LineString([(self.radius,f(self.radius)),(-self.radius,f(-self.radius)) ])
#This line will find where l intersects with the circle
#i is the geometry object that is created from the intersection (POINT, MULTIPOINT, LINE, etc)
i = self.circle.intersection(l)
```

I found that using shapely has made the functions more accurate. We do lose some speed as a consequence.
    

http://geomalgorithms.com/a03-_inclusion.html