import numpy as np

#x – a random choice from our Beta distribution
# B – our Beta function
# a – the first argument
# b – the second argument

conversionRates = [0.15, 0.04, 0.13, 0.11, 0.05]
N = 10000
d = len(conversionRates)
X = np.zeros((N,d))

for i in range(N):
    for j in range(d):
        if np.random.rand() < conversionRates[j]:
            X[i][j] = 1

nPosReward = np.zeros(d)
nNegReward = np.zeros(d)

for i in range(N):
    selected = 0
    maxRandom = 0
    for j in range(d):
            randomBeta = np.random.beta(nPosReward[j] + 1, nNegReward[j] + 1)
            if randomBeta > maxRandom:
                maxRandom = randomBeta
                selected = j
                print(f"Selected: {selected}, Random Beta: {randomBeta}")
    if X[i][selected] == 1:
        nPosReward[selected] += 1
    else:
        nNegReward[selected] += 1
print("Positive Rewards:", nPosReward)
print("Negative Rewards:", nNegReward)
print("Conversion Rates:", conversionRates)
