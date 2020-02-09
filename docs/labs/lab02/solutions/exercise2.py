a = -1
b = 1

# define the knots 
num_knots = 10
x = np.linspace(a,b,num_knots)

# define the function we want to approximate
y = 1/(1+25*(x**2))

# make the Cubic spline
yy = CubicSpline(x, y)

# OR make a linear spline
ll = interp1d(x, y)

# plot
xx = np.linspace(a,b,1000)
plt.plot(x,y,'*')
plt.plot(xx, ll(xx), label='linear');
plt.plot(xx, yy(xx), label='cubic');
plt.legend();
