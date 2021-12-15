import os
from random import shuffle
from codes import Error_codes

class File:

    def __init__(self, input_path, output_path ):
        self.inp_path = input_path
        self.outp_path = output_path
        self.error_code = Error_codes.bad_request
        self.data = []
        self.fin = None

        self.check_file()

        if self.error_code == Error_codes.ok:
            self.fin = open(self.inp_path, 'r')
            self.data = self.fin.readlines()
            for i in range(len(self.data)):
                if not self.data[i].count("\n"):
                    self.data[i]+="\n"

    def __del__(self):
        if self.error_code == Error_codes.ok:
            self.fin.close()

    def check_file(self):
        self.error_code = Error_codes.ok
        if not os.path.isfile(self.inp_path):
            self.error_code = Error_codes.no_file

    def write_in_file(self):
        if self.error_code == Error_codes.ok:
            fout = open(self.outp_path, 'w')
            fout.writelines(self.data)
            fout.close()



    def sort_up(self):
        self.data.sort()
    
    def sort_down(self):
        self.data.sort(reverse=True)
    
    def sort_len_up(self):
        self.data.sort(key=len)

    def sort_len_down(self):
        self.data.sort(key=len, reverse=True)

    def random(self):
        shuffle(self.data)
    
    def result_of_work(self):
        return self.error_code