echo "Enter the maximum number of elements"
read n

echo "Enter numbers in array:"
for((i = 0; i < $n; i++))
	do
		read nos[$i]
	done

echo "The numbers in array are:"
for((i = 0; i < $n; i++))
	do
		echo ${nos[$i]}
	done
# Now do the Sorting of numbers
for (( i = 0; i < $n ; i++ ))
	do
		for (( j = $i; j < $n; j++ ))
			do
				if [ ${nos[$i]} -gt ${nos[$j]}  ]; then
					t=${nos[$i]}
					nos[$i]=${nos[$j]}
					nos[$j]=$t
				fi
			done
	done
# Printing the sorted number
echo -e "\nSorted Numbers "
for (( i=0; i < $n; i++ ))
do
echo ${nos[$i]}
done