
package main

import (
	"fmt"
	"net/http"
)

func helloHandler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintln(w, "Hello World from Go in minimal Docker container")
	fmt.Println("Got request: server page")
}

func main() {
	http.HandleFunc("/", helloHandler)

	fmt.Println("Started, serving at 8000")
	err := http.ListenAndServe(":8000", nil)
	if err != nil {
		panic("ListenAndServe: " + err.Error())
	}
}

