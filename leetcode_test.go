package main

import (
	"strconv"
	"testing"

	meddiff "github.com/ivanmatev/LeetCode/MedDiff"
)

func TestLengthOfLargestSubarrayWithKFrequency(t *testing.T) {
	tests := []struct {
		testID int
		nums   []int
		k      int
		ans    int
	}{
		{
			testID: 1,
			nums:   []int{1, 2, 3, 1, 2, 3, 1, 2},
			k:      2,
			ans:    6,
		},
		{
			testID: 2,
			nums:   []int{1, 2, 1, 2, 1, 2, 1, 2},
			k:      1,
			ans:    2,
		},
		{
			testID: 3,
			nums:   []int{5, 5, 5, 5, 5, 5, 5},
			k:      4,
			ans:    4,
		},
		{
			testID: 4,
			nums:   []int{1, 1000000000},
			k:      2,
			ans:    2,
		},
		{
			testID: 5,
			nums:   []int{2, 2, 3},
			k:      1,
			ans:    2,
		},
		{
			testID: 6,
			nums:   []int{1, 1, 1, 3},
			k:      2,
			ans:    3,
		},
	}

	for _, tc := range tests {
		t.Run(strconv.Itoa(tc.testID), func(t *testing.T) {
			testAns := meddiff.MaxSubarrayLength(tc.nums, tc.k)
			if testAns != tc.ans {
				t.Errorf("\nTestID: %v failed. Expected %v. Got %v.", tc.testID, tc.ans, testAns)
			}
		})
	}
}
