package main

import (
	"bufio"

	"github.com/rs/zerolog/log"
)

type NumberRange struct {
	MIN int `json:"min"`
	MAX int `json:"max"`
}

func SolvePartTwo(fileScanner *bufio.Scanner) {
	log.Info().Msg("Solve Part 2")

	fileScanner.Scan()

	numbers := getNumbers(fileScanner.Text())

	var currRanges []NumberRange

	for i := 0; i < len(numbers); i += 2 {
		currRanges = append(currRanges, getNumberRange(numbers[i], numbers[i+1]))
	}

	log.Debug().Interface("currRanges", currRanges).Send()

	var srcRange []NumberRange
	var dstRange []NumberRange

FILE_LOOP:
	for fileScanner.Scan() {
		line := fileScanner.Text()

		if len(line) == 0 {
			log.Debug().Msg("Empty line")
			continue FILE_LOOP
		}

		if reMap.MatchString(line) {
			log.Debug().Interface("srcRange", srcRange).Send()
			log.Debug().Interface("dstRange", dstRange).Send()

			var tmpRanges []NumberRange

			for _, curr := range currRanges {
				for _, src := range srcRange {
					if src.MIN <= curr.MIN && src.MAX >= curr.MAX {
						// inside of range
					} else if src.MIN <= curr.MIN && src.MAX < curr.MAX {
						// inside min, outside max
					} else if src.MIN > curr.MIN && src.MAX >= curr.MAX {
						// outside min, inside max
					} else {
						// outside min, outside max
					}

				}

			}

			// empty ranges
			srcRange = []NumberRange{}
			dstRange = []NumberRange{}

			match := reMap.FindStringSubmatch(line)
			mapName := match[reMap.SubexpIndex("map")]
			log.Info().Str("mapName", mapName).Msg("Found header")

			// to the thing
		} else {
			numbers := getNumbers(line)

			srcRange = append(srcRange, getNumberRange(numbers[1], numbers[2]))
			dstRange = append(dstRange, getNumberRange(numbers[0], numbers[2]))
		}
	}

}

func getNumberRange(first int, second int) NumberRange {
	return NumberRange{
		MIN: first,
		MAX: first + second - 1,
	}
}
