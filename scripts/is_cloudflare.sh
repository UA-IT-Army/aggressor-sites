#!/bin/bash

for s in $(jq -r '. | keys[]' ${1}) 
do 
    no_proto=${s#*://}
    domain=${no_proto%%/*}
    dig ${domain} NS +short | grep -q cloudflare && echo ${domain}
done | jq -R -s '[split("\n")[] | select( . != "")] | map({ key: ., value: {}}) | from_entries'