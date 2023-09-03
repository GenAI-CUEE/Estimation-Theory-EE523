# This code is part of Estimation Theory EE2102523 
# Lecture I: What is an Estimator? 
# by Suwichaya Suwanwimolkul 


import numpy as np
import matplotlib.pyplot as plt
import os


def sample_mean(data): 
    return np.mean(data)

def sample_variance(data): 
    return np.var(data, ddof=1)

def biased_sample_variance(data): 
    return np.var(data)


def bias_func(estimates, gt):
    return np.mean(estimates) - gt

def MSE_func(estimates, gt):
    var = np.var(estimates)  
    bias_square =  (np.mean(estimates) - gt)**2
    return var, bias_square

def sample_mean_simulation(data_population, select, size = 1000): 
    estimator_population = []
    for i in range(size):
        data_subsample = np.random.choice(data_population, select, replace=False)
        estimates = sample_mean(data_subsample)
        estimator_population.append(estimates)

    return estimator_population


def sample_variance_simulation(data_population, select, unbiased = True, size = 1000): 
    estimator_population = []
    for i in range(size):
        data_subsample = np.random.choice(data_population, select, replace=False)
        if unbiased:
            estimates = sample_variance(data_subsample)
        else:
            estimates = biased_sample_variance(data_subsample)
        
        estimator_population.append(estimates)

    return estimator_population


def hist_plot(sample_mean_estimates, data_population, gt, func, estimator_name = "sample mean", ploting = "Bias" , dirpath=None):
    value = func(sample_mean_estimates, gt)
    ploting_title = "%s [%s] = %.2f" % (ploting, estimator_name, value)
    
    plt.hist(sample_mean_estimates, bins=100, density=True, color="blue", alpha = 0.2, label="distribution of estimates") 
    plt.axvline(x=gt,  color="black",  linewidth=2,      label="True mean") 
    plt.axvline(x=np.mean(sample_mean_estimates), color="red", linestyle="--", label="Average of estimators")
    plt.legend(loc='lower right')
    plt.ylabel("Freq. (Density)")
    plt.xlabel("Samples")
    plt.title(ploting_title)
    plt.grid()
    plt.savefig(os.path.join(dirpath, "%s-%s.pdf" % (ploting, estimator_name)))
    plt.savefig(os.path.join(dirpath, "%s-%s.png" % (ploting, estimator_name)))
    plt.show()