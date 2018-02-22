#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Book:
    # book bean

    def __init__(self,title,creator,subject,description,contributor,date,type,format,identifier,source,language,relation,coverage,rights):
        self.title = title
        self.creator = creator
        self.subject = subject
        self.description = description
        self.contributor = contributor
        self.date = date
        self.type = type
        self.format = format
        self.identifier = identifier
        self.source = source
        self.language = language
        self.relation = relation
        self.coverage = coverage
        self.rights = rights
        self.ChapterList = ''

    def setChapterList(self,chapters):
        self.ChapterList = chapters