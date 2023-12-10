package inputfilereader

import (
	"bufio"
	"fmt"
	"os"
)

func GetLines(filepath string) (*bufio.Scanner, *os.File) {
	readFile, err := os.Open(filepath)

	if err != nil {
		fmt.Println(err)
	}
	fileScanner := bufio.NewScanner(readFile)

	fileScanner.Split(bufio.ScanLines)

	return fileScanner, readFile
}
