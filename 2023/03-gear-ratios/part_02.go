package main

import (
	"bufio"
	"fmt"
	"regexp"
)

var (
	reGear = regexp.MustCompile(`[*]`)
)

func SolvePartTwo(fileScanner *bufio.Scanner) {
	matrix := [3]string{}
	var matches [][]int
	sum := 0

	fileScanner.Scan()
	matrix[0] = fileScanner.Text()
	fileScanner.Scan()
	matrix[1] = fileScanner.Text()

	matches = reGear.FindAllStringIndex(matrix[0], -1)
	fmt.Printf("gear=%v\n\n", matches)
	for _, gear := range matches {
		totalNumbers := lineNumbersLookup(gear, matrix[0])
		totalNumbers = append(totalNumbers, lineNumbersLookup(gear, matrix[1])...)

		if len(totalNumbers) == 2 {
			sum += totalNumbers[0] * totalNumbers[1]
		}
	}

	for fileScanner.Scan() {
		matrix[2] = fileScanner.Text()

		matches = reGear.FindAllStringIndex(matrix[1], -1)

		for _, gear := range matches {
			totalNumbers := lineNumbersLookup(gear, matrix[0])
			totalNumbers = append(totalNumbers, lineNumbersLookup(gear, matrix[1])...)
			totalNumbers = append(totalNumbers, lineNumbersLookup(gear, matrix[2])...)

			if len(totalNumbers) == 2 {
				sum += totalNumbers[0] * totalNumbers[1]
			}
		}

		// do some moves
		matrix[0] = matrix[1]
		matrix[1] = matrix[2]
	}

	matches = reGear.FindAllStringIndex(matrix[1], -1)
	for _, gear := range matches {
		totalNumbers := lineNumbersLookup(gear, matrix[1])
		totalNumbers = append(totalNumbers, lineNumbersLookup(gear, matrix[2])...)

		if len(totalNumbers) == 2 {
			sum += totalNumbers[0] * totalNumbers[1]
		}
	}

	fmt.Printf("sum=%d\n", sum)
}
