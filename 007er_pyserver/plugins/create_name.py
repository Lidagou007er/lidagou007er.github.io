#-*-coding:utf-8-*-
import random as rd

#类,称号生成器
class Name_Creator():
    def __init__(self):
        self.first_title=['风暴降生','火吻而生','野猪克星','核暴之神']
        self.sourceA=['智障','Rick大陆','Morty宇宙','哥谭','夹皮沟']
        self.sourceB=['之子','之王','毁灭者','之神']
        self.data=[['不焚者','五境女王','多重宇宙统治者'],['地球的合法统治者','人类的创造者','火星的合法继承者']]
        self.data.append([self.word_creator(self.sourceA,self.sourceB)])
    #input_name = raw_input("输入你的名字：")
    #input_num = raw_input("输入称号长度: ")

    '''
    #函数：生成固定长度且不重复的二维数组__然并卵
    def create_num(self,name_length):
        data=self.data
        name_num_total=len(data)
        num_list=[]
        while len(num_list)!=name_length:
            if_add=True
            rd_num = rd.randint(0, int(name_num_total)-1)
            for name in num_list:
                if rd_num==name:
                    if_add=False
            if if_add==True:
                num_list.append(rd_num)
        return num_list
    '''
    #生词！
    def word_creator(self,sourceA,sourceB):
        return sourceA[rd.randint(0, int(len(sourceA)) - 1)]+sourceB[rd.randint(0, int(len(sourceB)) - 1)]
    #print create(5,10)-----test
    #函数：根据数组从data中提取名称
    def get_name(self):
        data = self.data
        name=""
        for names in data:
            rd_name=names[rd.randint(0,len(names)-1)]
            name=name+","+rd_name
        return name

    def create_name(self,name_input):
        first_name=self.first_title[rd.randint(0, int(len(self.first_title)) - 1)]
        return first_name+name_input+self.get_name()

#test
#a=Name_Creator()
#print a.create_name('a')