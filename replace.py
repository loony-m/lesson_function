def replaceStr(search, string, *files):
    for file in files:
        filetext = open(file)
        filetextnew = ''
        for line in filetext:
            if (line.find(search) != -1):
                print('В строке - {0} найдено - {1}'.format(line, search))
                line = line.replace(search, string)
                print('Новая строка - {0}'.format(line))
            filetextnew += line
        filetext.close()

        filewrite = open(file, 'w')
        filewrite.write(filetextnew)
        filewrite.close()


replaceStr('Hi', 'Hello', 'replace.txt')
