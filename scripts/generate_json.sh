#!/bin/sh -e
set -u

d=$(dirname $0)
for script in creators gocomics drunkduck universal keenspot smackjeeves arcamax; do
  echo "Executing ${script}.py"
  "${d}/${script}.py"
done
