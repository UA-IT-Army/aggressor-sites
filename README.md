# Sample use

```shell
for url in $(curl -s https://raw.githubusercontent.com/droopy4096/agressor-sites/main/russia.json | jq -r '.[]' )
do 
  echo "contact $url"
done
```
