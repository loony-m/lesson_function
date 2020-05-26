import pickle

# записали в файл, тестовые данные
data = {'Максим': '+79203492211', 'Андрей': '+79301234466'}
file = open('contacts.data', 'wb')
pickle.dump(data, file)
file.close()


class ContactList:
    def __init__(self):
        self.file = open('contacts.data', 'rb')
        self.contactlist = pickle.load(self.file)
        self.file.close()

    def getList(self):
        """ Получить список контактов """
        return self.contactlist

    def add(self, name, phone):
        """Добавить запись контакт"""
        self.contactlist[name] = phone
        self.__save__()

    def delete(self, name):
        """Удалить контакт"""
        del (self.contactlist[name])
        self.__save__()

    def getCount(self):
        """Получить текущее кол-во контактов"""
        count = 0
        for item in self.contactlist:
            count += 1
        return 'На данный момент кол-во записей в контакт листе: {0} шт. \n'.format(count)

    def __save__(self):
        self.file = open('contacts.data', 'wb')
        pickle.dump(self.contactlist, self.file)
        self.file.close()

contact = ContactList()
count = contact.getCount()

print(count)

contact.add('Сергей', '+79432221133')
contact.add('Антон', '+331122')
contact.delete('Максим')

list = contact.getList()
count = contact.getCount()

print('Записей после всех действий')
print(count)
print(list)
