This Github page is a part of **Estimation Theory EE2102523** 
by *Suwichaya Suwanwimolkul*.

Our goal is to provide the code-based visualization and exercises to understand the mathematics behind each of the lecture.

### Link to lectures and homeworks

[Link to Google Derive](https://drive.google.com/drive/folders/1VAEFqNYpjVlbc7dac92entSJlO_gzd-6?usp=drive_link)  

## Topics

I hope that at the end, I will be able to provide the coding scripts & excercises for the following topics

- [x] [Tutorial 1:  Estimator and its properties *to support Lecture I: What is Estimators?* ](Tutorial1/main.ipynb) 

<a target="_blank" href="https://colab.research.google.com/github/GabbySuwichaya/Estimation-Theory-EE523/blob/master/Tutorial1/main.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

    - Sampling from distirbution
    - Example of estimators (sample mean/sample variances)
    - Estimator properties (bias, mse, consistency). 
    - Homework Simulation
 
- [x] [Tutorial 2: Probabilistic Convergence *to support Lecture II: Probabilistic Convergence*](Tutorial2/main.ipynb) 

<a target="_blank" href="https://colab.research.google.com/github/GabbySuwichaya/Estimation-Theory-EE523/blob/master/Tutorial2/main.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>
    - Convergence in distribution, 
    - Central limit Theorems, 
    - KL divergence, 
    - Convergence in probability, 
    - Almost sure Convergence simulation. 
    - Homework Simulation

- [x] [Tutorial 3](Tutorial3/main.ipynb): KL-Divergence Loss *to support Lecture V: MLE-KL, Conditional MLE,  MLE-MSE, MLE-MAE, MMSE*
    - KL Divergence
    - Central Limit Theorem Example 
    - Variational Auto Encoder
    - Why KL Divergence is used in VAE
    - Apply VAE to reconstruct the image data

- [x] [Tutorial 4](Tutorial4/main.ipynb): Wiener Filter and MAP Esitmation *to support Lecture VI: LMSE, Wiener Filtering, Maximum A Posteriori*  
    - Wiener Filtering
    - Auto/Cross-Correlation Checking 
    - MAP Esitmation 
    - Gaussian-Laplacian conjugate prior and extension to estimate other unknowns in the posteriori distribution
    - Apply to reconver image data from compression in compressive sensing.

## Getting Started

1. Change the directory to the `Tutorial` folder.
2. Look for the  instructions (e.g. [Tutorial 1 Readme](Tutorial1/Readme.md)) for install dependencies. 
3. You may execute the `main` file in python or ipynb fileformat. 

* Course materials (such as HW and lecture notes) maybe provided in each `Tutorial` folder. 
* Each tutorial runs independently in its own environment. 