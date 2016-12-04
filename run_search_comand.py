

'''
x = dildo.do_search()
print x
'''


#bashCommand = "python OpenCV_template_matching.py --template temp_lab.jpg --images images_2 -v false"
'''
import subprocess
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
output = process.communicate()[0]
'''

'''
from subprocess import call
call(["python OpenCV_template_matching.py", "--template temp_lab.jpg", "--images images_2", "-v false"])
'''

import os
def do():
    os.system('python OpenCV_template_matching.py --template nao_test.jpg --images Pictures -v false')
