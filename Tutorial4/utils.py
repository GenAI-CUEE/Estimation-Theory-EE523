
# This code is part of Estimation Theory EE2102523 
# Lecture II: Probabilistic Convergence 
# by Suwichaya Suwanwimolkul 

import numpy as np
import scipy.stats as sp
import matplotlib.pyplot as plt
import math
import os

def KL_expo(ZN_prob, GAUSS_prob, nmu=0, nsigma=1): 
    KL = np.sum(GAUSS_prob * np.log(GAUSS_prob / ZN_prob))
    return KL

def CTL_simulation(N_round=2, N_size= 1000, orginal_distribution="Bernoulli", dirpath=None, hide_showplots=False):
    XN = 0
    if orginal_distribution == "Bernoulli":
        
        p  = 0.5
        
        MU_Xi  = p
        STD_Xi = np.sqrt(p*(1-p))

        for count_round in range(N_round):
            XN += np.random.binomial(size=N_size, p=p, n=1) 

    else:
        a = 0 
        b = 1 

        MU_Xi  = 0.5*(a + b)
        STD_Xi = np.sqrt((1/12)*(b - a)**2 )

        for count_round in range(N_round):
            XN += np.random.uniform(a,b,N_size)


    # Calculated emperical mean 
    mean_emp = np.mean(XN) 
    std_emp  = np.std(XN)

    # Calculated true mean 
    mu = N_round*MU_Xi  
    sigma =  np.sqrt(N_round)*STD_Xi  

    # Normalize
    ZN = (XN - mu) / sigma

    # Gaussian samples
    gauss = np.random.standard_normal(N_size)
    nsigma = 1
    nmu = 0  

    ############################## Printing & Plotting ############################
    if not(hide_showplots):
        print("Mean per RV $\mu_x$: %.2f"  % MU_Xi)
        print("Std  per RV $\sigma_x$: %.2f" % STD_Xi)

        print('==============================')

        print("N round: %d" % N_round) 

        print("Empirical Mean: %.2f"  % mean_emp)
        print("Empirical std: %.2f" % std_emp) 

        print("True Mean ($n \mu_x$): %.2f"  %  mu)
        print("True standard deviation ($\sqrt{n} \sigma_x$): %.2f"  % sigma)

        print('==============================')

        print("Normalized Mean: %.2f"  % np.mean(ZN))
        print("Normalized std: %.2f" % np.std(ZN)) 
 

    # Plotting

    plt.figure(figsize=(10,7))
    
    count, bins, ignored = plt.hist(gauss, np.arange(-3, 3 + 0.2, 0.2), alpha=0.8, color="orange" , density=True, label="Normal Samples")
    plt.plot(bins, 1/(nsigma * np.sqrt(2 * np.pi)) *  np.exp( - (bins - nmu)**2 / (2 * nsigma**2) ),  linewidth=3, color='r', label="Standard Normal") 
    count_Zn, bins_Zn, ignored_Zn = plt.hist(ZN, np.arange(-3, 3 + 0.2, 0.2), alpha=0.5, color="Navy" , density=True, label="Zn (CTL)")
    
    
    KL_scores = KL_expo(count_Zn + 1e-6, count + 1e-6 , nmu=0, nsigma=1)
    if not(hide_showplots):
        print("KL %.2f" % KL_scores )

    textstr = '\n'.join([ 
        "N round: "+ str(N_round),  
        "Normalized Mean: %.2f"  % np.mean(ZN), 
        "Normalized std: %.2f" % np.std(ZN),
        "KL Divergence: %.2f" % KL_scores])

    plt.legend() 
    plt.text( -2.85, 0.95, textstr,horizontalalignment='left', verticalalignment='top', family='monospace')
    plt.ylabel("Freq. (Density)")
    plt.xlabel("Samples")
    plt.title("CTL at N=%d from %s" % (N_round, orginal_distribution))
    plt.xlim(-3,3)
    plt.ylim(0,1.0)
    plt.savefig(os.path.join(dirpath, "CLT_N%d_%s.pdf" % (N_round, orginal_distribution)))
    plt.savefig(os.path.join(dirpath, "CLT_N%d_%s.png" % (N_round, orginal_distribution)))
    if not(hide_showplots):
        plt.show() 
    plt.close('all')

    return KL_scores