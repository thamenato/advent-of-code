package main

import (
	"bufio"
	"fmt"

	"github.com/samber/lo"
	"golang.org/x/exp/maps"
)

func SolvePartTwo(fileScanner *bufio.Scanner) {
	fmt.Println("Solve part 2")

	cards := make(map[int]int)

	cardIdx := 1
	for fileScanner.Scan() {
		line := fileScanner.Text()
		cards[cardIdx] += 1

		numbers := extractNumbers(line)
		intersection := lo.Intersect(numbers[0], numbers[1])

		matches := len(intersection)

		for i := 1; i <= matches; i++ {
			cards[cardIdx+i] += 1 * cards[cardIdx]
		}

		cardIdx += 1
	}

	sum := lo.Sum(maps.Values(cards))
	fmt.Printf("sum=%d\n", sum)
}
