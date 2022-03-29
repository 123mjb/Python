import subprocess,sys,os
def install(package): 
    for i in package: subprocess.check_call([sys.executable, "-m", "pip", "install", i])
install(["pygame",])
# "PyOpenGL","PyOpenGL_accelerate","setuptools"

# import subprocess,sys,os; install = (lambda package: for i in package: subprocess.check_call([sys.executable, "-m", "pip", "install", i])); install(["pygame",])
