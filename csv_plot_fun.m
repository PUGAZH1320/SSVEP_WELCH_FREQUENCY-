close all;
data=csvread('o1_1min1.csv');
x=data(:, 1);
y=data(:, 2);
plot(x,y);
xlabel('X coordinates');
ylabel('Y coordinates');
title('o1');