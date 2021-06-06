# orologio del cazzo con le scritte	
# - print al centro
# - cerchio di 1 e 0
#        ____________________
#       |    10        01    |  
#       | 0      1  0      0 |
#       |1   04    :   20   1| 
#       | 0      1  0      0 |
#       |    01        10    |
#       |____________________|
#
#
#
#     
from colored import fg, bg, attr
import time
#172
x = 172
y = 9		
z = 10
print ('      '  + '%s____________________ %s' % (fg(x), attr(0)))	
print ('     %s|%s' % (fg(x), attr(0)) + '    %s10%s' % (fg(y), attr(0)) + '        %s01%s' % (fg(y), attr(0)) +   '    %s|%s' % (fg(x), attr(0)))
print ('     %s|%s' % (fg(x), attr(0)) + ' %s0%s' % (fg(y), attr(0)) + '      %s1%s' % (fg(y), attr(0)) + '  %s0%s' % (fg(y), attr(0)) + '      %s0%s' % (fg(y), attr(0)) + ' %s|%s' % (fg(x), attr(0)))

Orologio = '     %s1%s' % (fg(x), attr(0)) + '%s1%s' % (fg(y), attr(0)) + '   ' + '4 ' + '    %s:%s' % (fg(z), attr(0)) + '   ' + '2 ' + '   %s1%s' % (fg(y), attr(0)) + '%s|%s' % (fg(x), attr(0))
ore = Orologio[6]
print (Orologio)	

print ('     %s|%s' % (fg(x), attr(0)) + ' %s0%s' % (fg(y), attr(0)) + '      %s1%s' % (fg(y), attr(0)) + '  %s0%s' % (fg(y), attr(0)) + '      %s0%s' % (fg(y), attr(0)) + ' %s|%s' % (fg(x), attr(0)))
print ('     %s|%s' % (fg(x), attr(0)) + '    %s01%s' % (fg(y), attr(0)) + '        %s10%s' % (fg(y), attr(0)) +   '    %s|%s' % (fg(x), attr(0)))
print ('     '  + '%s|____________________| %s' % (fg(x), attr(0)))

time.sleep(1)
print(ore)







