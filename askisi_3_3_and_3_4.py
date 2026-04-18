from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import kstest


def f(x):
    m=2**10
    c=3
    a = 5
    return (a*x+c) % m

array_list = []

for i in range(500,5500):
    array_list.append(f(i))


#print(array_list)

freq = Counter(array_list)
print(freq)


sorted_keys = sorted(freq.keys())
sorted_values = [freq[k] for k in sorted_keys]

plt.bar(sorted_keys, sorted_values, color='steelblue', width=1.0)


plt.title('Συχνότητα Εμφάνισης Τιμών (0-1023)')
plt.xlabel('Τιμή (0-1023)')
plt.ylabel('Πλήθος Εμφανίσεων')

plt.savefig('my_histogram.png')


#-----Kolmogorov-Smirnov Test-----
sample_size = len(array_list)
print(f"Sample Size: {sample_size}")
normalized_data = np.array(array_list) / 1024
ks_statistic, p_value = kstest(normalized_data, 'uniform')
critical_value = 1.36 / np.sqrt(sample_size)
alpha = 0.05
print(f"KS Statistic: {ks_statistic:.4f}")
print(f"P-value: {p_value:.4f}")
print(f"Critical Value (alpha={alpha}): {critical_value:.4f}")

if ks_statistic > critical_value or p_value < alpha:
    print("Reject the null hypothesis: The sample does NOT follow the uniform distribution.")
else:
    print("Fail to reject the null hypothesis: The sample follows the uniform distribution.")