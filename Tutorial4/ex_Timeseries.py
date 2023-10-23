import numpy as np 
import matplotlib.pyplot as plt 
import numpy as np
from scipy.linalg import toeplitz 
import pdb
# Constants in simuation
N       = 1000
varu    = 1
varv    = 10
a       = 0.999

#% Generate the noisy observed signal
u       = np.sqrt(varu)*np.random.randn(N)
x       = [0] #; % Initialize x to be the mean

for n in range(1,N):
    x.append(a*x[n-1] + u[n])

v       = np.sqrt(varv)*np.random.randn(N)
y       = x + v 

# Step 1
M       = 100 
tau     = np.arange(0,M)  

# Step 2
rvv     = np.zeros_like(tau)
rvv[0]  = varv;             # Autocorrelation is a Kronecker Delta function

# Step 3 
rss     = (a**abs(tau))/(1-a**2)*varu 
rxs     = rss 
# Step 4
rxx     = rss + rvv            # Autocorrelation vector
 
# Step 5
Rxx     = toeplitz(rxx);       # Autocorrelation matrix 

# Step 6

# Step 7 
w_      = np.linalg.inv(Rxx).dot(rxs) 
 
# Step 8 
g = []
for n_ in range(M-1,N):
    g.append(w_.dot(np.flipud(y[(n_-M+1):n_+1])))


stime_index = np.arange(0,N)
ytime_index = np.arange(M-1,N)
# Plot result
plt.plot(stime_index, y, label="Observed: y[n]", color="gray")
plt.plot(stime_index, x, label="Original: x[n]", color="red") 
plt.plot(ytime_index, g, label="Predict: g[n]", linestyle= '--', color="blue")

plt.grid()

plt.legend() #'y(n)','g(n)','x(n)'
plt.xlabel("Time Index, n")
plt.ylabel("Amplitude")
plt.title('Wiener filtering')
plt.show()