from abc import ABC,abstractmethod
class Reader(ABC):
    @abstractmethod
    def read(self,contents):
        pass

class NewsReader(Reader):
    def read(self,contents):
        print(contents)

class Poet(Reader):
    def read(self,contents):
        print(contents)
    def writingPoems(self,language):
        self.language=language
        print("Language used is "+self.language)

nw=NewsReader()
nw.read("Reading News on TV")
p=Poet()
p.read("Reading Poem")
p.writingPoems("Hindi")