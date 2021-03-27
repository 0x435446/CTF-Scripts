#!/bin/bash

archive=`file $1|grep -o "compressed\|archive"`

file1=flag

while [[ $archive == "compressed" || $archive == "archive" ]];
do

ext=`file $file1|cut -d" " -f 2`

ext=`echo $ext | tr '[:upper:]' '[:lower:]'`

if [ $ext == "gzip" ]
then
	ext="gz"
fi

file=$file1.$ext

mv $file1 $file1.$ext

echo $file
echo $file1

if [ $ext == "lzma" ]
then
	unlzma $file
elif [ $ext == "gz" ]
then
	gzip -d $file
elif [ $ext == "bzip2" ]
then
	bzip2 -d $file
	mv "$file.out" $file1
elif [ $ext == "xz" ]
then
	unxz $file
	mv "$file1.xz" $file1
elif [ $ext == "zip" ]
then
	unzip $file
	mv "$file1.gz" $file1
	rm $file1.zip
fi
done

