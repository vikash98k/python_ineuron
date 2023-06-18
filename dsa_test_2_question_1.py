def sqrt_root(n):
	if n < 2:
		return n
	low, high = 1, n
	while low <= high:
		mid = (low + high) // 2
		if mid * mid == n:
			return mid
		elif mid * mid < n:
			low = mid + 1
		else:
			high = mid - 1
	return high


n=8
print(sqrt_root(n))
