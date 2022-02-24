
import xlwt

class excel():
    def __init__(self,path,qusetion):
        self.save_path=path
        self.total_num=len(qusetion)
        self.book = xlwt.Workbook(encoding='utf-8')
        self.sheet = self.book.add_sheet('answer', cell_overwrite_ok=True)
        self.sheet.write(0,0,"round")
        for i in range(1,self.total_num+1):
            self.sheet.write(0,i,qusetion[i-1])
        self.sheet.write(0,self.total_num+1,"time")
    def write_line(self,rol,answer_index,answer,date_string):
        self.sheet.write(rol,0,"%d"%rol)
        self.sheet.write(rol,answer_index,answer)
        self.sheet.write(rol,self.total_num+1,date_string)
    def last_save(self):
        self.book.save(self.save_path)
