# У него есть ровно один метод log,
# который позволяет выводить в лог
# (в данном случае в stdout) какое-то сообщение,
# добавляя при этом текущее время.
# Реализуйте класс LoggableList,
# отнаследовав его от классов list и Loggable таким
# образом, чтобы при добавлении элемента в список
# посредством метода append в лог отправлялось сообщение,
# состоящее из только что добавленного элемента.

import time

class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))

class LoggableList(list, Loggable):
    def append(self, elem):
        super(LoggableList, self).append(elem)
        self.log(elem)

a = LoggableList()
a.append('msg 1')
a.append('msg 2')
print(a)