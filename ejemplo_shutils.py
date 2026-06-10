import shutil #Utility functions for copying and archiving files and directory trees
import os
import pandas as pd

#copiar fichero
#shutil.copy(src='miquijote.txt', dst='miquijote_copia.txt')

#copiar directorio
#shutil.copytree(src="dir1", dst="dir2")

#ignorar los ficheros .txt al copiar el directorio
#shutil.copytree(src="dir1", dst="dir3", ignore=shutil.ignore_patterns("*.txt")) 

#mover ficheros
#shutil.move(src="dir2/miquijote_copia.txt", dst="dir3/miquijote_copia.txt")

#renombrar ficheros
#os.rename("dir1/hola.py", "dir1/hola2.py ")

#borrar ficheros
#os.remove("dir1/hola_rn.py")

