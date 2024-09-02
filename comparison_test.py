import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import wasserstein_distance
from scipy.spatial.distance import jensenshannon

np.random.seed(33)

reference_data = np.random.normal(loc=0, scale=1, size=100)
current_data = np.random.normal(loc=0, scale=1, size=100000)


w_distance = wasserstein_distance(reference_data, current_data)

ref_hist, ref_bins = np.histogram(reference_data, bins=50, density=True)
cur_hist, cur_bins = np.histogram(current_data, bins=50, density=True)

js_distance = jensenshannon(ref_hist, cur_hist)

print(f"Wasserstein Distance: {w_distance}")
print(f"Jensen-Shannon Distance: {js_distance}")

plt.figure(figsize=(12, 6))
plt.hist(reference_data, bins=50, alpha=0.5, label='Reference Data', density=True)
plt.hist(current_data, bins=50, alpha=0.5, label='Current Data', density=True)
plt.title(f"Wasserstein Distance: {w_distance:.4f} | Jensen-Shannon Distance: {js_distance:.4f}")
plt.legend()
plt.show()
