class Animals:
    def __init__(self,heart,eyes,Freedom):
        self.h=heart
        self.e=eyes
        self.f=Freedom


    def __str__(self):
        return f'Heart: {self.h}\n'\
               f'eyes: {self.e}\n'\
               f'Freedom: {self.f}\n'

Горилла = Animals('Имеются','Имеются','найн')
Крокодил = Animals('имеются','Имеются','найн')

print(f'У Гориллы:\n{Горилла}')
print(f'У Крокодила:\n{Крокодил}')

class Млекопитающие(Animals):
    def __init__(self,heart,eyes,Freedom,Temperatura,MilkGlands):
        super().__init__(heart,eyes,Freedom)
        self.t=Temperatura
        self.m=MilkGlands
    def __str__(self):
        return super(Млекопитающие, self).__str__()+f'Temprature: {self.t}\n' \
                                                    f'MilkGlands: {self.m}\n'
Горилла = Млекопитающие('имеются','Имеются','найн','постоянная','Имеютя')
Лев= Млекопитающие('имеются','Имеются','найн','постоянная','Имеютя')

print(f'У Гориллы:\n{Горилла}')
print(f'У Льва:\n{Лев}')

class Reptil(Млекопитающие):
    def __init__(self,heart,eyes,Freedom,Temperatura,MilkGlands,cheshuya):
        super().__init__(heart,eyes,Freedom,Temperatura,MilkGlands)
        self.ch=cheshuya
    def __str__(self):
        return super(Reptil, self).__str__()+f'Checuhuya: {self.ch}\n' \

Varan= Reptil('имеются','Имеются','найн','непостоянная','не Имеютя','Имеются')
Croco= Reptil('имеются','Имеются','найн','ненпостоянная','не Имеютя',"имеются")

print(f'У Варана:\n{Varan}')
print(f'У Крокодила:\n{Croco}')

class Zoo_show:
    def __init__(self,firstshow,secondshow,thirdshow):
        self.f=firstshow
        self.s=secondshow
        self.t=thirdshow
    def __str__(self):
        return f"Имеются три вида шоу:\n" \
               f"1) {self.f}\n" \
               f"2) {self.s}\n" \
               f"3) {self.t}\n"
V=Zoo_show(firstshow='Gorilla figth!!! ',secondshow="Dolphine race",thirdshow="Monkey symphony " )
print(V)
choice=int(input("Выберите номер билета:"))
if choice == 1:
    print(f"Цена билета: 150000сом\n"
          f"Длительность: 15-20мин\n"
          f"Шоу представляет собой дарку до смерти двух сверепых горил накаченных адреналином ")
elif choice == 2:
    print(f"Цена билета: 15000сом\n"
          f"Длительность: 20-25мин\n"
          f"Шоу представляет cобой гонку на воде более 15 дельфинов. Ставки принимаются)")
elif choice == 3:
    print(f"Цена билета: 15000сом\n"
          f"Длительность: 25-30мин\n"
          f"Шоу представляет cобой оркестр из более чем 10 видов обезъян исполняющих симфонию Моцарта,Бетховена и Со"
          f"льери")

