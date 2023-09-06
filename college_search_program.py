class college:
    def __init__(self, cid, cname, ccontact, cadd, cpin):
        self.collegeid = cid
        self.collegename = cname
        self.collegecontact = ccontact
        self.address = cadd
        self.pincode = cpin


class solution:
    def __init__(self, clist):
        self.clist = clist

    def findclgwithmaxpincode(self):
        m = 0
        for i in self.clist:
            if i.pincode > m:
                m = i.pincode

        for j in self.clist:
            if j.pincode == m:
                return j

    def searchclgbyaddress(self, ad):
        for i in self.clist:
            if i.address.lower() == ad.lower():
                #print(i.pincode)
                return i


n = int(input())
clist = []
for i in range(n):
    cid = int(input())
    cname = input()
    ccontact = int(input())
    add = input()
    pin = int(input())

    clist.append(college(cid, cname, ccontact, add, pin))



ad = input()

obj = solution(clist)



ans1 = obj.findclgwithmaxpincode()

if ans1:
  
  print(ans1.collegeid)
  print(ans1.collegename)
  print(ans1.collegecontact)
  print(ans1.address)
  print(ans1.pincode)

else:
  print("no college found with the mention attribute!!")


ans2 = obj.searchclgbyaddress(ad)

if ans2:
    print(ans2.collegeid)
    print(ans2.collegename)
    print(ans2.collegecontact)
    print(ans2.address)
    print(ans2.pincode)


else:
    print("NO MATCH FOUND!!")

