import os
import time
import zipfile

class Archive:
    def addFile(self, *file):
        """ Добавить файлы """
        self.files = file

    def dir(self, path):
        """ Путь, где создать архив """
        self.dir = path

    def create(self):
        """ Создать архив """
        today = self.dir + os.sep + time.strftime('%Y%m%d')
        now = time.strftime('%H%M%S')
        target = today + os.sep + now + '.zip'

        if not os.path.exists(today):
            os.mkdir(today)  # создание каталога
            print('Каталог успешно создан', today)

        zf = zipfile.ZipFile(target, 'w')
        for i in self.files:
            zf.write(i)
        else:
            zf.close()

first = Archive()
first.addFile('F:\Python\project-1\continue.py', 'F:\Python\project-1\keyword_only.py')
first.dir('F:\Python\project-github\python')
first.create()
