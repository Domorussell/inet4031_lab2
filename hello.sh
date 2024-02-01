#!/bin/bash

a=2
b=2
c=$((a + b))

echo "Bash says: Hello, World!"
echo "$a + $b = $c"

ListOfUsers=(User1 User2 User3)

for i in "${ListOfUsers[@]}"
do
	echo $i
done
