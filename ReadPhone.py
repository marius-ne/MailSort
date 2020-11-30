import pytesseract
import os,sys
import cv2
import time
import numpy as np
from PIL import Image
import ssl


class ReadPhone(object):

    def __init__(self):
        self._filestuff()
        self._get_img()
        self._output()

    def _filestuff(self):
        '''Get the current working directory and establish output-filename and output-folder'''

        script_path = os.path.abspath(__file__)
        self.script_dir = os.path.split(script_path)[0]
        rel_path = "pics"
        self.abs_file_path = os.path.join(self.script_dir, rel_path)

        self.filename = 'test.PNG'
        self.img_path = self.abs_file_path + "/" + self.filename
        try:
            os.mkdir('output')
        except Exception:
            pass

    def _get_img(self):
        '''Get the image from IP-camera API, streaming from phone'''

        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE

        url = 'https://192.168.2.115:8080/video'
        stream = cv2.VideoCapture(url)
        _,self.frame = stream.read()
        cv2.imshow('stream',self.frame)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        os.chdir(self.abs_file_path)
        cv2.imwrite(self.filename,self.frame)

    def _output(self):
        '''Make input grayscale and read with pytesseract'''

        cv_read = cv2.imread(self.img_path)
        cv_scale = cv2.cvtColor(cv_read,cv2.COLOR_BGR2GRAY)
        cv_gray = cv2.pow(cv_scale,1)
        cv2.imshow('stream',cv_gray)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        custom_config = r'--oem 3 --psm 12'
        self.txt = pytesseract.image_to_string(cv_gray,config=custom_config)
        print(self.txt)
        self._write()

    def _write(self):
        '''Write output to output folder'''

        pic_name = self.filename.split('.')[0]
        os.chdir(os.path.join(self.script_dir, 'output'))

        filename = '%s_out.txt' % pic_name
        with open(filename,'w') as fid:
            for let in self.txt:
                try:
                    fid.write(let)
                except Exception:
                    fid.write('[?]')
