package main

import (
	"bufio"
	"fmt"
	"regexp"
	"strconv"
)

const (
	RED_MAX   int = 12
	GREEN_MAX int = 13
	BLUE_MAX  int = 14
)

func SumValidGames(fileScanner *bufio.Scanner) {
	var sumValidGames int

	for fileScanner.Scan() {
		line := fileScanner.Text()

		gameNumber, gameText := extractGameNumber(line)

		plays := ExtractPlays(gameText)

		ok := isValidPlay(plays)

		if !ok {
			continue
		}

		sumValidGames += gameNumber
	}

	fmt.Println("sum=", sumValidGames)
}

func extractGameNumber(text string) (int, string) {
	r := regexp.MustCompile(`Game\W(?P<game>\d+):`)

	res := r.FindStringSubmatch(text)

	val, err := strconv.Atoi(res[1])

	if err != nil {
		fmt.Println(err)
	}

	newText := r.ReplaceAllString(text, "")

	return val, newText
}

func isValidPlay(plays []Play) bool {
	for _, p := range plays {
		for _, c := range p.Cubes {
			switch color := c.Color; color {
			case "red":
				if c.Number > RED_MAX {
					return false
				}
			case "green":
				if c.Number > GREEN_MAX {
					return false
				}
			case "blue":
				if c.Number > BLUE_MAX {
					return false
				}
			}
		}
	}
	return true
}
