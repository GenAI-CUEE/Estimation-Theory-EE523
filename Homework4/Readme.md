# Homework 4

You can access Homework 4 through Google Collab  

<a target="_blank" href="https://colab.research.google.com/github/GabbySuwichaya/Estimation-Theory-EE523/blob/master/Homework4/simulation.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

## Simulations
 
Suppose that we want to estimate $\mathbf{X} \in \mathcal{R^N}$ from the observed data $\mathbf{Y} \in \mathcal{R^N}$ where $\mathbf{Y} = \mathbf{X} + N$; where $N\in \mathcal{R}$ is the noise corrupting the target signal. 

The probabilistic relationship between $\mathbf{X}$ and $\mathbf{Y}$ can be represented by the following probabilistic models:

- The likelihood is $ f_{\mathbf{Y}|\mathbf{X}}(\mathbf{y}|\mathbf{x}) = \mathcal{N}(\mathbf{y}| \mathbf{x}, \sigma_V^2) \propto \prod_i \frac{1}{\sqrt{2 \pi \sigma_V^2}} \exp{ - \frac{(y_i - x_i)^2}{2 \sigma_V^2} }$. 

- The prior for $x$ is a Gaussian-Gamma distribution, that is,  

	- $\mathbf{X} \sim f_{\mathbf{X}}(\mathbf{x})$  is $ f_{X }(\mathbf{x}| \mathbf{\mu}, \mathbf{\tau}) = \mathcal{N}(\mathbf{x}| \mathbf{\mu}, \mathbf{\tau}) \propto  \prod_i \sqrt{\frac{\tau_i}{2 \pi}} \exp{ \frac{\tau_i (x_i - \mu_i)^2}{2} }$ 
	- $\mathbf{\tau} \sim f_{\mathbf{\tau}}(\mathbf{\tau}) = \text{Gamma}(\mathbf{\tau}; \alpha, \beta) \propto  \prod_i  \tau_i^{\alpha - 1} \exp{- \beta \tau_i}$  

It is assume that the true distribution of $\mathbf{X}$ is the same as the prior distribution.  

Therefore, the joint distribution among the random variables are 

$$p(\mathbf{y}, \mathbf{x}, \mathbf{\tau}; \mathbf{\mu}, \sigma_V^2, \alpha, \beta) = \mathcal{N}(\mathbf{y}| \mathbf{x}, \sigma_V^2) \mathcal{N}(\mathbf{x}| \mathbf{\mu}, \mathbf{\tau}) \text{Gamma}(\mathbf{\tau}; \alpha, \beta).$$

Your observations are the random sample vector $\mathbf{Y}^1, \mathbf{Y}^2, ..., \mathbf{Y}^k$ that are independently and identically distributes according to each element in the multi-variate $\mathbf{Y}$ in $\mathcal{R^N}$.

All the implementation (60 scores) and analysis (40 scores) shall be done in a single Jupyter notebook. 

 

## How to submit your work
 

Please implement your work in the provided `.ipynb` file and save it with the task name, e.g., `simulation.ipynb`, and put the file into a folder with your task name `homework4`. Then, finally put them into a folder where your student id is used as the folder name. For example, 
    
- `6470160121/homework4/simulation.ipynb`
	
	 
Save each of your figures in `.png` format with a name  corresponding to each question ...For example, in responding to `Question 1`, you plot a  histogram of a prior to verify that it is a **Gamma** distribution, please name your file `Q1-Histogram-Verified-Gamma.png` ; otherwise, your scores for plotting graphs will be zero. 
	
- Then, put these saved figures in `homework4` folder, eg, `6470160121/homework4/Q1-Histogram-Verified-Gamma.png` .
	
- If you provide the saved figures, but you put use the incorrect notations for graph labeling, eg,  X-Y labels,  legends,  title, or did not provide any of them, your **scores for plotting graphs will also be zero**...
	
- I will *start marking* your `ipynb` file, **if and only if** there are  *plots and output showing*, and *without any error showing*. 
	
- Scores in each section will be given, **if and only if** your code runs successfully  and correctly without any bugs.
	 
- The `ipynb` file should be submitted online via `MS-Team's messanger` to me.   

- Please do not copy your friend, it is easy to see especially in this one...  