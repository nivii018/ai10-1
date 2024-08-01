from matplotlib import pyplot as pi
us=[12,32,16,45]
la=["asus","dell","lenovo","hp"]
e=[0,0,0,0.4]
c=["g","c","#880000","#473c88"]
pi.pie(us,labels=la,startangle=270,explode=e,autopct='%1.2f%%')
pi.show()