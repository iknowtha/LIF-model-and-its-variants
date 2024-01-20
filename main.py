import numpy as np
import matplotlib.pyplot as plt
import math
from Neuron import Neuron



#实例化LIF神经元，需要配置参数name, tau, R, I
LIF = Neuron(name = 'LIF', tau = 20, R = 1, I =2)
time1, results1 = LIF.sim(start = 0, end = 100, dt = 0.1)



#实例化QIF神经元,需要配置参数name, tau, R, I, theta_reset, a_0, u_c
QIF = Neuron(name = 'QIF', tau =20, R = 1, I =2,theta_reset = 1,\
             a_0 = 7, u_c = 0.5)
time2, results2 = QIF.sim(start = 0, end = 100, dt = 0.1)


#实例化EIF神经元,需要配置参数name, tau, R, I, theta_reset, theta_rh, delta_T
EIF = Neuron(name = 'EIF',tau =20, R = 1, I =1.5, theta_reset = 1, theta_rh = 0.7, delta_T = 0.2)
time3, results3 = EIF.sim(start = 0, end = 100, dt = 0.1)


#实例化AdEx神经元,需要配置参数name, tau, R, I, theta_reset, theta_rh, a, tau_w, b, delta_T
AdEx = Neuron(name = 'AdEx', tau = 10, R = 1, I = 1.2, theta_reset = 1,\
               theta_rh = 0.7, a = 1, tau_w = 30, b =0.1, delta_T = 0.2)
time4, results4, w = AdEx.sim(start = 0, end = 500, dt = 0.1)


#仿真效果
fig, ax = plt.subplots(figsize=(8,6))
plt.subplots_adjust(hspace=0.4, wspace = 0.4)

#LIF
plt.subplot(2,2,1)
plt.plot(time1, results1,linewidth = 2)
plt.title("LIF model")
plt.xlabel('Time(ms)')
plt.ylabel('Membrane potential')

#QIF
plt.subplot(2,2,2)
plt.plot(time2, results2,linewidth = 2)
plt.title("QIF model")
plt.xlabel('Time(ms)')
plt.ylabel('Membrane potential')

#EIF
plt.subplot(2,2,3)
plt.plot(time3, results3,linewidth = 2)
plt.title("EIF model")
plt.xlabel('Time(ms)')
plt.ylabel('Membrane potential')

#AdEx
plt.subplot(2,2,4)
plt.plot(time4, results4,linewidth = 2)
plt.title("AdEx model")
plt.xlabel('Time(ms)')
plt.ylabel('Membrane potential')
plt.show()

