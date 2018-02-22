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


if __name__ == '__main__':
    EasyBook.BuilderEpub()