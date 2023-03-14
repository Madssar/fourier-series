import json
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

t = np.linspace(-np.pi, np.pi)

# Load data from the fourierData.json file
with open("fourierData.json","r") as fd:
    data = json.load(fd)

# creating sin square waves
sinWave = 0
for sine in data["sin"]:
    y = np.sin(sine["freq"]*t)/sine['amp'] #extracting frequency and amplitude from fourierData.json,multiply frequency with x and dividing it with amplitude
    sinWave += y

# creating cos waves
cosWave = 0
for cosine in data["cos"]:
    y = np.cos(cosine["freq"]*t)/cosine['amp']
    cosWave += y

# creating sum of sin and cos waves
resultant = sinWave + cosWave

plt.plot(t, sinWave, label="sin-waves") #ploting sin square waves
plt.plot(t, cosWave, label="cos-waves") #ploting cos waves
plt.plot(t, resultant, label="Aggregation") #ploting sum of sin and cos waves
plt.title("Aggregation of sin and cos waves")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()




#Animation on Sin square wave
zipSin = list(zip(t,sinWave))

sortedSin = sorted(zipSin,reverse = True) #sorting values by second value
x = [sin[0] for sin in sortedSin]
y = [sin[1] for sin in sortedSin]

def animateSin(sin):
    plt.scatter(x[:sin],y[:sin],color='red',s=10)
    
mySinAni = animation.FuncAnimation(plt.gcf(),
                  animateSin, 
                  frames= range(0,len(x)),#frame will animate until length of x
                  )



#Animation on Cos waves
zipCos = list(zip(t,cosWave))

sortedCos = sorted(zipCos,reverse = True) #sorting values by second value
cosX = [cos[0] for cos in sortedCos]
cosY = [cos[1] for cos in sortedCos]

def animateCos(cos):
    plt.scatter(cosX[:cos],cosY[:cos],color='red',s=10)
    
myCosAni = animation.FuncAnimation(plt.gcf(),
                  animateCos, 
                  frames= range(0,len(cosX)),#frame will animate until length of x
                  )



#Animation on resultant waves
zipResultant = list(zip(t,resultant))

sortedResultant = sorted(zipResultant,reverse = True) #sorting values by second value
resultantX = [resultant[0] for resultant in sortedResultant]
resultantY = [resultant[1] for resultant in sortedResultant]

def animateResultant(resultant):
    plt.scatter(resultantX[:resultant],resultantY[:resultant],color='red',s=10)
    
myResultantAni = animation.FuncAnimation(plt.gcf(),
                  animateResultant, 
                  frames= range(0,len(resultantX)),#frame will animate until length of x
                  )
# %matplotlib qt   run this command in console then run the program to see animation

#sorting and printing values without graphic library
sort_sin = sorted(sinWave, reverse=True)
print(f'Sin sorted data={sort_sin}')


sort_cos = sorted(cosWave, reverse=True)
print(f'\nCos sorted data={sort_cos}')


sort_resultant = sorted(resultant, reverse=True)
print(f'\nResultant sorted data={sort_resultant}')


plt.savefig("output") #saving chart on current working directory

