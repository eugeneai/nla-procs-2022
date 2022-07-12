
for file in *.tex;
do
    echo $file
    sed -i 's/\r//' $file
done
