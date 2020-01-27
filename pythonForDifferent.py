import os
from os.path import abspath
import pathlib
import shutil
path='Z:\\drawable-nodpi\\'
path1='Z:\\Downloads\\Setup\\'
file1 = pathlib.Path("Z:output1.txt")
filenames = os.listdir(path)
for filename1 in filenames:
    f = open("Z:output1.txt", "a+")
    filename1 =filename1[:-4]
    f.writelines(filename1+'\n')
    print("rohithbairi       444sdf"+filename1)
    f.close()
for filename in filenames :
    #print("rohithbairi       333sdf"+filename)
    r = path1
    path1 = os.path.join(path1)
    for r,d,f in os.walk(path1):
            for files in f:
                print(os.path.join(r,files)  + " rohith   "  +filename )
                if filename in files:
                    print(os.path.join(r,files)  + " bairi   "  +filename )  
                    if 'HMC' in os.path.join(r,files) :
                        #print(os.path.join(r,files)  + " black   "  +filename )
                        if not os.path.exists('Z:\\HMC_NEW'):
                            os.makedirs('Z:\\HMC_NEW')
                            shutil.copy(os.path.join(r,files),'Z:\\HMC_NEW')
                        else:
                            shutil.copy(os.path.join(r,files),'Z:\\HMC_NEW')
                    else:
                        #print(os.path.join(r,files)  + " white   "  +filename )
                        if 'KMC' in os.path.join(r,files) :
                            #print(os.path.join(r,files)  + " white w   "  +filename )  
                            if not os.path.exists('Z:\\KMC_NEW'):
                                os.makedirs('Z:\\KMC_NEW')
                                shutil.copy(os.path.join(r,files),'Z:\\KMC_NEW')
                            else:
                                shutil.copy(os.path.join(r,files),'Z:\\KMC_NEW')            
             
             
            
