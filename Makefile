all:
	@which strfile || (echo -e "\nERROR: strfile command is missing: you need to install the fortune-mod package\n" ; exit 1)
	strfile -x -r spam-o spam-o.dat
	strfile -x -r spam-ita-o spam-ita-o.dat
