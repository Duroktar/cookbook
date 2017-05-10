package main

// Sum ...
func Sum(nums []int) int {
	rv := 0
	for _, num := range nums {
		rv += num
	}
	return rv
}

// IsEven ...
func IsEven(n int) bool {
	if n != 0 && n%2 == 0 {
		return true
	}
	return false
}

// Fibonacci ...
func Fibonacci() chan int {
	c := make(chan int)
	go func() {
		a, b := 0, 1
		for {
			a, b = b, a+b
			c <- a
		}
	}()
	return c
}

// SolveProblem2 ...
func SolveProblem2(n int) int {
	var accum []int
	for num := range Fibonacci() {
		if num > 4000000 {
			break
		} else {
			if IsEven(num) {
				accum = append(accum, num)
			}
		}

	}
	return Sum(accum)
}
