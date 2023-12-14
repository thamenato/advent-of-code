package main

import (
	"fmt"
	"os"

	"github.com/apsdehal/go-logger"
	"github.com/thamenato/advent-of-code/libs/go/inputfilereader"
)

var log *logger.Logger

func main() {
	log, _ = logger.New("day05", 1, os.Stdout)
	log.SetLogLevel(logger.DebugLevel)

	if len(os.Args) <= 2 {
		fmt.Println("Missing argument: part_1, part_2")
		os.Exit(1)
	}
	filePath := os.Args[2]

	fileScanner, readFile := inputfilereader.GetLines("./files/" + filePath)

	if os.Args[1] == "part_1" {
		SolvePartOne(fileScanner)
	} else if os.Args[1] == "part_2" {
		SolvePartTwo(fileScanner)
	} else {
		fmt.Println("Wrong argument")
		os.Exit(1)
	}

	readFile.Close()
}
