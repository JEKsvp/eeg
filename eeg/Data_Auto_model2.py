import numpy as np
from matplotlib.pyplot import *
from struct import unpack
import os
rcParams['font.sans-serif']=['Arial']

chD = 3400

NumberChannel0 = 0
NumberChannel1 = 1
NumberChannel2 = 2
NumberChannel3 = 3


SumChannel = 4
Bits = 2
    
#Считывание данных
ListNameFile = []
for f in os.listdir('../data/'):
    if os.path.splitext(f)[1] == '.txt':
        ListNameFile.append(os.path.splitext(f)[0])

for NameFile in ListNameFile:
    print(NameFile)

    fname = '../data/'+NameFile + '.bin'
    f = open(fname, 'rb')

    #Считывание разметки
    figure(figsize=(15, 7))
    MasRat = np.loadtxt('../data/'+NameFile+'.txt')
    for i in range (0, len(MasRat)):
        beginSEC = float(MasRat[i,0])
        print(beginSEC)
        begin = int(beginSEC*chD)
        endSEC =  float(MasRat[i,1])
        end = int(endSEC*chD)
        seizureSEC = endSEC - beginSEC
        seizure = int(seizureSEC*chD)
        plusSEC = 5
        plus = int(plusSEC*chD)
        length = 2*plus+seizure

        mylist = []
        f.seek(SumChannel*Bits*(begin-plus))
        buffer = f.read(SumChannel*Bits*length)
        mylist = unpack(SumChannel*length*'h', buffer)
            
        ch0 = mylist[NumberChannel0::SumChannel]
        ch1 = mylist[NumberChannel1::SumChannel]
        ch2 = mylist[NumberChannel2::SumChannel]
        ch3 = mylist[NumberChannel3::SumChannel]
        
        widthSEC=0.2
        width = int(widthSEC*chD)
        stepSEC=0.1
        step = int(stepSEC*chD)
        NumberWindow = int((len(ch0)-width)/(stepSEC*chD))+1

        clf()
        for cannum in range(SumChannel-1):
            if cannum==0:
                channel='RTN'
                ch=np.array(ch0)
            if cannum==1:
                channel='VPM'
                ch=np.array(ch1)
            if cannum==2:
                channel='Cortex'
                ch=np.array(ch2)+np.array(ch3)

            t = np.linspace(0, seizureSEC+2*plusSEC, len(ch))
            # Строим временной ряд
            subplot(SumChannel-1, 2, 2*cannum+1)
            title(channel + ' (time series)')
            plot(t, ch/1000, color = 'blue', lw=0.5)
            axvline(plusSEC, color='black', lw=2)
            axvline(plusSEC+seizureSEC, color='black', lw=2)
            xlim(t[0],t[-1])
            ylim([-5,35])
            ylabel(r'$U$, mV')
            xlabel(r'$t$, s')
            grid(True)

            # Строим спектрограмму
            subplot(SumChannel-1, 2, 2*cannum+2)
            title(channel + ' (spectrogram)')
            specgram(ch, NFFT=chD, Fs=chD, noverlap=int(0.9*chD), cmap=cm.jet,
                     mode='magnitude', vmin=90, vmax=130)
            ylim([0, 50])
            xlim ([0, (seizureSEC+2*plusSEC)])
            axvline(plusSEC, color='black', lw=2)
            axvline(plusSEC+seizureSEC, color='black', lw=2)
            ylabel(r'$Frequency$, Hz')
            xlabel(r'$t$, s')
            grid(True)

        
        tight_layout()
        savefig(NameFile+'_'+str(beginSEC)+'sec.png')
