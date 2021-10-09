import os
from posix import listdir

actual_dir = os.getcwd()
actual_dir = str(actual_dir)

dirs = os.listdir()

paths = [os.path.join(actual_dir, dir) for dir in dirs]

for path in paths:
    os.chdir(path)
    os.remove('DTOTENERGY.OUT')
    os.remove('EFERMI.OUT')
    os.remove('EIGVAL.OUT')
    os.remove('EQATOMS.OUT')
    os.remove('EVALCORE.OUT')
    os.remove('EVALFV.OUT')
    os.remove('EVALSV.OUT')
    os.remove('EVECFV.OUT')
    os.remove('EVECSV.OUT')
    os.remove('FERMIDOS.OUT')
    os.remove('GAP.OUT')
    os.remove('GEOMETRY.OUT')
    os.remove('IADIST.OUT')
    os.remove('INFO.OUT')
    os.remove('KPOINTS.OUT')
    os.remove('LINENGY.OUT')
    os.remove('OCCSV.OUT')
    os.remove('RMSDVS.OUT')
    os.remove('SYMCRYS.OUT')
    os.remove('SYMLAT.OUT')
    os.remove('SYMSITE.OUT')
