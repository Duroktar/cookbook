package main

import (
	"math"
)

func isPrime(n int) bool {
	if n < 5 {
		return false
	}
	for i := 2; i <= int(math.Sqrt(float64(n))); i++ {
		if n%i == 0 {
			return false
		}
	}
	return true
}

func factors(n int) []int {
	var accum []int
	for i := 1; i <= int(math.Sqrt(float64(n))); i++ {
		if n%i == 0 {
			accum = append(accum, i)
		}
	}
	return accum
}

// SolveProblem3 ...
func SolveProblem3(n int) int {
	var accum []int
	data := factors(n)
	for _, value := range data {
		if isPrime(value) {
			accum = append(accum, value)
		}
	}
	return accum[len(accum)-1]
}
