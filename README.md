# Non-Local_Curvature
A program to programatically explore non-local curvature.

The nonlocal mean curvature is the average curvature aroud a curve (open or closed) specified at a point. The purpose of this repository is compute the NonLocal mean curvature for functions in two dimensions. By hand, these integrals are sometimes only able to be estimated.

What is nonlocal mean curvature?
    This [link](https://web.ma.utexas.edu/mediawiki/index.php/Nonlocal_minimal_surfaces) will explain in mathematical terms what this code is designed to estimate.

What is the purpose of this project?
    The purpose of the project is to develop a tool for estimating the nonlocal mean curvature for any function.

### Requirements
- Python 3

### Install process
The first thing one must do is install the required packages.
```bash
python3 -m pip install -r ./requirements.txt
```

### Config File
The config file is where the user defines givens for the code to work with. The user must parameterize their desired curve into two variables. Lets take a look at an example of a circle with a radius of two.
```yaml
curv:
  func_x: 2*np.cos(t) #Circle parameterization for x variable
  func_y: 2*np.sin(t) #Circle parameterization for y variable
  start_point: [0,-2] #The point at which the curvature is realitive too
  origin: [0,0] #The origin of the circle
  radius: 2 #The radius of the circle
  alg: winding_number #user choosen point in polygon algorithm (for speed testing)
```

### Running Code
After you have installed all the packages and updated the config file to your specifications, you can now run the code.
```bash
python3 non-local-curvature.py
```

### Current Working Features
- Can estimate the nonlocal mean curvature of a circle
- Winding number point-in-polygon algorithm
- Ray casting point-in-polygon algorithm 

### Current Development Focus
- Ability to estimate the nonlocal mean curvature of any closed curve
- Ability to estimate the nonlocal mean curvature of any open curve
