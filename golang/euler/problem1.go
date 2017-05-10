package main

// IsMult returns true if n is divisible by both 3 and 5
// otherwise it return false tits
func IsMult(n int) bool {

	if (n%3 == 0) || (n%5 == 0) {
		return true
	}
	return false
}

// SolveProblem1 of euler challenge
func SolveProblem1(n int) int {
	sum := 0
	for i := 0; i < n; i++ {
		if IsMult(i) {
			sum += i
		}
	}
	return sum
}
