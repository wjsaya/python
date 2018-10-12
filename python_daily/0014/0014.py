
import json
import xlwt

class json2xls():
    def __init__(self, fileName='student.txt'):
        self.sheetName = fileName.split('.')[0]
        self.parseJsonFiles(fileName)

    def parseJsonFiles(self, fileName=''):
        filein = open(fileName, 'r', encoding="utf-8")
        lines = filein.readlines()
        for i in range(len(lines)):
            lines[i] = lines[i].strip("\n").strip("\t")
        self.jsonContent = lines

    def save2file(self, fileName="test.xls"):
        xls = xlwt.Workbook()
        sheet = xls.add_sheet('student')

        for i, value in enumerate(self.jsonContent, -1):
            if value not in ['{', '}']:
                self.save2fileWorker(sheet, i, value.strip(','))
        xls.save(fileName)

    def save2fileWorker(self, sheet, x, ylist):
        row1, rows = ylist.split(":")
        sheet.write(x, 0, row1)

        for i, value in enumerate(rows.split(","), 1):
            value = value.strip('[').strip(']')
            sheet.write(x, i, value)
        c




a = json2xls("student.txt")
a.save2file('temp.xls')

# fun2()
# fun3()




