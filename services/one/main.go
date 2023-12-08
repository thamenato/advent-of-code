package main

import (
	"net/http"

	"github.com/labstack/echo/v4"
	"github.com/thamenato/advent-of-code/libs/hello"
)

func main() {
	e := echo.New()

	e.GET("/one/hello", func(c echo.Context) error {
		return c.String(http.StatusOK, hello.Greet("World"))
	})
	e.GET("/one/bye", func(c echo.Context) error {
		return c.String(http.StatusOK, hello.Goodbye("World"))
	})
	_ = e.Start(":8080")
}
