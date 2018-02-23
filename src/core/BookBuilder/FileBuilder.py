#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os.path
import zipfile


# create epub file
class FileBuilder(object):

    def __init__(self,outputPath,targetPath,fileName):
        if not isinstance(outputPath,str):
            raise TypeError('bad operand type of outputPath')
        if len(outputPath)==0:
            raise TypeError('bad path of outputPath')
        self.__targetPath = os.path.abspath('..') + r'\temp'
        if len(targetPath) > 0 and os.path.exists(targetPath):
            self.__targetPath = targetPath
        if not isinstance(fileName,str):
            raise TypeError('bad operand type of fileName')
        if len(fileName)==0:
            raise TypeError('bad name of fileName')

        self.__ouputPath = outputPath
        self.__fileName = fileName

        if not os.path.exists(self.__ouputPath):
            os.makedirs(self.__ouputPath)

        self.zip_dir()

    def zip_dir(self):
        fileList = []
        if os.path.isfile(self.__targetPath):
            fileList.append(self.__targetPath)
        else:
            for root,dirs,files in os.walk(self.__targetPath):
                for name in files:
                    fileList.append(os.path.join(root,name))

        zf = zipfile.ZipFile(self.__ouputPath+'/'+self.__fileName+'.epub','w',zipfile.zlib.DEFLATED)

        for tar in fileList:
            arcname = tar[len(self.__targetPath):]
            zf.write(tar,arcname)
        zf.close()