## Simulations

Suppose that we want to estimate $\bm{X} \in \mathcal{R^N}$ from the observed data $\bm{Y} \in \mathcal{R^N}$ where $\bm{Y} = \bm{X} + N$; where $N\in \mathcal{R}$ is the noise corrupting the target signal. 

The probabilistic relationship between $\bm{X}$ and $\bm{Y}$ can be represented by the following probabilistic models:

- The likelihood is $ f_{\bm{Y}|\bm{X}}(\bm{y}|\bm{x}) = \mathcal{N}(\bm{y}| \bm{x}, \sigma_V^2) \propto \prod_i \frac{1}{\sqrt{2 \pi \sigma_V^2}} \exp{ - \frac{(y_i - x_i)^2}{2 \sigma_V^2} }$. 

- The prior for $x$ is a Gaussian-Gamma distribution, that is,  

	- $\bm{X} \sim f_{\bm{X}}(\bm{x})$  is $ f_{X }(\bm{x}| \bm{\mu}, \bm{\tau}) = \mathcal{N}(\bm{x}| \bm{\mu}, \bm{\tau}) \propto  \prod_i \sqrt{\frac{\tau_i}{2 \pi}} \exp{ \frac{\tau_i (x_i - \mu_i)^2}{2} }$ 
	- $\bm{\tau} \sim f_{\bm{\tau}}(\bm{\tau}) = \text{Gamma}(\bm{\tau}; \alpha, \beta) \propto  \prod_i  \tau_i^{\alpha - 1} \exp{- \beta \tau_i}$  

It is assume that the true distribution of $\bm{X}$ is the same as the prior distribution.  

Therefore, the joint distribution among the random variables are 

$$p(\bm{y}, \bm{x}, \bm{\tau}; \bm{\mu}, \sigma_V^2, \alpha, \beta) = \mathcal{N}(\bm{y}| \bm{x}, \sigma_V^2) \mathcal{N}(\bm{x}| \bm{\mu}, \bm{\tau}) \text{Gamma}(\bm{\tau}; \alpha, \beta).$$

Your observations are the random sample vector $\bm{Y}^1, \bm{Y}^2, ..., \bm{Y}^k$ that are independently and identically distributes according to each element in the multi-variate $\bm{Y}$ in $\mathcal{R^N}$.

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