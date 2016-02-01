class Student(object):
    def __init__(self,name,score):
        self.__name = name
        self.__score = score
    def __len__(self):
        return 10


    def get_name(self):
        print (self.__name)

    def get_score(self):
        print (self.__score)

    def set_name(self,name):
        self.__name = name

    def set_score(self,score):
        if 0<=score<=100:
            self.__score = score
        else:
            raise ValueError('bad score')

    def print_score(self):
        print ('%s:%s' % (self.__name,self.__score))



bart = Student('brat',20)

# yangyang = Student('yangyang',0)
#
# bart.print_score()
# yangyang.print_score()
#
# bart.set_score(100)
# bart.get_score()
#
# print(type(bart))
# print(dir(bart))
print(len(bart))
