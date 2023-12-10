package main

import (
	"strconv"
	"strings"
)

type Play struct {
	Cubes []Cube
}

type Cube struct {
	Number int
	Color  string
}

func ExtractPlays(text string) []Play {
	playsText := strings.Split(text, ";")
	plays := []Play{}

	for _, p := range playsText {
		cubesText := strings.Split(p, ",")

		play := Play{}
		for _, c := range cubesText {
			values := strings.Split(c, " ")

			n, _ := strconv.Atoi(values[1])
			color := values[2]

			s := Cube{Number: n, Color: color}
			play.Cubes = append(play.Cubes, s)
		}

		plays = append(plays, play)
	}
	return plays
}
