import scipy.stats as stats
import numpy as np

def hypothesis_testing(sample_data, population_mean, alpha=0.05):
    # Step 1: State the hypotheses
    print("Step 1: State the hypotheses")
    print("H0: The sample mean is equal to the population mean (mu = {})".format(population_mean))
    print("H1: The sample mean is not equal to the population mean (mu ≠ {})".format(population_mean))
    print()
    
    # Step 2: Choose the significance level
    print("Step 2: Choose the significance level")
    print("Significance level (alpha) = {}".format(alpha))
    print()
    
    # Step 3: Calculate the test statistic
    print("Step 3: Calculate the test statistic")
    sample_mean = np.mean(sample_data)
    sample_std = np.std(sample_data, ddof=1)
    sample_size = len(sample_data)
    
    t_statistic = (sample_mean - population_mean) / (sample_std / np.sqrt(sample_size))
    print("Sample mean = {:.2f}".format(sample_mean))
    print("Sample standard deviation = {:.2f}".format(sample_std))
    print("Sample size = {}".format(sample_size))
    print("t-statistic = {:.2f}".format(t_statistic))
    print()
    
    # Step 4: Determine the critical value(s) or p-value
    print("Step 4: Determine the critical value(s) or p-value")
    # Two-tailed test
    t_critical = stats.t.ppf(1 - alpha/2, df=sample_size-1)
    p_value = (1 - stats.t.cdf(abs(t_statistic), df=sample_size-1)) * 2
    print("t-critical for two-tailed test = ±{:.2f}".format(t_critical))
    print("p-value = {:.4f}".format(p_value))
    print()
    
    # Step 5: Make a decision
    print("Step 5: Make a decision")
    if abs(t_statistic) > t_critical:
        print("Reject the null hypothesis (H0).")
        print("The sample mean is significantly different from the population mean.")
    else:
        print("Fail to reject the null hypothesis (H0).")
        print("The sample mean is not significantly different from the population mean.")
    
    return t_statistic, p_value

# Example usage
try:
    sample_data = list(map(float, input("Enter the sample data (space-separated values): ").split()))
    population_mean = float(input("Enter the population mean: "))
    alpha_input = input("Enter the significance level (default is 0.05): ")
    alpha = float(alpha_input) if alpha_input else 0.05

    hypothesis_testing(sample_data, population_mean, alpha)
except ValueError:
    print("Invalid input. Please enter numerical values for sample data, population mean, and significance level.")
