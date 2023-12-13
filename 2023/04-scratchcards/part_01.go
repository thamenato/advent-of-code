package main

import (
	"bufio"
	"fmt"
	"math"
	"regexp"
	"strings"

	"github.com/samber/lo"
)

var reNumbers = regexp.MustCompile(`\d+`)

func SolvePartOne(fileScanner *bufio.Scanner) {
	fmt.Println("Solve part One")

	totalPoints := 0
	for fileScanner.Scan() {
		line := fileScanner.Text()

		numbers := extractNumbers(line)
		intersection := lo.Intersect(numbers[0], numbers[1])

		matches := len(intersection)
		if matches > 0 {
			totalPoints += int(math.Pow(2, float64(matches-1)))
		}
	}

	fmt.Printf("total_points=%d\n", totalPoints)
}

func extractNumbers(line string) [][]string {
	text := strings.Split(strings.Split(line, ":")[1], "|")

	return [][]string{
		reNumbers.FindAllString(text[0], -1),
		reNumbers.FindAllString(text[1], -1),
	}
}
