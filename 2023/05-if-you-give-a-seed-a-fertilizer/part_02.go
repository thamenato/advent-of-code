package main

import (
	"bufio"
	"sort"

	"github.com/rs/zerolog/log"
)

type NumberRange struct {
	MIN    int `json:"min"`
	MAX    int `json:"max"`
	OFFSET int `json:"offset"`
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

	fileScanner.Scan() // go over first empty line
	var conversion []NumberRange

FILE_LOOP:
	for fileScanner.Scan() {
		line := fileScanner.Text()

		if len(line) == 0 {
			log.Debug().Msg("Empty line")

			sort.Slice(conversion, func(i, j int) bool {
				return conversion[i].MIN < conversion[j].MIN
			})
			log.Debug().Interface("conversion", conversion).Send()

			var nextRanges []NumberRange

			i := 0
			for _, r := range currRanges {
				log.Debug().Interface("r", r).Send()
				if r.MIN < conversion[i].MIN {
					log.Debug().Interface("r", r).Send()
					// if r.MAX < conversion[i].MIN {
					// 	nr := NumberRange{MIN: r.MIN, MAX: r.MAX}
					// 	nextRanges = append(nextRanges, nr)
					// } else {
					// 	nr := NumberRange{MIN: r.MIN, MAX: conversion[i].MIN - r.MAX}
					// 	nextRanges = append(nextRanges, nr)

					// 	r.MIN = conversion[i].MIN
					// }
				}
			}

			log.Debug().Interface("nextRanges", nextRanges).Send()
			continue FILE_LOOP
		}

		if reMap.MatchString(line) {
			// empty ranges
			conversion = []NumberRange{}

			match := reMap.FindStringSubmatch(line)
			mapName := match[reMap.SubexpIndex("map")]
			log.Info().Str("mapName", mapName).Msg("Found header")
		} else {
			numbers := getNumbers(line)
			numberRange := getNumberRange(numbers[1], numbers[2])
			numberRange.OFFSET = numbers[0] - numbers[1]
			conversion = append(conversion, numberRange)
		}
	}

}

func getNumberRange(first int, second int) NumberRange {
	return NumberRange{
		MIN: first,
		MAX: first + second - 1,
	}
}
