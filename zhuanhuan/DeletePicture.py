import os

class Delete:
    def DPictrue(file):
        my_file = file
        if os.path.exists(my_file):
            os.remove(my_file)
            #os.unlink(my_file)
        else:
            print('no such file:%s'%my_file)




