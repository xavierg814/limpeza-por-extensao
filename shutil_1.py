import os, shutil
 
dir = 'C:\Users\usuario002\Oracle\oradiag_usuario002\diag\clients\user_usuario002\host_457085956_76\incident'
for files in os.listdir(dir):
    path = os.path.join(dir, files)
    print (f"arquivo/subpasta {files} deletado")
    try:
        shutil.rmtree(path)
    except OSError:
        os.remove(path)