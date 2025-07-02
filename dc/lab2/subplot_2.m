t = 0:0.01:2;
y = sin(2*3.1415*t);
subplot(2,2,1);
plot(t,y);
title('Harmonic 1/Asim/08');
xlabel('Time(s)');
ylabel('Amplitude');
grid on;


z = sin(2*3.1415*2*t);
subplot(2,2,2);
plot(t,z);
title('Harmonic 2/Asim/08');
xlabel('Time(s)');
ylabel('Amplitude');
grid on;

g = cos(2*3.1415*3*t);
subplot(2,2,3);
plot(t,g);
title('Harmonic 3/Asim/08');
xlabel('Time(s)');
ylabel('Amplitude');
grid on;

x = y+g+z;
subplot(2,2,4);
plot(t,x);
title('Composite /Asim/ 08');
xlabel('time');
ylabel('amplitude');
grid on;
