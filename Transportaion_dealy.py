import numpy as np
import matplotlib.pyplot as plt


#  DATASET (30 DAYS)


days = np.arange(1, 31)

routeA = np.array([
    52, 55, 57, 50, 63, 49, 46, 58, 62, 59,
    51, 54, 48, 65, 70, 53, 56, 49, 47, 52,
    60, 58, 62, 75, 68, 50, 49, 54, 61, 57
])

routeB = np.array([
    48, 50, 49, 46, 60, 44, 42, 52, 55, 53,
    47, 50, 45, 58, 63, 48, 51, 45, 44, 47,
    55, 53, 56, 66, 60, 45, 44, 49, 52, 50
])

toll_delay = np.array([
    4, 5, 3, 2, 6, 2, 3, 5, 4, 5,
    3, 4, 2, 6, 7, 4, 5, 3, 2, 3,
    5, 4, 6, 8, 7, 3, 2, 4, 5, 4
])

railway_delay = np.array([
    6, 7, 5, 4, 10, 3, 2, 8, 9, 8,
    5, 6, 3, 11, 13, 4, 6, 3, 2, 4,
    9, 8, 10, 15, 12, 4, 3, 5, 7, 6
])

morning_delay = np.array([
    8, 10, 9, 7, 12, 6, 5, 11, 13, 12,
    8, 9, 7, 14, 16, 9, 10, 7, 6, 8,
    12, 11, 13, 17, 15, 7, 6, 9, 11, 10
])

evening_delay = np.array([
    10, 12, 11, 9, 15, 8, 7, 13, 16, 14,
    9, 11, 8, 16, 18, 11, 12, 8, 7, 9,
    14, 13, 15, 20, 17, 8, 7, 10, 12, 11
])


#  1. ROUTE A vs ROUTE B LINE PLOT

plt.figure(figsize=(10, 5))
plt.plot(days, routeA, marker='o', label="Route A")
plt.plot(days, routeB, marker='s', label="Route B")
plt.title("Route A vs Route B Travel Time (30 Days)")
plt.xlabel("Days")
plt.ylabel("Travel Time (min)")
plt.legend()
plt.grid(True)
plt.show()
plt.close()



#  2. TOLL DELAY BAR CHART


plt.figure(figsize=(10, 5))
plt.bar(days, toll_delay)
plt.title("Toll Delay Over 30 Days")
plt.xlabel("Days")
plt.ylabel("Delay (min)")
plt.grid(True)
plt.show()
plt.close()



#  3. RAILWAY DELAY SCATTER PLOT


plt.figure(figsize=(10, 5))
plt.scatter(railway_delay, routeA)
plt.title("Railway Delay vs Route A Travel Time")
plt.xlabel("Railway Delay (min)")
plt.ylabel("Route A Travel Time (min)")
plt.grid(True)
plt.show()
plt.close()



#  4. MORNING vs EVENING DELAY


plt.figure(figsize=(10, 5))
plt.plot(days, morning_delay, marker='o', label="Morning Delay")
plt.plot(days, evening_delay, marker='*', label="Evening Delay")
plt.title("Morning vs Evening Peak Delay (30 Days)")
plt.xlabel("Days")
plt.ylabel("Delay (min)")
plt.legend()
plt.grid(True)
plt.show()
plt.close()



#  5. BASIC NUMPY ANALYSIS


print("=== NUMPY ANALYSIS RESULTS ===")

print("Average Route A Time:", np.mean(routeA))
print("Average Route B Time:", np.mean(routeB))

print("Max Route A Delay:", np.max(routeA))
print("Day of Max Route A Delay:", np.argmax(routeA) + 1)

print("Correlation (Railway Delay ↔ Route A):")
print(np.corrcoef(railway_delay, routeA))

# Linear prediction for next day
coef = np.polyfit(days, routeA, 1)
next_day_prediction = np.polyval(coef, 31)
print("Predicted Route A Time for Day 31:", next_day_prediction)

print("Days with Route A > 60 min:", routeA[routeA > 60])