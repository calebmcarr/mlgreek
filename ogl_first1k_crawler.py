#Caleb Carr 3Feb2019
#Strip all the Greek text out of downloaded First 1k Greek from OGL
#store result as .txt files
import re
import os
import os.path

def file_gather():
    '''Gather all of the xml files off the unzipped First 1k Years of Greek
    download and get rid of any _cts_.xml files'''
    files = []
    for dirpath, dirnames, filenames in os.walk('.'):
        for filename in [f for f in filenames if f.endswith('1.xml')]:
            files.append(os.path.join(dirpath,filename))
    return files

def write_reg_read(files):
    '''Read xml files, strip non Greek text, and store it'''
    for i in range(len(files)):
        title = files[i]
        title_name = './Texts/OGL_texts/'+str(os.path.basename(files[i]))
        #open file and read it
        f = open(title,'r')
        text = f.read()
        #regex out non Greek.  Sorry its a ridiculous expression.
        r = re.sub(r'[a-zA-Z0-9]*[\[\]!@~|üΜΑäæ\\NÜﬁﬂ#$%^&é*ß()—_+-=;,./<>·"?]*','',text)
        r = re.sub(r'\'','',r)
        r = re.sub(r'\s+',' ',r)
        f.close()
        #save changed text in ./Text_demo
        #title_name = title_name.strip('.xml')+'.txt'
        f = open(title_name,'w')
        f.write(r)
        f.close()
        print('Completed File '+str(i))

def main():
    files = file_gather()
    write_reg_read(files)

main()
