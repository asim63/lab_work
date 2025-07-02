clc;
clear all;
close all;
fs = 8000;
fm = 20;
fc = 500;
Am = 1;
Ac = 1;
t = [0: 0.1*fs]/fs;
m = Am * cos(2 * pi * fm * t);
c = Ac * cos(2 * pi * fc * t);
B = 15;
S1 = Ac*cos((2*pi*fc*t) + B*sin(2*pi*fm*t));

subplot(3,1,1);
plot(t,m);
xlabel('Time');
ylabel('Amplitude');
title('Message/Asim');
grid on;

subplot(3,1,2);
plot(t,c);
xlabel('Time');
ylabel('Amplitude');
title('Carrier/Asim');
grid on;

subplot(3,1,3);
plot(t,S1);
xlabel('Time');
ylabel('Amplitude');
title('Modulated');
grid on;
