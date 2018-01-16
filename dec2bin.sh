read n
echo "Value is:"
fin=0
while [ $n -ge 1 ]
do
val=$((n%2))
fin=$(((fin*10)+$val))
n=$((n/2))	
done
echo "$fin"
