# Sites

sites are split by region where possible:

* `ru`
* `by`
* `other`

Also compiled into a single file:

`all-in-one.json`

# Sample use

```shell
for url in $(curl -s https://raw.githubusercontent.com/UA-IT-Army/agressor-sites/main/russia.json | jq -r '.[]' )
do 
  echo "contact $url"
done
```
