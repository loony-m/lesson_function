import pickle

# записали в файл, тестовые данные
data = {'Максим': '+79203492211', 'Андрей': '+79301234466'};
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
        self.file = open('contacts.data', 'rb')
        self.contactlist = pickle.load(self.file)
        self.file.close()

        self.file = open('contacts.data', 'wb')
        self.contactlist[name] = phone
        pickle.dump(self.contactlist, self.file)
        self.file.close()

    def delete(self, name):
        """Удалить контакт"""
        del (self.contactlist[name])

    def getCount(self):
        """Получить текущее кол-во контактов"""
        count = 0
        for item in self.contactlist:
            count += 1
        return 'На данный момент кол-во записей в контакт листе: {0} шт. \n'.format(count)


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
