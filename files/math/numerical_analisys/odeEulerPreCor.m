clc;
clear;
close all;
%function definition
function [x, y] = odeEulerPreCor(ODE, a, b, h, yINI)
  N = (b-a)/h;
  x = a:h:b;
  y = zeros(1, N);
  y(1) = yINI;
  for counter = 1:N
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
end

%User defined code
ODE = @(x, y)(y + x^3);
fexact = @(x)(7*exp(x)-x.^3-3*x.^2-x.*6.-6);
[x, y] = odeEulerPreCor(ODE, 0, 1.5, 0.1, 1);

%Get numerical solution
fprintf('predict(%0.1f) = %f \n', [x;y]);

%Plot numerical and then analytical solution
plot(x,y)
hold on
y_exact = fexact(x);
plot(x,y_exact);
legend('Numerical', 'Exact');
xlabel('x');
ylabel('y');
