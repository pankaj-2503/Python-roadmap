# Matplotlib is low level graph plotting library in python that serves as visualization utility
import matplotlib.pyplot as plt
import numpy as np

x=np.array([1,2,3,4])
y=np.array([3,9,7,2])

# plt.plot(x,y)
# plt.show()


# plt.plot(x,y,'o') # dots only
# plt.show()


# ypoints=np.array([2,3,6,8,5])
# plt.plot(ypoints,marker='*')
# plt.show()


ypoints=np.array([2,3,8,9])  # marker|line|color ,
# '-'	Solid line	
# ':'	Dotted line	
# '--'	Dashed line	
# '-.'	Dashed/dotted line , color reference - r-red,g-green,y-yellow,w-white,k-black,m-magenta,c-cyan,b-blue
# ms -> marker size , mec -> marker edge color ,mfc -> marker face color , linewidth -> for marker width

# plt.plot(ypoints,'o--b',ms=10,mec='r',mfc='g')
# plt.show()



# x=np.array([1,3,5,7,8])
# y=np.array([7,8,9,1,0])
# plt.plot(x,y)
# plt.xlabel("Age")
# plt.title("Average Height Data",loc="left")
# plt.ylabel("Height")
# plt.grid()  # here we could pass argument axis='x' or 'y' , color='r' , linewidth=20,linestyle='--'
# plt.show()




# #plot 1:
# x = np.array([0, 1, 2, 3])
# y = np.array([3, 8, 1, 10])

# plt.subplot(2, 1, 1)
# plt.title("Sales")
# plt.plot(x,y)

# plt.subplots_adjust(hspace=0.6) # vertical space , similarly -> plt.subplots.tight_layout(pad=3)  increases horizontal space

# #plot 2:
# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])

# plt.subplot(2, 1, 2)
# plt.title("Income")
# plt.plot(x,y)

# plt.show()


# x=np.array([1,2,3,4])
# y=np.array([3,9,7,2])
# plt.bar(x,y,color='red',width=0.2)            # plt.barh(x,y) -> represent bar in horizontal , here height instead of width
# plt.show()

y = np.array([35, 25, 25, 15])
mylabel=["Apples","Banana","Guava","Dates"]
mycolor=["blue","green","yellow","red"]
myexplode=[0.08,0,0,0]
plt.pie(y,labels=mylabel,startangle=45,explode=myexplode,colors=mycolor,shadow=True)
plt.legend()
plt.show()