package meddiff

func IntergerBreak(n int) int {
	// special cases for num <= 3
	if n <= 3 {
		return n - 1
	}

	product := 1

	// 3's are the magic num
	for n > 4 {
		product *= 3
		n -= 3
	}

	// mult by the left over
	return product * n
}
