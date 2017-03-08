# -*- coding: UTF-8 -*-
print "Hello, Python!";

name="jack";
home="jack";

Money = 2000
def AddMoney():
   # 想改正代码就取消以下注释:
   global Money
   Money = Money + 1
 
print Money
AddMoney()
print Money

if(name is "jack"):
	print "xiang deng de";
	print "second"
else:
	print "no"

total1=100; #quan ju bian liang
num=raw_input("Enter a number!\n");
print num;

def sum(arg1,arg2):
	#return the sum of two parameters
	print total1;
	total=arg1+arg2;
	print "jubu: ",total
	return total;

xs=sum(10,20);
print xs;
print total1;

#来改一下
#测试能不能