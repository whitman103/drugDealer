set terminal gif animate delay 2
set output 'test.gif'

set xrange[0:800]
set yrange[0:800]

do for [i=1:400] {
    plot 'imageBin//'.i.".txt"
}