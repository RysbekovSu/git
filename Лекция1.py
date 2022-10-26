class Luxurything:
    def __init__(self,image,price,girls,attraction,history,demand,safety,acessebility,hype,aesthetics):
        self.i=image
        self.p=price
        self.g=girls
        self.at=attraction
        self.hi=history
        self.d=demand
        self.s=safety
        self.ac=acessebility
        self.h=hype
        self.a=aesthetics

    def House(self,yes_no):
        return f'House: {yes_no}'
    def need(self,l):
        return f"the need in a luxury thing is: {l}"
    def __str__(self):
        return f'image: {self.i}\n' \
               f'price: {self.p}\n' \
               f'girls: {self.g}\n' \
               f'attraction: {self.at}\n' \
               f'history: {self.hi}\n' \
               f'demand: {self.d}\n' \
               f'safety: {self.s}\n' \
               f'acessebility: {self.ac}\n' \
               f'hype: {self.h}\n' \
               f'aesthetics {self.a}\n'

obj1 = Luxurything(True,"High","Arguable",'Arguable',"Mostly True",'Arguable',False,False,True,"Arguable")
print("Luxry thing:")
print(obj1.need(False))
print(f'\n{obj1}')

class Watches(Luxurything):
    def __init__(self,image,price,girls,attraction,history,demand,safety,acessebility,hype,aesthetics,reliability,accuracy):
        super().__init__(image,price,girls,attraction,history,demand,safety,acessebility,hype,aesthetics)
        self.re=reliability
        self.acr=accuracy

    def comfort(self, yes_no):
        return f'comfort: {yes_no}'
    def design(self, t):
        return f'design: {t}'
    def __str__(self):
        return super(Watches,self).__str__()+f'reliability: {self.re}\n' \
                                                 f'accuracy: {self.acr}'
obj2= Watches(True,"High","Arguable",'Arguable',"Mostly True",'Arguable',False,False,True,"Arguable",'High','High')
print('-'*50)
print(obj2.comfort('High'))
print(obj2.design('Timeless'))
print(f'Rolex: \n{obj2}')

class Supercars(Luxurything):
    def __init__(self,image,price,girls,attraction,history,demand,safety,acessebility,hype,aesthetics,weight,power):
        super().__init__(image,price,girls,attraction,history,demand,safety,acessebility,hype,aesthetics)
        self.w=weight
        self.p=power

    def vision(self, yes_no):
        return f'vision: {yes_no}'
    def emotions(self, t):
        return f'emotions: {t}'
    def __str__(self):
        return super(Supercars,self).__str__()+f'weight: {self.w}\n' \
                                                 f'power: {self.p}'
obj3= Supercars(True,"High","Arguable",'Arguable',"Mostly True",'Arguable',False,False,True,"Arguable",'Low','High')
print('-'*50)
print(obj3.vision('High'))
print(obj3.emotions('Unforgettable'))
print(f'Ferrari: \n{obj3}')




