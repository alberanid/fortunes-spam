all:
	@which strfile || (echo -e "\nERROR: strfile command is missing: you need to install the fortune-mod package\n" ; exit 1)
	strfile -c spam-o spam-o.dat
	strfile -c spam-ita-o spam-ita-o.dat
