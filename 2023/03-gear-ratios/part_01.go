package main

import (
	"bufio"
	"fmt"
	"regexp"
	"strconv"
)

var (
	reSymbol = regexp.MustCompile(`[^a-zA-Z0-9_.]`)
	reNumber = regexp.MustCompile(`\d+`)
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
		if checkLine(number, matrix[0]) || checkOtherLine(number, matrix[1]) {
			sum += numberInt
		}
	}

	for fileScanner.Scan() {
		matrix[2] = fileScanner.Text()

		matches = reNumber.FindAllStringIndex(matrix[1], -1)

		for _, number := range matches {
			numberInt, _ := strconv.Atoi(matrix[1][number[0]:number[1]])
			if checkLine(number, matrix[1]) || checkOtherLine(number, matrix[0]) || checkOtherLine(number, matrix[2]) {
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
		if checkLine(number, matrix[1]) || checkOtherLine(number, matrix[0]) {
			sum += numberInt
		}
	}

	fmt.Printf("sum=%d\n", sum)
}

func isSymbol(value string) bool {
	return reSymbol.MatchString(value)
}

func checkLine(number []int, line string) bool {
	lineLength := len(line)
	// leftmost
	if number[0] == 0 {
		if isSymbol(string(line[number[1]])) {
			return true
		} else if reSymbol.MatchString(line[number[0] : number[1]+1]) {
			return true
		}
	} else
	// rightmost
	if number[1] == lineLength {
		if isSymbol(string(line[number[0]-1])) {
			return true
		}
	} else {
		if isSymbol(string(line[number[0]-1])) {
			return true
		} else if isSymbol(string(line[number[1]])) {
			return true
		}
	}
	return false
}

func checkOtherLine(number []int, line string) bool {
	lineLength := len(line)
	leftIndex := minIndex(number[0])
	rightIndex := maxIndex(number[1], lineLength)

	return isSymbol(line[leftIndex:rightIndex])
}

func minIndex(number int) int {
	if number == 0 {
		return 0
	}
	return number - 1
}

func maxIndex(number int, max int) int {
	if number == max {
		return max
	}
	return number + 1
}
