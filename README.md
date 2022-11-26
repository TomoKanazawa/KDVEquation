# KDVEquation
A solution for the KDV equation using the Runge-Kutta method. 
The result of time diveropment will be saved in a folder named "result" as you can see in the code.

Look at this site to know what's the KDV equation.
https://en.wikipedia.org/wiki/Korteweg–De_Vries_equation

The equation soluved here:
u_t + u * u_x + delta**2 * u_xxx = 0
u(x,0) = cos(x)
delta = 0.022

In this solution, the Galerking method is used to give, which is one of the the methods of weighted residual.
The residul R(x,t) can be written as:

R(x,t) = u_t + u * u_x + delta**2 * u_xxx

Now, Discrete fourier transformation is used to make this formula easier to solve:
u(x,t) = ∑ [ u(t) * exp(-ikx) ] (∑: k = -N/2, -N/2 + 1, ..., N/2 - 1, N/2)

Then integral the weighted residual multiplying e(-ix) and meke a equation requiring that should be 0.
And we get:

u'_t = delta**2 * i * k**3 * u' - (nonliner term)

Finally, Runge-Kutta method is used to calculate the time development.
