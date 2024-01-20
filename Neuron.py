import numpy as np
import math


#定义脉冲神经元类
class Neuron:
    def __init__(self, name, tau, R, I, theta_reset = 1, theta_rh = 0, delta_T = 0, u_reset = 0, a_0 = 0, u_c = 0, a = 0, tau_w = 0, b = 0):
        super(Neuron,self).__init__()

        #神经元参数
        self.name = name                    #脉冲神经元模型名称，可从'LIF','QIF','EIF','AdEx'中选择
        self.tau = tau                      #膜电位时间常数tau
        self.I = I                          #输入电流I
        self.R = R                          #电阻
        self.volt = 0                       #神经元膜电位
        self.theta_reset = theta_reset      #数值阈值
        self.theta_rh = theta_rh            #实际阈值
        self.delta_T = delta_T              #锐度参数
        self.u_reset = u_reset              #重置电位
        self.a_0 = a_0                      
        self.u_c = u_c
        self.a = a
        self.w = 0                          #自适应变量w
        self.tau_w = tau_w                  #自适应变量时间常数
        self.b = b                          
        self.diff_equ = ''                  #膜电位变化方程

    def TypeIdentify(self):
        #确定膜电位方程形式
        type_dict = {'LIF':'''(1-dt/self.tau)*self.volt[i]+dt/self.tau*(self.u_reset+self.I*self.R)''', \
                     'QIF':'''self.volt[i]+dt/self.tau* \
                            (self.a_0*(self.volt[i]-self.u_reset)*(self.volt[i]-self.u_c)+self.R*self.I)''', \
                     'EIF':'''(1-dt/self.tau)*self.volt[i]+dt/self.tau* \
                                (self.u_reset+self.I*self.R+self.delta_T* \
                                math.exp((self.volt[i]-self.theta_rh)/self.delta_T))''',\
                     'AdEx':'''(1-dt/self.tau)*self.volt[i]+dt/self.tau* \
                            (self.u_reset+self.I*self.R-self.w[i]*self.R+self.delta_T* \
                            math.exp((self.volt[i]-self.theta_rh)/self.delta_T))'''
                    }
        self.diff_equ = type_dict[self.name]
        print(self.diff_equ)

        

    #神经元仿真
    def sim(self, start, end, dt):
        self.TypeIdentify()                             #确定神经元类型
        time = np.arange(start, end, dt)                #生成仿真时间序列
        l = len(time)
        self.volt = [0 for i in range(l)]               #膜电位列表
        self.w = [0 for i in range(l)]                  #自适应变量列表

        for i in range(0,l-1):
            #离散化微分方程
            if self.volt[i] == self.theta_reset:
                self.volt[i+1] = self.u_reset
                if self.name == 'AdEx':
                    self.w[i+1] = self.w[i]
            else:


                self.volt[i+1]= eval(self.diff_equ)

                if self.name == 'AdEx':                 #如果是AdEx模型，则需要额外加入自适应方程
                    self.w[i+1] = (1-dt/self.tau_w)*self.w[i]+dt/self.tau_w* \
                    self.a*(self.volt[i]-self.u_reset)


                #脉冲产生机制
                if self.volt[i+1] >= self.theta_reset:
                    self.volt[i+1] = self.theta_reset
                    if self.name == 'AdEx':
                        self.w[i+1] = self.w[i+1]+self.b
        if self.name == 'AdEx':
            return time, self.volt, self.w                      #AdEx模型返回时间，膜电位，自适应变量
        else:
            return time, self.volt                              #其他模型返回时间，膜电位

