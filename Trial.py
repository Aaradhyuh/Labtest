import numpy as np
import matplotlib.pyplot as plt

sl=np.dtype([("Week","U20"),("Electronics","i4"),("Groceries","i4"),("Clothing","i4"),("Furniture","i4"),("Stationery","i4")])
ds=np.array([("Week1",120,200,230,75,45),("Week2",130,520,210,80,40),("Week3",125,530,220,70,50),("Week4",140,540,200,90,60)],dtype=sl)
print(ds)


def Wedo():
    p=ds["Electronics"][ds["Week"]=="Week1"]
    p1=ds["Electronics"][ds["Week"]=="Week2"]
    p2=ds["Electronics"][ds["Week"]=="Week3"]
    p3=ds["Electronics"][ds["Week"]=="Week4"]
    sumele=p+p2+p3+p1
    
    
    s=ds["Groceries"][ds["Week"]=="Week1"]
    s1=ds["Groceries"][ds["Week"]=="Week2"]
    s2=ds["Groceries"][ds["Week"]=="Week3"]
    s3=ds["Groceries"][ds["Week"]=="Week4"]
    sumg=s+s2+s3+s1
    
    f=ds["Furniture"][ds["Week"]=="Week1"]
    f1=ds["Furniture"][ds["Week"]=="Week2"]
    f2=ds["Furniture"][ds["Week"]=="Week3"]
    f3=ds["Furniture"][ds["Week"]=="Week4"]
    sumf=f+f2+f3+f1
    l=ds["Clothing"][ds["Week"]=="Week1"]
    l1=ds["Clothing"][ds["Week"]=="Week2"]
    l2=ds["Clothing"][ds["Week"]=="Week3"]
    l3=ds["Clothing"][ds["Week"]=="Week4"]
    sumc=l+l2+l3+l1
    
    q=ds["Stationery"][ds["Week"]=="Week1"]
    q1=ds["Stationery"][ds["Week"]=="Week2"]
    q2=ds["Stationery"][ds["Week"]=="Week3"]
    q3=ds["Stationery"][ds["Week"]=="Week4"]
    sums=q+q2+q3+q1
    return sumele,sumg,sumf,sumc,sums

sumele,sumg,sumf,sumc,sums=Wedo()


sal1=ds["Electronics"][ds["Week"]=="Week1"]
sal2 =ds["Groceries"][ds["Week"]=="Week1"]
sal3 =ds["Clothing"][ds["Week"]=="Week1"]
sal4 =ds["Furniture"][ds["Week"]=="Week1"]
sal5 =ds["Stationery"][ds["Week"]=="Week1"]
esumw1=sal1+sal2+sal3+sal4+sal5

pal1=ds["Electronics"][ds["Week"]=="Week2"]
pal2 =ds["Groceries"][ds["Week"]=="Week2"]
pal3 =ds["Clothing"][ds["Week"]=="Week2"]
pal4 =ds["Furniture"][ds["Week"]=="Week2"]
pal5 =ds["Stationery"][ds["Week"]=="Week2"]
esumw2=pal1+pal2+pal3+pal4+pal5

dal1=ds["Electronics"][ds["Week"]=="Week3"]
dal2 =ds["Groceries"][ds["Week"]=="Week3"]
dal3 =ds["Clothing"][ds["Week"]=="Week3"]
dal4 =ds["Furniture"][ds["Week"]=="Week3"]
dal5 =ds["Stationery"][ds["Week"]=="Week3"]
esumw3=dal1+dal2+dal3+dal4+dal5

cal1=ds["Electronics"][ds["Week"]=="Week4"]
cal2 =ds["Groceries"][ds["Week"]=="Week4"]
cal3 =ds["Clothing"][ds["Week"]=="Week4"]
cal4 =ds["Furniture"][ds["Week"]=="Week4"]
cal5 =ds["Stationery"][ds["Week"]=="Week4"]
esumw4=cal1+cal2+cal3+cal4+cal5


arr1=["Week1","Week2","Week3","Week4"]
cats = [ 'Electronics', 'Groceries', 'Clothing', 'Furniture', 'Stationery']

arr=[0,0,0,0,0]
arr[0]=int(sumele[0])
arr[1]=int(sumf[0])
arr[2]=int(sumc[0])
arr[3]=int(sumg[0])
arr[4]=int(sums[0])
print(arr)
plt.bar(cats,arr)
plt.show()