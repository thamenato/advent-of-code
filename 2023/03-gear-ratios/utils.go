package main

import (
	"regexp"
	"strconv"
)

var (
	reSymbol = regexp.MustCompile(`[^a-zA-Z0-9_.]`)
	reNumber = regexp.MustCompile(`\d+`)
)

func isSymbol(value string) bool {
	return reSymbol.MatchString(value)
}

func lineNumbersLookup(gear []int, line string) []int {
	lineLength := len(line)
	validNumbers := []int{}
	matches := reNumber.FindAllStringIndex(line, -1)

	for _, number := range matches {
		leftIndex := minIndex(number[0])
		rightIndex := maxIndex(number[1], lineLength)

		if gear[0] >= leftIndex && gear[0] < rightIndex {
			numInt, _ := strconv.Atoi(line[number[0]:number[1]])
			validNumbers = append(validNumbers, numInt)
		}
	}

	return validNumbers
}

func sameLineSymbolLookup(number []int, line string) bool {
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

func otherLineSymbolLookup(number []int, line string) bool {
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
