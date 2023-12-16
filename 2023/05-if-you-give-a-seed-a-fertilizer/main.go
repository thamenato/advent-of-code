package main

import (
	"fmt"
	"os"

	"github.com/rs/zerolog"
	"github.com/rs/zerolog/log"
	"github.com/thamenato/advent-of-code/libs/go/inputfilereader"
)

func main() {
	log.Logger = log.Output(zerolog.ConsoleWriter{Out: os.Stderr})

	if len(os.Args) <= 1 {
		fmt.Println("Missing argument: part_1, part_2")
		os.Exit(1)
	}

	fileScanner, readFile := inputfilereader.GetLines("./files/sample")

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
