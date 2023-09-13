class Professor:
  def __init__(self,profid,profname,subjectdict):
    self.profid = profid
    self.profname = profname
    self.subjectdict = subjectdict
    
class University:
  
  def gettotalexperience(proflist,iprofid):
    total = 0
    for i in proflist:
      if i.profid == iprofid:
        total = sum(i.subjectdict.values())
        print("Professor Name is : " + str(i.profname) + "\nTotal Year of Experience: "+ str(total))
    
        
        
  def select_senior_prof_by_subject(proflist,isubjectname):
    highexpprof = None
    maxx = 0
    for i in proflist:
      for j in i.subjectdict.keys():
        if j.lower() == isubjectname.lower():
          if i.subjectdict[j] > maxx:
            maxx = i.subjectdict[j]
            highexpprof = i
            
    return highexpprof
    
          
    
n = int(input())
proflist = []
for i in range(n):
  pid = int(input())
  pname = input()
  subdict = {}
  c = int(input())
  for i in range(c):
    key = input()
    value = int(input())
    subdict[key] = value
    
  proflist.append(Professor(pid,pname,subdict))
  
iprofid = int(input())
isubjectname = input()

University.gettotalexperience(proflist,iprofid)

ans2 = University.select_senior_prof_by_subject(proflist,isubjectname)
if ans2 != None:
  print("Professor ID : "+str(ans2.profid)+"\nProfessor Name : "+ str(ans2.profname)+"\nYear of Experience of Each Subject:\n"+str(ans2.subjectdict))
  
else:
  print("NONE!!")
  
  



