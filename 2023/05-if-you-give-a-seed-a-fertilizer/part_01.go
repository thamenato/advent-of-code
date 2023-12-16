package main

import (
	"bufio"
	"regexp"
	"strconv"

	"github.com/rs/zerolog/log"
	"github.com/samber/lo"
	"golang.org/x/exp/maps"
)

var (
	reNumbers = regexp.MustCompile(`\d+`)
	reMap     = regexp.MustCompile(`to-(?P<map>\w+) map`)
)

func SolvePartOne(fileScanner *bufio.Scanner) {
	log.Info().Msg("Solve Part 01")

	lookupMap := make(map[string]map[int]bool)
	tableName := "seeds"

	// get first line
	fileScanner.Scan()
	lookupMap[tableName] = make(map[int]bool)

	for _, s := range getNumbers(fileScanner.Text()) {
		lookupMap[tableName][s] = false
	}

	log.Debug().Msgf("%s=%v", tableName, lookupMap[tableName])

	// drop empty line
	fileScanner.Scan()

	log.Debug().Msgf("lookupMap=%v", lookupMap)
	mapName := ""
	// start scanning map information
OUTER:
	for fileScanner.Scan() {
		line := fileScanner.Text()

		if len(line) == 0 {
			log.Debug().Msgf("found empty line")
			for k, v := range lookupMap[tableName] {
				if !v {
					lookupMap[mapName][k] = false
				}
			}

			tableName = mapName
			mapName = ""

			log.Debug().Msgf("tableName=%s, mapName=%s", tableName, mapName)
			continue OUTER
		}

		if reMap.MatchString(line) {
			match := reMap.FindStringSubmatch(line)
			mapName = match[reMap.SubexpIndex("map")]
			lookupMap[mapName] = make(map[int]bool)
			log.Debug().Msgf("found map=%s", mapName)
		} else {
			numbers := getNumbers(line)
			markTrue := []int{}
			for k, v := range lookupMap[tableName] {
				if !v {
					src := numbers[1]
					dst := numbers[0]
					rangeLength := numbers[2]

					if k >= src && k < src+rangeLength {
						offset := k - src
						markTrue = append(markTrue, k)
						lookupMap[mapName][dst+offset] = false
					}
				}
			}
			log.Debug().Msgf("mark_true=%v", markTrue)
			for _, k := range markTrue {
				lookupMap[tableName][k] = true
			}
			log.Debug().Msgf("%s=%v", tableName, lookupMap[tableName])
		}
	}

	log.Debug().Msgf("lookupMap=%v", lookupMap)

	log.Debug().Msgf("lowest location = %d", lo.Min(maps.Keys(lookupMap["location"])))
}

func getNumbers(line string) []int {
	var numbers []int
	for _, s := range reNumbers.FindAllString(line, -1) {
		n, _ := strconv.Atoi(s)
		numbers = append(numbers, n)
	}
	return numbers
}
