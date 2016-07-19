import time, os

ADC_PATH= os.path.normpath('/proc/')
ADC_FILENAME = "adc"
PWM_PATH= os.path.normpath('/sys/class/leds/')
multiplevalue = 1.5 #this use to convert adc value to the temperature
adcFiles = []

for i in range(0,6):
  adcFiles.append(os.path.join(ADC_PATH, ADC_FILENAME+str(i)))

while True:
    fd = open(adcFiles[1], 'r')
    fd.seek(0)
    value= fd.read(16).strip("\n")
    numvalue=int(value.split(":")[1])
    print numvalue*multiplevalue
    fd.close()
