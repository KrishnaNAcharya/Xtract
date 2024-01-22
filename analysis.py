import numpy as np
from scipy import stats
from scipy.stats import chi2_contingency,mode, skew, kurtosis,norm, expon, uniform, binom, poisson
import matplotlib.pyplot as plt
#*****************************************************************************
#*****************************************************************************
#DESCRIPTIVE ANALYSIS
def print_mean(data):
    print(f"Mean: {np.mean(data)}")

def print_median(data):
    print(f"Median: {np.median(data)}")

def print_mode(data):
    print(f"Mode: {mode(data).mode[0]}")

def print_range(data):
    print(f"Range: {np.ptp(data)}")

def print_variance(data):
    print(f"Variance: {np.var(data)}")

def print_std_deviation(data):
    print(f"Standard Deviation: {np.std(data)}")

def print_percentiles(data):
    percentiles = np.percentile(data, [25, 75])
    print(f"25th Percentile (Q1): {percentiles[0]}")
    print(f"75th Percentile (Q3): {percentiles[1]}")

def print_skewness(data):
    print(f"Skewness: {skew(data)}")

def print_kurtosis(data):
    print(f"Kurtosis: {kurtosis(data)}")

def plot_histogram(data):
    plt.hist(data, bins=20, edgecolor='black')
    plt.title("Histogram")
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.show()

# Sample data
data = np.random.normal(50, 10, 1000)

# Central Tendency Measures
print_mean(data)
print_median(data)
print_mode(data)

# Dispersion Measures
print_range(data)
print_variance(data)
print_std_deviation(data)

# Position Measures
print_percentiles(data)

# Distribution Shape Measures
print_skewness(data)
print_kurtosis(data)

# Plot Histogram
plot_histogram(data)


#*************************************************************************************
#**************************************************************************************
#PROBABBILITY DISTRIBUTIONS
# Continuous Distributions

def generate_normal_distribution(mu, sigma, size):
    data = np.random.normal(mu, sigma, size)
    print(f"Generated Normal Distribution: {data}")
    
def generate_exponential_distribution(lambda_param, size):
    data = np.random.exponential(1/lambda_param, size)
    print(f"Generated Exponential Distribution: {data}")

def generate_uniform_distribution(low, high, size):
    data = np.random.uniform(low, high, size)
    print(f"Generated Uniform Distribution: {data}")

# Discrete Distributions

def generate_binomial_distribution(n, p, size):
    data = np.random.binomial(n, p, size)
    print(f"Generated Binomial Distribution: {data}")

def generate_poisson_distribution(lambda_poisson, size):
    data = np.random.poisson(lambda_poisson, size)
    print(f"Generated Poisson Distribution: {data}")

# Plotting

def plot_histogram(data, bins, title, color):
    plt.hist(data, bins=bins, color=color, alpha=0.7)
    plt.title(title)
    plt.show()

# Parameters
size = 1000

# Continuous Distributions
generate_normal_distribution(0, 1, size)
generate_exponential_distribution(1, size)
generate_uniform_distribution(0, 1, size)

# Discrete Distributions
n, p = 10, 0.5
generate_binomial_distribution(n, p, size)

lambda_poisson = 3
generate_poisson_distribution(lambda_poisson, size)
#********************************************************************************************
#********************************************************************************************

#HYPOTHESIS TESTING
# T-tests

def one_sample_t_test(sample, pop_mean):
    t_stat, p_value = stats.ttest_1samp(sample, pop_mean)
    print(f"One-Sample t-test:")
    print(f"T-statistic: {t_stat}")
    print(f"P-value: {p_value}")

def two_sample_t_test(sample1, sample2):
    t_stat, p_value = stats.ttest_ind(sample1, sample2)
    print(f"Two-Sample t-test:")
    print(f"T-statistic: {t_stat}")
    print(f"P-value: {p_value}")

def paired_t_test(before, after):
    t_stat, p_value = stats.ttest_rel(before, after)
    print(f"Paired t-test:")
    print(f"T-statistic: {t_stat}")
    print(f"P-value: {p_value}")

# ANOVA

def one_way_anova(*groups):
    f_stat, p_value = stats.f_oneway(*groups)
    print(f"One-Way ANOVA:")
    print(f"F-statistic: {f_stat}")
    print(f"P-value: {p_value}")

def two_way_anova(data, factor1, factor2):
    model = stats.ols("value ~ C({}) * C({})".format(factor1, factor2), data).fit()
    anova_table = stats.anova_lm(model, typ=2)
    print("Two-Way ANOVA:")
    print(anova_table)

# Z-test

def z_test(sample, pop_mean, pop_std):
    z_stat, p_value = stats.ztest(sample, value=pop_mean, std_dev=pop_std)
    print(f"Z-test:")
    print(f"Z-statistic: {z_stat}")
    print(f"P-value: {p_value}")

# Example usage

# Generate sample data
np.random.seed(42)
sample1 = np.random.normal(30, 5, 50)
sample2 = np.random.normal(35, 5, 50)
before = np.random.normal(40, 5, 30)
after = before + np.random.normal(5, 2, 30)

# T-tests
one_sample_t_test(sample1, 30)
two_sample_t_test(sample1, sample2)
paired_t_test(before, after)

# ANOVA
one_way_anova(sample1, sample2, before)
two_way_anova(data={'value': np.concatenate([sample1, sample2, before, after]),
                    'group': ['Group1'] * 50 + ['Group2'] * 50 + ['Before'] * 30 + ['After'] * 30},
              factor1='group', factor2='group')

# Z-test
z_test(sample1, 30, 5)
