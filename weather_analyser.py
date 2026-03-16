import numpy as np

temperature = np.array([32, 34, 36, 38, 41,39, 37, 35, 33, 30,29, 31, 34, 36, 40,42, 44, 43, 39, 37,35, 33, 32, 31, 30,34, 36, 38, 41, 45])

avg=np.mean(temperature)
hot=np.argmax(temperature)+1
cold=np.argmin(temperature)+1
temp_less_avg=np.where(temperature<avg)[0]+1
temp_high_avg=np.where(temperature>avg)[0]+1
heat_wave=np.where(temperature>40)[0]+1

print(f"Average temperature of the month is {avg:.2f}°C")
print(f"Hottest day of the month is {hot} with {temperature[hot-1]}°C")
print(f"Coldest day of the month is {cold} with {temperature[cold-1]}°C")
print(f"Days when the temperature is below the average temperature of the month is {temp_less_avg}")
print(f"Days when the temperature is above the average temperature of the month is {temp_high_avg}")
print(f"Days when heat wave occurs (temperature > 40°C) -> {heat_wave}")
