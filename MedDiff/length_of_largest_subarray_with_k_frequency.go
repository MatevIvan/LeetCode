package meddiff

func MaxSubarrayLength(nums []int, k int) int {
	usedNumbers := make(map[int]int)
	lowerIndex := 0
	longestSubarray := 0

	// create expanding right-side window
	for upperIndex, num := range nums {
		// inc each new used num
		usedNumbers[num]++

		// close in the left-side window
		for usedNumbers[num] > k {
			usedNumbers[nums[lowerIndex]]--
			lowerIndex++
		}

		windowLength := upperIndex - lowerIndex + 1
		if windowLength > longestSubarray {
			longestSubarray = windowLength
		}
	}

	return longestSubarray
}
