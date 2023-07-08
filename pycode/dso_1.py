import matplotlib.pyplot as plt
from ds1054z import DS1054Z
scope = DS1054Z('169.254.7.218')
print(scope.idn)
a =(scope.get_waveform_samples(1, mode='MAX'))
print(type(a[1]))
plt.plot(a)
plt.show()

#print("offset", scope.get_channel_offset(1))
#print("channel scale", scope.get_channel_scale(1))
#print("probe ratio", scope.get_probe_ratio(1))
#print("waveform bytes", scope.get_waveform_bytes(1, mode='RAW'))
