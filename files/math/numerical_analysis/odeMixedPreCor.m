clc;
clear;
close all;
%function definition
function [x, y] = odeMixedPreCor(ODE, a, b, h, yINI)
  N = (b-a)/h;
  x = a:h:b;
  y = zeros(1, N);
  y(1) = yINI;
  
  %first step:
  for counter = 1:2
    %predictor with Euler's explicit method
    y(counter+1) = y(counter) + ODE(x(counter), y(counter))*h;
    y_k = y(counter+1);
    %corrector with an implicit method
    while true
      y(counter+1) = y(counter) + (ODE(x(counter), y(counter))+ODE(x(counter+1), y_k))*h/2;
      if norm((y(counter+1)-y_k)/y_k) < 5*10^(-4)
        break
      else
        y_k = y(counter+1);
      end 
    endwhile
  end
  
  %following steps:
  for counter = 3:N
    %predictor with Adams-Bashforth's explicit method
    y(counter+1) = y(counter) + (23*ODE(x(counter),y(counter))...
                                -16*ODE(x(counter-1),y(counter-1))...
                                +5*ODE(x(counter-2),y(counter-2)))*h/12;
    y_k = y(counter+1);
    %corrector with Adams-Moulton implicit method
    while true
      y(counter+1) = y(counter) + (5*ODE(x(counter+1), y_k)...
                                  + 8*ODE(x(counter), y(counter))
                                  - ODE(x(counter-1), y(counter-1)))*h/12;
      if norm((y(counter+1)-y_k)/y_k) < 10^(-5)
        break
      else
        y_k = y(counter+1);
      end 
    endwhile
  
  end
end

%User defined code
ODE = @(x, y)(1 - y/x);
fexact = @(x)(x./2 + 9./(2.*x));
[x, y] = odeMixedPreCor(ODE, 1, 6, 0.25, 5);
y_exact = fexact(x);
Error = y_exact - y;

%Get numerical solution
fprintf('predict(%0.2f) = %f,  f_exact = %f,  Error = %f\n', [x;y;y_exact;Error]);

%Plot numerical and then analytical solution
plot(x,y)
hold on
plot(x,y_exact);
legend('Numerical', 'Exact');
xlabel('x');
ylabel('y');

%get export as a xlsx file
xlswrite('report.xlsx', [x', y', y_exact', Error']);