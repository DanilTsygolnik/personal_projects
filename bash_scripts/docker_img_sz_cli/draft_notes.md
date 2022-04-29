Команда[^source]:
```
docker manifest inspect -v <registry-domain>/<image-name> | \
grep size | \
awk -F ':' '{sum+=$NF} END {print sum}' | \
numfmt --to=iec-i
```

[^source]: https://www.codegrepper.com/code-examples/shell/docker+get+image+size+before+pull+acr

Работает только с пользовательскими образами -- `rancher/cowsay`. С официальными не срабатывает (`nginx`, например).

---

Построчный разбор кода:
- `docker manifest inspect -v <registry-domain>/<image-name>`
- `grep size`
- `awk -F ':' '{sum+=$NF} END {print sum}'`
- `numfmt --to=iec-i`
