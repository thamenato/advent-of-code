package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
	"unicode"
)

func main() {
	readFile, err := os.Open("./files/input")

	if err != nil {
		fmt.Println(err)
	}
	fileScanner := bufio.NewScanner(readFile)

	fileScanner.Split(bufio.ScanLines)

	sum := 0
	for fileScanner.Scan() {
		line := fileScanner.Text()

		first := findNumber(line, false)
		last := findNumber(line, true)

		value, err := strconv.Atoi(first + last)

		if err != nil {
			fmt.Printf("line: %s, err=%s\n", line, err)
		} else {
			sum += value
			fmt.Printf("line: %s, first: %s, last: %s\n", line, first, last)
		}
	}

	fmt.Printf("Sum of all calibration numbers = %d\n", sum)

	readFile.Close()
}

func findNumber(text string, reverse bool) string {
	var subString string

	if !reverse {
		for _, char := range text {
			if unicode.IsDigit(char) {
				return string(char)
			} else {
				subString += string(char)
				num, ok := numberFromSubstring(subString)
				if ok {
					return string(num)
				}
			}
		}
	} else {
		runes := []rune(text)
		for i := len(runes) - 1; i >= 0; i-- {
			char := runes[i]
			if unicode.IsDigit(char) {
				return string(char)
			} else {
				subString = string(char) + subString
				num, ok := numberFromSubstring(subString)
				if ok {
					return string(num)
				}
			}
		}
	}

	return ""
}

func numberFromSubstring(text string) (string, bool) {
	words := []string{"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"}
	numbers := []string{"1", "2", "3", "4", "5", "6", "7", "8", "9"}

	for i, w := range words {
		if strings.Contains(text, w) {
			return numbers[i], true
		}
	}

	return "", false
}
