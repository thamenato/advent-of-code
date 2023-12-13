package main

import (
	"bufio"
	"fmt"
	"strconv"
)

func SolvePartOne(fileScanner *bufio.Scanner) {
	matrix := [3]string{}
	var matches [][]int
	sum := 0

	fileScanner.Scan()
	matrix[0] = fileScanner.Text()
	fileScanner.Scan()
	matrix[1] = fileScanner.Text()

	matches = reNumber.FindAllStringIndex(matrix[0], -1)
	for _, number := range matches {
		numberInt, _ := strconv.Atoi(matrix[0][number[0]:number[1]])
		if sameLineSymbolLookup(number, matrix[0]) || otherLineSymbolLookup(number, matrix[1]) {
			sum += numberInt
		}
	}

	for fileScanner.Scan() {
		matrix[2] = fileScanner.Text()

		matches = reNumber.FindAllStringIndex(matrix[1], -1)

		for _, number := range matches {
			numberInt, _ := strconv.Atoi(matrix[1][number[0]:number[1]])
			if sameLineSymbolLookup(number, matrix[1]) || otherLineSymbolLookup(number, matrix[0]) || otherLineSymbolLookup(number, matrix[2]) {
				sum += numberInt
			}
		}

		// do some moves
		matrix[0] = matrix[1]
		matrix[1] = matrix[2]
	}

	matches = reNumber.FindAllStringIndex(matrix[1], -1)
	for _, number := range matches {
		numberInt, _ := strconv.Atoi(matrix[1][number[0]:number[1]])
		if sameLineSymbolLookup(number, matrix[1]) || otherLineSymbolLookup(number, matrix[0]) {
			sum += numberInt
		}
	}

	fmt.Printf("sum=%d\n", sum)
}
