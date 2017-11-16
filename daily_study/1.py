#!coding:utf-8
import re

def strip(file_name):
    line = open(file_name,'r',encoding='utf-8').readlines()
    for i in line:
        #R = (r'(\[[0-9\:\.]*\][a-z]*[\ ]*\.[^\x00-\xff]*)')
       # R = (r'([^\x00-\xff]*)')
        R = (r'[\u4e00-\u9fa5]*')
#[02:56.55]come  vi. 来；经过；达到，至；产生（于），来（自）；
        result = re.findall(R,i)
        while '' in result:
            result.remove('')

        if (  result ):
            print (result)
            print (i)
            save_to_file(file_name+".after", i)

            #with open (file_name+".after", 'wb') as FF:
            
def save_to_file(file_name, contents):
    print (file_name)
    fh = open(file_name, 'a')
    fh.write(contents)
    fh.close()



if __name__ == '__main__':
    strip('F:\github\python\日常学习练习/1.lrc')

