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

print 0
localtime = time.localtime(time.time())
print "Local current time :", localtime
print 1

print 0
