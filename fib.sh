read n
f1=0
f2=1
echo "The Fibonacci sequence for the number $Num is : "
for (( i=0;i<=n;i++ ))
do
     fn=$((f1+f2))	
     f1=$f2
     f2=$fn
     echo -n "$fn "
done
