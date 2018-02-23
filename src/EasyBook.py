from src.core.BookBuilder.FileBuilder import FileBuilder
from src.core.BookBuilder.StructureBuilder import StructureBuilder
from src.core.Model.Book import Book


class EasyBook(object):
    @staticmethod
    def BuilderEpub():
        book = Book(' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ')
        book.title = 'test'
        book.creator = 'smileSB101'
        book.ChapterList = ['asdasd','asdasd','asdasd','asdqwd','gsdfg','tryur']
        structureBuilder = StructureBuilder('',book)
        fileBuilder = FileBuilder(r'C:\EasyBook\Book','','tesst')
        structureBuilder.CleanWorkPath()


if __name__ == '__main__':
    EasyBook.BuilderEpub()