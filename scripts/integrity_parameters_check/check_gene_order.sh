#!/bin/bash

# check the selected gene order
if [[ $1 == 'ances' || $1 == 'vert' || $1 == 'panc' || $1 == 'albin' || $1 == 'hyal' || $1 == 'meta' ]]; then
	echo "The gene order selected is $1"
else
	echo "The gene order selected is $1."
    	# Read the file line by line
	while IFS= read -r line; do
		if ! [[ "$line" =~ ^(positive|negative): ]]; then
			echo "Error: gene order file passed does not fit the standard. Check how to build it in the manual or check the example in templates/go"
			exit 1
		else
			# Check if all items are present
			for item in nd1 nd2 nd3 nd4 ndl nd5 nd6 cox1 cox2 cox3 cob atp6 atp8; do
				if ! grep -q "$item" $1; then
				echo "Gene $item not found in the gene order."
				exit 1
				fi
			done
			echo "Gene order file structure is correct."
			mv $1 templates/go/
			exit 0
		fi
	done < "$1"

    	# If loop completes without finding the structure
	echo "Error: gene order file passed does not fit the standard. Check how to build it in the manual or check the example in templates/go"
	exit 1
fi

