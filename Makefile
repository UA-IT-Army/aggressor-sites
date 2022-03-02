all: clean all-in-one.json

clean:
	rm all-in-one.json || true

all-in-one.json:
	jq  '[inputs] | add' $(shell find ru by other -name \*.json) > $@