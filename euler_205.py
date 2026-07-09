import itertools
from collections import Counter

# Model 1: 9 kast med en firesidet terning
# Model 2: 6 kast med en seks-sidet terning

udfaldsrum_model_1 = list(itertools.product([1, 2, 3, 4], repeat=9))
udfaldsrum_model_2 = list(itertools.product([1, 2, 3, 4, 5, 6], repeat=6))

sum_fordeling_model_1 = Counter(sum(udfald) for udfald in udfaldsrum_model_1)
sum_fordeling_model_2 = Counter(sum(udfald) for udfald in udfaldsrum_model_2)

vundne_kast_model_1 = 0
vundne_kast_model_2 = 0
uafgjorte_kast = 0

for sum_1, count_1 in sum_fordeling_model_1.items():
    for sum_2, count_2 in sum_fordeling_model_2.items():
        if sum_1 > sum_2:
            vundne_kast_model_1 += count_1 * count_2
        elif sum_2 > sum_1:
            vundne_kast_model_2 += count_1 * count_2
        else:
            uafgjorte_kast += count_1 * count_2

sandsynlighed_model_1 = vundne_kast_model_1 / ((4**9) * (6**6))
print(f"Sandsynligheden for at model 1 vinder over model 2: {sandsynlighed_model_1:.10f}")