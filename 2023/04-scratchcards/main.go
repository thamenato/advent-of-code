package main

import (
	"fmt"
	"os"

	"github.com/thamenato/advent-of-code/libs/go/inputfilereader"
)

func main() {
	if len(os.Args) <= 1 {
		fmt.Println("Missing argument: part_1, part_2")
		os.Exit(1)
	}

	fileScanner, readFile := inputfilereader.GetLines("./files/input")

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
