#!/usr/bin/env bash

set -e

{
	cat <<- 'EOH'
		# This files shows the list of contributors to this repo
		
	EOH
	echo
	git log --format='%aN <%aE>' | LC_ALL=C.UTF-8 sort -uf
} > AUTHORS
