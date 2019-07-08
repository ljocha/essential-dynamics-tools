#!/bin/bash

# XXX: funguje jen s relativnimi cestami


usage()
{
	echo usage: $0 -o outfile [-l list_of_files] [infiles ...] >&2
	exit 1
}

while getopts "o:l:" opt; do
	case $opt in
		o)
			out=$OPTARG
			;;
		l)
			list=$OPTARG
			;;
		\?)
			usage
			;;
	esac
done

shift $(($OPTIND -1))

[ -z "$out" ] && usage
[ -z "$list" -a -z "$1" ] && usage
[ -n "$list" -a -n "$1" ] && usage

if [ -z "$list" ]; then
	cat "$@" >$out.pdb || { echo $out.pdb: $! >&2; exit 1; }
else
	[ -f "$list" ] || { echo $list: No such file >&2; exit 1; }
	>$out.pdb
	while read f; do
		cat $f >>$out.pdb || { echo $out.pdb: $! >&2; exit 1; }
	done <$list
fi

dir=$(dirname $out)
cd $dir || { echo $dir: $! >&2; exit 1; }

gmx="docker run -u $(id -u):$(id -g) -v $PWD:/work -w /work ljocha/gromacs:2019.4.30-1 gmx"

$gmx trjconv -f $(basename $out.pdb) -o $(basename $out)

ret=$?

rm $out.pdb

exit $ret
