package utilities

import (
	"encoding/csv"
	"fmt"
	"io"
	"io/ioutil"
	"os"
	"path"
	"path/filepath"
	"strings"

	"github.com/fatih/color"
	"github.com/jszwec/csvutil"
)

type Token struct {
	ID string `csv:"id"`
	Count int `csv:"counter"`
}

func UseToken(token string) {
	fmt.Println(token)
	ex, err := os.Executable()
	if err != nil {
		color.Red("Failed in os")
		return
	}
	ex = filepath.ToSlash(ex)
	csvPath := path.Join(path.Dir(ex) + "/input/" + "usage.csv")
	content, err := ioutil.ReadFile(csvPath)
	if err != nil {
		color.Red("Failed in read file")
		return
	}

	csvReader := csv.NewReader(strings.NewReader(string(content)))


	dec, err := csvutil.NewDecoder(csvReader)
	if err != nil {
		color.Red("Failed in read csv decode")
		return
	}

	var tokens []Token
	for {
		var t Token
		if err := dec.Decode(&t); err == io.EOF {
		break
		} else if err != nil {
			fmt.Printf("error")
		}
		tokens = append(tokens, t)
	}

	// fmt.Printf("%+v", tokens)

	found := false
	for i := 0; i < len(tokens); i++ {
		if (tokens[i].ID == token) {
			tokens[i].Count++
			found = true
		}
	}
	if (!found) {
		tokens = append(tokens, Token{ID: token, Count: 1})
	}

	// fmt.Printf("%+v", tokens)

	b, err := csvutil.Marshal(tokens)
	if err != nil {
		fmt.Println("error:", err)
	}
    
	// fmt.Printf("%s\n", b)
        
	err = ioutil.WriteFile(csvPath, b, 0644)
	if err !=  nil {
		fmt.Printf("Failed in saving csv")
		return
	}
}