from natsort import natsorted

versions = ['v2.1', 'v1.1', 'v1.2', 'v1.10']

print(sorted(versions))  # ['v1.1', 'v1.10', 'v1.2', 'v2.1']
print(natsorted(versions))  # ['v1.1', 'v1.2', 'v1.10', 'v2.1']
