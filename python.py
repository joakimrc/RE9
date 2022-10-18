import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st
import pandas as pd

def selectData(indexLists):
    timeTemp = np.array([])
    heliumTemp = np.array([])
    hydrogenTemp = np.array([])
    nitrogenTemp = np.array([])
    methaneTemp = np.array([])
    co2Temp = np.array([])
    for j in range(len(indexLists)):
        for i in indexLists[j]:
            timeTemp = np.append(timeTemp, time[i])
            heliumTemp = np.append(heliumTemp, helium[i])
            hydrogenTemp = np.append(hydrogenTemp, hydrogen[i])
            nitrogenTemp = np.append(nitrogenTemp, nitrogen[i])
            methaneTemp = np.append(methaneTemp, methane[i])
            co2Temp = np.append(co2Temp, co2[i])
        
    return timeTemp, heliumTemp, hydrogenTemp, nitrogenTemp, methaneTemp, co2Temp
    

print("----")

labData = pd.read_excel('RE6/FelleslabB20.xls', usecols="B,G:L",header=0,skiprows=[1,2,3,4,5,45,46,47,48])
#print(labData)
time = labData["Injection date"].tolist()
helium = labData["He (A)"].tolist()
hydrogen = labData["H2 (A)"].tolist()
nitrogen = labData["N2 (A)"].tolist()
methane = labData["CH4 (A)"].tolist()
co2 = labData["CO2 (A)"].tolist()

n2VolumeFlow = 30


time = np.array(time)
helium = np.array(helium)
hydrogen = np.array(hydrogen)
nitrogen = np.array(nitrogen)
methane = np.array(methane)
co2 = np.array(co2)

co2flowrate = []
#total = labData["Total raw"].tolist()
calibrate_1 = [1,2,3]
calibrate_2 = [6,7,8]
calibrate_3 = [9,10,11]

step1 = [15,16,17]
step2 = [22,23,24]
step3 = [26,27,28]
step4 = [31,32,33]
step5 = [36,37,38]

names = ["Calibrate 1", "Calibrate 2", "Calibrate 3", "Step 1", "Step 2", "Step 3", "Step 4", "Step 5"]


indexLists = [calibrate_1,calibrate_2,calibrate_3, step1, step2, step3, step4, step5]

for j in range(len(indexLists)):
    print(f"{names[j]}: ")
    timeTemp = np.array([])
    heliumTemp = np.array([])
    hydrogenTemp = np.array([])
    nitrogenTemp = np.array([])
    methaneTemp = np.array([])
    co2Temp = np.array([])


    for i in indexLists[j]:
        timeTemp = np.append(timeTemp, time[i])
        heliumTemp = np.append(heliumTemp, helium[i])
        hydrogenTemp = np.append(hydrogenTemp, hydrogen[i])
        nitrogenTemp = np.append(nitrogenTemp, nitrogen[i])
        methaneTemp = np.append(methaneTemp, methane[i])
        co2Temp = np.append(co2Temp, co2[i])
    
    print(co2Temp)
    plt.plot(timeTemp, heliumTemp,'r.-')
    plt.plot(timeTemp, hydrogenTemp, 'g.-')
    plt.plot(timeTemp, nitrogenTemp, 'b.-')
    plt.plot(timeTemp, methaneTemp, 'y.-')
    plt.plot(timeTemp, co2Temp, 'k.-')
    rrfco2 = co2Temp * n2VolumeFlow / nitrogenTemp
    print(rrfco2)
    #plt.legend()

plt.plot(time[1], helium[1],'r.-', label="$He$")
plt.plot(time[1], hydrogen[1], 'g.-', label="$H_2$")
plt.plot(time[1], nitrogen[1], 'b.-', label="$N_2$")
plt.plot(time[1], methane[1], 'y.-', label="$CH_4$")
plt.plot(time[1], co2[1], 'k.-', label="$CO_2$")
plt.legend()
    
plt.savefig("fig.png")


F_co2 = np.array([4.4615e-4, 4.4615e-4, 4.4615e-4, 6.6923e-4, 6.6923e-4, 6.6923e-4, 8.9230e-4, 8.9230e-4, 8.9230e-4])

F_no2 = 0.0013385

time_cal, A_he_cal, A_h2_cal, A_n2_cal, A_me_cal, A_co2_cal = selectData([calibrate_1, calibrate_2, calibrate_3])
print(A_co2_cal)
RF_co2_elns = A_co2_cal * F_no2 / A_n2_cal

plt.figure(200)
plt.plot(F_co2, RF_co2_elns, 'k.')
slope, intercept, r, p, se = st.linregress(F_co2, RF_co2_elns)
plt.plot(F_co2, (slope*F_co2+intercept), 'r-')
plt.xlabel("Molar flow rate of $CO_2$, [mol/min]")
plt.ylabel('$A_{CO_2} F_{IS}/A_{IS}$')

plt.savefig("RFelns.png")




