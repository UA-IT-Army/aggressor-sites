# Sample use

```shell
for url in $(jq -r '.[]' russia.json)
do
  echo "Contact $url"
done
```
