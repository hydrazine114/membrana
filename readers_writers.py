import numpy as np
import pandas as pd

# |------------------------- readers -------------------------|


def read_xyz(file):
    with open(file) as file:
        system = []
        for cnt, line in enumerate(file):
            if cnt > 1:
                system.append(line.split())
    df = pd.DataFrame(system, columns = ('atom', 'x', 'y', 'z'))
    return df.astype({'atom': str, 'x': float, 'y': float, 'z': float})


def read_mol2(file):
    read = False
    with open(file) as file:
        system = []
        for line in file:
            if '@<TRIPOS>BOND' in line:
                read = False
            if read:
                system.append(line.split())
            
            if '@<TRIPOS>ATOM' in line:
                read = True
    df = pd.DataFrame(system, columns = ('atnum', 'atom', 'x', 'y', 'z', 'atType',
                                         'resnum', 'res', 'something'))
    return df.astype({'atnum': np.uint32, 'resnum': np.uint32, 'atom': str, 'x': float, 'y': float, 'z': float})
        

def read_pdb(file):
    with open(file) as file:
        system = []
        for line in file:
            if ('ATOM' in line) or ('HETATM' in line):
                system.append(line.split()[1:])           
    df = pd.DataFrame(system, columns = ('atnum', 'atom', 'res', 'resnum', 'x', 'y', 'z', 'smth0', 'smth1', 'atType'))
    df = df.assign(resnum=[1]*df.shape[0])
    return df.astype({'atnum': np.uint32, 'resnum': np.uint32, 'atom': str, 'x': float, 'y': float, 'z': float})


# |------------------------- writers -------------------------|


def write_xyz(df, filename='test.xyz'):
    with open(filename, 'w') as file:
        file.write(f'{df.shape[0]}\n\n')
        for i in range(df.shape[0]):
            file.write('{:3s}{:17.9f}{:17.9f}{:17.9f}\n'.format(df.iloc[i].atom, df.iloc[i].x, df.iloc[i].y, df.iloc[i].z))


def write_pdb(system, file='test.pdb'):
    system['atType'] = system.atType.apply(lambda x: x[0])
    gg = system.apply(lambda x:
    'HETATM{:5d} {:>4s} {:<4s} {:<4d}    {:8.3f}{:8.3f}{:8.3f}  0.00  0.00               {:s}\n'.format(
        x['atnum'], x['atom'], x['res'], x['resnum'], x['x'], x['y'], x['z'], x['atType']
    ), axis=1).values
    
    with open(file, 'w') as file:
        for i in range(gg.shape[0]):
            if i > 1 and system.iloc[i].resnum != system.iloc[i-1].resnum:
                file.write('TER\n')
            file.write(gg[i])
        file.write('END\n')


def write_gro(system, file='test.gro', box=None):
    system[['x', 'y', 'z']] /= 10
    system[['x', 'y', 'z']] -= system[['x', 'y', 'z']].min()
    system['x'] += 7.4
    with open(file, 'w') as file:
        file.write(f'!comment\n{system.shape[0]}\n')
        for i in range(system.shape[0]):
            file.write('{:5d}{:<5s}{:5s}{:5d}{:8.3f}{:8.3f}{:8.3f}\n'
                       .format(*system.iloc[i][['resnum', 'res', 'atom', 'atnum', 'x', 'y', 'z']]))
        if box is None:
            box = system[['x', 'y', 'z']].max()
            box.iloc[0] = 18
        file.write('{} {} {}\n'.format(*box))
