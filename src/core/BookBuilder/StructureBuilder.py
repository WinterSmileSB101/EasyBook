#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
from lxml import etree

from src.core.Model.Book import Book


class StructureBuilder(object):
    # build the book structure of book opreation floder

    def __init__(self,targetPath,book):
        self.__targetPath = r'C:\EasyBook\Book'
        if len(targetPath)>0:
            self.__targetPath = targetPath
        self.__workPath = os.path.abspath('..')+r'\temp'

        self.__Book = Book(' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ')
        if isinstance(book, Book):
            self.__Book = book

        self.__CreatePath()
        self.__CreateFile()

    def __CreatePath(self):
        # create target path
        if not os.path.exists(self.__targetPath):
            os.makedirs(self.__targetPath)
        # create workpath path
        if not os.path.exists(self.__workPath):
            os.makedirs(self.__workPath)
        # create META path
        if not os.path.exists(self.__workPath+r'\META-INF'):
            os.makedirs(self.__workPath+r'\META-INF')
        # create OEBPS path
        if not os.path.exists(self.__workPath + r'\OEBPS'):
            os.makedirs(self.__workPath + r'\OEBPS')

    def __CreateFile(self):
        self.__CreateMimetype()
        self.__CreateContainer()
        self.__CreateOPF()
        self.__CreateToc()

    def __CreateMimetype(self):
        # create mimetype file
        with open(self.__workPath + '\mimetype', 'w', encoding='utf-8') as f:
            f.write('application/epub+zip')

    def __CreateContainer(self):
        # create container.xml
        container = etree.Element('container',nsmap={'xmlns':'urn:oasis:names:tc:opendocument:xmlns:container'})
        rootfiles = etree.SubElement(container,'rootfiles')
        rootfile = etree.SubElement(rootfiles,'rootfile',attrib={'full-path':'OEBPS/content.opf','media-type':'application/oebps-package+xml'})
        containerTree = etree.ElementTree(container)
        containerTree.write(self.__workPath+r'\META-INF\container.xml', pretty_print=True, xml_declaration=True, encoding='utf-8')

    def __CreateOPF(self):
        # create content opf file
        package = etree.Element('package',attrib={'version':'2.0','unique-identifier':'PrimaryID'},nsmap={'xmlns':'http://www.idpf.org/2007/opf'})
        self.__CreateMetaData(package)
        self.__CreateManifest(package)
        self.__CreateSpine(package)

        packageTree = etree.ElementTree(package)
        packageTree.write(self.__workPath+r'\OEBPS\content.opf', pretty_print=True, xml_declaration=True, encoding='utf-8')

    def __CreateMetaData(self,parentNode):
        # create metadata node
        metadata = etree.SubElement(parentNode,'metadata',nsmap={'dc':'http://purl.org/dc/elements/1.1/','opf':'http://www.idpf.org/2007/opf'})
        title = etree.SubElement(metadata,"{http://purl.org/dc/elements/1.1/}title")
        title.text = self.__Book.title
        creator = etree.SubElement(metadata,'{http://purl.org/dc/elements/1.1/}creator')
        creator.text = self.__Book.creator
        description = etree.SubElement(metadata, '{http://purl.org/dc/elements/1.1/}description')
        description.text = self.__Book.description
        subject = etree.SubElement(metadata, '{http://purl.org/dc/elements/1.1/}subject')
        subject.text = self.__Book.subject
        contributor = etree.SubElement(metadata, '{http://purl.org/dc/elements/1.1/}contributor')
        contributor.text = self.__Book.contributor
        date = etree.SubElement(metadata, '{http://purl.org/dc/elements/1.1/}date')
        date.text = self.__Book.date
        type = etree.SubElement(metadata, '{http://purl.org/dc/elements/1.1/}type')
        type.text = self.__Book.type
        format = etree.SubElement(metadata, '{http://purl.org/dc/elements/1.1/}format')
        format.text = self.__Book.format
        identifier = etree.SubElement(metadata, '{http://purl.org/dc/elements/1.1/}identifier')
        identifier.text = self.__Book.identifier
        source = etree.SubElement(metadata, '{http://purl.org/dc/elements/1.1/}source')
        source.text = self.__Book.source
        language = etree.SubElement(metadata, '{http://purl.org/dc/elements/1.1/}language')
        language.text = self.__Book.language
        relation = etree.SubElement(metadata, '{http://purl.org/dc/elements/1.1/}relation')
        relation.text = self.__Book.relation
        coverage = etree.SubElement(metadata, '{http://purl.org/dc/elements/1.1/}coverage')
        coverage.text = self.__Book.coverage
        rights = etree.SubElement(metadata, '{http://purl.org/dc/elements/1.1/}rights')
        rights.text = self.__Book.rights
        meta = etree.SubElement(metadata, 'meta',attrib={'name':'cover','content':'cover'})

    def __CreateManifest(self,parentNode):
        # create manifest node
        manifest = etree.SubElement(parentNode,'manifest')
        index = 1;
        ncx = etree.SubElement(manifest,'item',
                               attrib={'id':'ncx','href':'content.ncx','media-type':'application/x-dtbncx+xml'})
        ncx = etree.SubElement(manifest, 'item',
                               attrib={'id': 'cover', 'href': 'cover.jpg', 'media-type': 'image/jpeg'})
        for chapter in self.__Book.ChapterList:
            item = etree.SubElement(manifest,'item',
                                    attrib={'id':'chapter{index}.html'.format(index = index),
                                            'href':'chapter{index}.html'.format(index = index),
                                            'media-type':'application/xhtml+xml'})
            index = index+1

    def __CreateSpine(self,parentNode):
        # create spine node
        spine = etree.SubElement(parentNode,'spine',attrib={'toc':'ncx'})
        index = 1;
        for chapter in self.__Book.ChapterList:
            itemref = etree.SubElement(spine,'itemref',
                                    attrib={'idref':'chapter{index}.html'.format(index = index)})
            index = index + 1

    def __CreateToc(self):
        # create toc file
        ncx = etree.Element('ncx',attrib={'version':'2005-1'},nsmap={'xmlns':'http://www.daisy.org/z3986/2005/ncx/'})

        head = etree.SubElement(ncx,'head')
        meta_uid = etree.SubElement(head,'meta',attrib={'name':'dtb:uid','content':''})
        meta_depth = etree.SubElement(head, 'meta', attrib={'name': 'dtb:depth', 'content': '-1'})
        meta_uid = etree.SubElement(head, 'meta', attrib={'name': 'dtb:totalPageCount', 'content': '0'})
        meta_uid = etree.SubElement(head, 'meta', attrib={'name': 'dtb:maxPageNumber', 'content': '0'})

        docTitle = etree.SubElement(ncx,'docTitle')
        titleText = etree.SubElement(docTitle,'text')
        titleText.text = self.__Book.title

        docAuthor = etree.SubElement(ncx, 'docAuthor')
        autorText = etree.SubElement(docTitle, 'text')
        autorText.text = self.__Book.creator

        navMap = etree.SubElement(ncx,'navMap')
        index = 1;
        for chapter in self.__Book.ChapterList:
            navPoint = etree.SubElement(navMap,'navPoint',
                                        attrib={'id':'chapter{index}.html'.format(index = index),
                                                'class':'level{index}'.format(index = index),
                                                'playOrder':'{index}'.format(index = index)})
            navLabel = etree.SubElement(navPoint,'navLabel')
            labelText = etree.SubElement(navLabel,'text')
            labelText.text = 'chapter{index}.html'.format(index = index)
            content = etree.SubElement(navPoint,'content',attrib={'src':'chapter{index}.html'.format(index = index)})
            index = index+1

        ncxTree = etree.ElementTree(ncx)
        ncxTree.write(self.__workPath + r'\OEBPS\toc.opf', pretty_print=True, xml_declaration=True,
                          encoding='utf-8')

    def CleanWorkPath(self):
        for root,dirs,files in os.walk(self.__workPath,topdown=False):
            for name in files:
                os.remove(os.path.join(root,name))
            for name in dirs:
                os.rmdir(os.path.join(root,name))
        os.rmdir(self.__workPath)


