from __future__ import division
# # # # # # tup1 = ('physics', 'chemistry', 1997, 2000);
# # # # # # tup2 = (1, 2, 3, 4, 5, 6, 7 );
# # # # #
# # # # # # myVar1 = "myfirstAnswerIs: ", tup1[0]
# # # # #
# # # # # # myVar2 = "my2ndAnswerIs: ", tup2[1:5]
# # # # # #
# # # # # ##
# # # # # # tup1 = (12, 34.56);
# # # # # # tup2 = ('abc', 'xyz');
# # # # # #
# # # # # # # Following action is not valid for tuples
# # # # # # # tup1[0] = 100;
# # # # # #
# # # # # # # So let's create a new tuple as follows
# # # # # # tup3 = tup1 + tup2;
# # # # # # print tup3
# # # # # #
# # # # # # tup = ('physics', 'chemistry', 1997, 2000);
# # # # # #
# # # # # # print tup
# # # # # # del tup;
# # # # # # print "After deleting tup : "
# # # # # # print tup
# # # # # #
# # # # # #
# # # # #
# # # # #
# # # # #
# # # # # print 'abc', -4.24e93, 18+6.6j, 'xyz'
# # # # # x, y = 1, 2;
# # # # # print "Value of x , y : ", x,y
# # # #
# # # #
# # # # tuple1, tuple2 = (123, 'xyz', 'zara'), (456, 'abc')
# # # #
# # # # print "First tuple length : ", len(tuple1)
# # # # print "Second tuple length : ", len(tuple2)
# # # #
# # #
# # #
# # #
# # # aList = [123, 'xyz', 'zara', 'abc'];
# # # aTuple = tuple(aList)
# # #
# # # print "Tuple elements : ", aTuple
# # #
# # #
# # # aList = [123, 557, 222, 4];
# # # newvar = min(aList)
# # # print 0
# # #
# # #
# #
# #
# # # going to Dic. from above Tuples ^^^^^^^^^^^^^^^^^^^^^^^
# #
# #
# #
# # dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First', 'Saturn': 'Old Man'}
# #
# # print "vvvvvvvv ", dict['Saturn']
#
# dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
# dictorig = dict
# dict3 = dict
#
# dict3['Age'] = 8; # update existing entry
# dict3['School'] = "DPS School"; # Add new entry
#
#
#
# dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
#
# # del dict['Name']; # remove entry with key 'Name'
# # dict.clear();     # remove all entries in dict
# # del dict ;        # delete entire dictionary
#
#
#
# myvar = len(dict)

import time;  # This is required to include time module.

# ticks = time.time()
# print "Number of ticks since 12:00am, January 1, 1970:", ticks

# print 0
# localtime = time.localtime(time.time())
# print "Local current time :", localtime
# print 1



#
# # this is setup code: Function definition is here
# def myPrintFunction( mystr ):
#    print mystr
#    mynewvar = mystr[3:7]
#    return mynewvar
#
# # Program starts here    Now you can call printme function
# newvar = myPrintFunction("aaabbbccc");
# newvar = myPrintFunction("dddeeefff")


# first command: printme (mystr="aaabbbccc")
# print value of mystr to console
# all done go to next command
# 2nd command: printtme (mystr="dddeeefff")
# print new value of mystr to console
#
# # Function definition is here
# def changeme( intmylist ):
#    "This changes a passed list into this function"
#    intmylist.append([1,2,3,4]);
#    print "Values inside the function: ", intmylist
#    return
#
# # Now you can call changeme function
# extmylist = [10,20,30];
# changeme( extmylist );
# print "Values outside the function: ", extmylist
#
#
#

#
# # Function definition is here
# def changeme( intmylist ):
#    "This changes a passed list into this function"
#    print 0
#    intmylist = [1,2,3,4]; # This would assig new reference in mylist
#    print "Values inside the function: ", intmylist
#    return
#
# def fff():
#     print 0
#
#
# # Now you can call changeme function
# mylist = [10,20,30];
# changeme( mylist );
# print "Values outside the function: ", mylist



# # Function definition is here
# def printme( str ):
#    "This prints a passed string into this function"
#    print str
#    return;
#
#
#
# # Now you can call printme function
# printme("HI")


# # Function definition is here
# def printme( intstr ):
#    "This prints a passed string into this function"
#    print intstr
#    # return;
#
# # Now you can call printme function
# printme( intstr = "a string")

# # Function definition is here
# def printinfo( name, age ):
#    "This prints a passed info into this function"
#    print "Name: ", name
#    print "Age ", age
#    return;
#
# # Now you can call printinfo function
# printinfo( age=50, name="miki" )

#
# def printinfo( name, age = 35 ):
#    "This prints a passed info into this function"
#    print "Name: ", name
#    print "Age ", age
#    return;
#
# # Now you can call printinfo function
# printinfo( age=50, name="miki" )
# printinfo( name="miki" )

#
#
#
# # Function definition is here
#
# def ShawnsFunc  ( name, age = 35 ):
#    "This prints a passed info into this function"
#    print "Name: ", name
#    print "Age ", age
#    return;
#
# # Now you can call printinfo function
# ShawnsFunc( age=50, name="miki" )
# ShawnsFunc( name="miki" )



#
#
# myglob = 2
# nancyIsMyGal = "nancyIsMyGal"
#
# def addEmUp( arg1, arg2 ):
#     # global myglob
#     myanswer = arg1 + arg2
#     mydiv = arg1 / arg2
#     print nancyIsMyGal
#     print myglob
#     myMulti = arg1 * arg2
#     return myanswer, mydiv, myMulti;
#
#
# myNewVar, myNewdiv, myMultiNew = addEmUp(2, 3)
#
#
# print "herez my answer"
# print "myNewVar equals ", myNewVar
# print "myNewdiv equals ", myNewdiv
# print "myMultiNew equals", myMultiNew
# print "nancy Is My Gal and lives in Santa Clara"
#
#








#
#
# def closet():
#     towels = 5
#     washcloth = 6
#
#     return towels, washcloth;
#
# mytowels, mywashclothes = closet()
#
# print "herez whatz in my closet", mytowels,  "towels and", mywashclothes, "washclothes"
#
#


# again but different:: whatz in garage--how many cars and how many hammers


def garage(arg1, arg2):
    cars = 1, 2, 3
    hammers = 6, 4, 5
    return cars[arg1], hammers[arg2];

def garagechange():
    var1 = 0
    var2 = 0
    while var1 < 3:
        loccar, lochammer = garage(var1, var2)
        print "What is in garage currently", loccar, "cars and ", lochammer, "hammers"
        var1 += 1
        var2 += 1

garagechange()






print 0

















