package main

import (
	"bufio"
	"fmt"
)

const (
	RED   string = "red"
	GREEN string = "green"
	BLUE  string = "blue"
)

func SumPowerSetGames(fileScanner *bufio.Scanner) {
	var sum int

	for fileScanner.Scan() {
		line := fileScanner.Text()

		i, gameText := extractGameNumber(line)

		plays := ExtractPlays(gameText)

		cubes := getViableCubeNumber(plays)

		power := 1
		for _, c := range cubes {
			power *= c.Number
		}
		fmt.Printf("i=%d, power=%d\n", i, power)

		sum += power
	}

	fmt.Println("sum=", sum)
}

func getViableCubeNumber(plays []Play) map[string]*Cube {
	cubes := map[string]*Cube{
		RED:   {Color: RED, Number: 1},
		GREEN: {Color: GREEN, Number: 1},
		BLUE:  {Color: BLUE, Number: 1},
	}

	for _, p := range plays {
		for _, c := range p.Cubes {
			switch color := c.Color; color {
			case RED:
				if c.Number > cubes[RED].Number {
					cubes[RED].Number = c.Number
				}
			case GREEN:
				if c.Number > cubes[GREEN].Number {
					cubes[GREEN].Number = c.Number
				}
			case BLUE:
				if c.Number > cubes[BLUE].Number {
					cubes[BLUE].Number = c.Number
				}
			}
		}
	}

	return cubes
}
