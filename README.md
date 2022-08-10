### You need to write:
make_mems.ipynb - creates bilayer from one molecule. 
You need to write guiding atoms for this, step from one molecule to another, size of layer n*n, and penetration distance..

### How it works
From one molecule, the script creates a pandas dataframe. Positions a molecule along an axis 0X.
Sequentially places one molecule from another with a given step and random rotation along the 0X axis and checking for the minimum distance. After the creation of the first layer, the second layer is created on its basis.