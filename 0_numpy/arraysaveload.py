import numpy as np
arr = np.arange(10)
print arr
# Save single arrays on file with default extension .npy
np.save('saved_array',arr)
# Load single array from file with default extension .npy
single_array = np.load('saved_array.npy')
print single_array
# ----------------
arr1 = np.arange(25)
arr2 = np.arange(35)

# Save multiple arrays to file with default extension .npz
np.savez('file_arrays', x1 = arr1, y1 = arr2)
np.savez_compressed('filearr_comp',x2 = arr1, y2 = arr2)

# Load multiple arrays from file with default extension .npz
ld_filearr = np.load('file_arrays.npz')
ld_filearrcomp = np.load('filearr_comp.npz')

print ld_filearr.items()
print
print ld_filearr['x1']
print ld_filearr['y1']
print
print
print ld_filearrcomp.items()
print
print ld_filearrcomp['x2']
print ld_filearrcomp['y2']
# ----------------------
# Save array to text file
np.savetxt('txtarray', arr1, delimiter=',')

# Load array from text file
txt_arr = np.loadtxt('txtarray', delimiter=',')

print txt_arr.dtype
print txt_arr