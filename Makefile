all: all-in-one.json

all-in-one.json:
	jq  '[inputs] | add' $(shell find ru by other -name \*.json) > $@