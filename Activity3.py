class India:
    def capital(self):
        print("Capital of India is New Delhi")
    def language(self):
        print("Hindi is most commonly spoken")
    def type(self):
        print("India is a developing country")

class USA:
    def capital(self):
        print("\nCapital of USA is Washington D.C")
    def language(self):
        print("English is widely spoken")
    def type(self):
        print("USA is a developed country")

obj_Ind = India()
obj_USA = USA()

for country in (obj_Ind, obj_USA):
    country.capital()
    country.language()
    country.type()