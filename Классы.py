class Jundev:
    def __init__(self,Watches,Cars,Drugs):
        self.w=Watches
        self.c=Cars
        self.d=Drugs

    def House(self,yes_no):
        return f'House: {yes_no}'
    def language(self,l):
        return f"Программист владеет {l} языком"
    def __str__(self):
        return f'Watches: {self.w}\n'\
               f'Cars: {self.c}\n'\
               f'Drugs: {self.d}\n'

obj1 = Jundev('Seiko','lambo','Marijuana')
print(obj1.House('Penthouse'))
print(obj1.language("QBasic"))
if obj1.language("QBasic"):
    print("Ты не молодец")
print(obj1)
class MidDev(Jundev):
    def __init__(self,Watches,Cars,Drugs,Computer,Tea,Burbon):
        super().__init__(Watches,Cars,Drugs)
        self.p=Computer
        self.t=Tea
        self.b=Burbon

    def Kids(self, yes_no):
        return f'Kids: {yes_no}'
    def __str__(self):
        return super(MidDev, self).__str__()+f'Computer: {self.p}\n' \
                                             f'Tea: {self.t}\n' \
                                             f'Burbon: {self.b}\n'
obj2 = MidDev('Rolex','Ferrari','Cock','Hp',Tea='champion',Burbon='Jameson')
print('-'*50)
print(obj2.House('Dacha'))
print(obj2.Kids('Nah'))
print(obj2.language("СSS"))
if obj2.language("CSS"):
    print("Ты молодец")
print(obj2)

class Sendev(MidDev):
    def __init__(self, Watches, Cars, Drugs, PComputer, Tea, Burbon, Mall, Faith, club):
        super().__init__(Watches, Cars, Drugs, PComputer, Tea, Burbon)
        self.m = Mall
        self.h = Faith
        self.s = club

    def Tiktok(self, yes_no):
        return f'Tiktok: {yes_no}'
    def __str__(self):
        return super(Sendev, self).__str__() + f'Mall: {self.m}\n'\
                                               f'Faith: {self.h}\n'\
                                               f'club: {self.s}'


obj3 = Sendev(Watches=True, Cars=False, Drugs=True, PComputer=True, Tea=True, Burbon=True, Mall='ASiaMall', Faith='atheist',club='Madrid')
print('-' * 50)
print(obj3.House('Penthouse'))
print(obj3.Kids('2 so far'))
print(obj3.Tiktok("i=not an idiot"))
print(obj3.language("Python"))
if obj2.language("CSS"):
    print("Ты молодец")
print(obj3)
