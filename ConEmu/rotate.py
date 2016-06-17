import os, random
files = os.listdir("C:\\Users\\bobby\\Pictures\\cylonsce\\")
os.rename("C:\\Users\\bobby\\Pictures\\cylonsce\\1.png","C:\\Users\\bobby\\Pictures\\cylonsce\\temp.png")
files.pop(0)
choice = random.choice(files)
print ("choice " + choice) 
os.rename("C:\\Users\\bobby\\Pictures\\cylonsce\\" + choice ,"C:\\Users\\bobby\\Pictures\\cylonsce\\1.png")
os.rename("C:\\Users\\bobby\\Pictures\\cylonsce\\temp.png", "C:\\Users\\bobby\\Pictures\\cylonsce\\" + choice)

#os.rename(files[, )
