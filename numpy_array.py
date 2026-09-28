import numpy as np

marks = np.array([78, 85, 92, 67, 88])

print("Original Array:", marks)
print("Data Type:", marks.dtype)

marks_float = marks.astype(float)

print("\nConverted Array:", marks_float)
print("Data Type:", marks_float.dtype)