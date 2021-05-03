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