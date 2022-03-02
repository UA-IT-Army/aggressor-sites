all: clean all-in-one.json 

cf: clean all-in-one-cf.json 

clean:
	rm all-in-one.json || true

all-in-one-cf.json: all-in-one.json
	scripts/is_cloudflare.sh $< > $@

all-in-one.json:
	jq -s 'add' $(shell find ru by other -name \*.json) > $@