package hello

import (
	"fmt"
)

func Greet(audience string) string {
	return fmt.Sprintf("Hello, %s!", audience)
}

func Goodbye(audience string) string {
	return fmt.Sprintf("Bye, %s!", audience)
}
