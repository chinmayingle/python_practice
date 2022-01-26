class Team:
   '''
   Contains List of Junior and senior team members and also overrides the __iter__() function.
   '''
   def __init__(self):
       self._juniorMembers = list()
       self._seniorMembers = list()
   def addJuniorMembers(self, members):
       self._juniorMembers += members
   def addSeniorMembers(self, members):
       self._seniorMembers += members
   def __iter__(self):
       ''' Returns the Iterator object '''
       return TeamIterator(self)

class person:
    def __init__(self,name) -> None:
        self.name=name
        pass

    def __str__(self) -> str:
        return self.name

class people:

    def __init__(self,name) -> None:
        self.name=name
        pass

    def __iter__(self):
        pass

    def __next__(self):
        pass

    # def __iter__(self):
    #     return self.name


    # def __iter__(self):

    #     return self.name
one=person("one")
print(one)
a=people("Aa")
one.__next__()
# for i in people:
#     print(i)