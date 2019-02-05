import glob
myPath = '*'
def printLevel(temppath):
    for name in glob.glob(temppath):
        if "." in name:
            if ".mdd" in name:
                print(" // opis!!", end="")
                
            # print("geeks", end =" ") 
            # print(""+ name)
            print("", end="")
        else:
            print(""+ name)
            printLevel(name + '\\*')
            #print(" "+ name) # ┤└

print('SPIS ISTOTNYCH FOLDEROW')
printLevel(myPath)

# for space in range(len(z1[:z3])):
#     print(' ', end="")
# print(z3)
# print(z4)
# printLevel(myPath)





# print(z1)
# z2 = z1[:z1.rfind('\\')]
# print(z2)
# z3 = z2[:z2.rfind('\\')]
# print(z3)
# for space in range(len(z3)):
#     print(' ', end="")
# for space in range(len(z1[len(z3):len(z2)])):
#     print('─', end="")
# print(z1[len(z2):], end="")

# def printSpaceDash(temppath):
#     print(temppath)
#     print(temppath.rfind('\\'))
#     # temppath = temppath.replace('\\','^',temppath.rfind('\\'))
#     temppath[temppath.rfind('\\')] = '^'
#     print(temppath.rfind('\\'))
#         # temppath[name.rfind('\\')]='?'
#     for space in range(temppath.rfind('\\')):
#             print(' ', end="")
#     for dash in range(temppath.rfind('^')):
#             print('─', end="")
#     print(temppath)





# # import glob
# # for name in glob.glob('*'):
# #     print(name)

# import glob
# # myPath = 'C:\\Workspace\\task'
# myPath = '*'
# # myPathTemp = myPath + '\\*'

# # def deepGenerator(deep)
# #     tempstring = "\t"

# def printSpaceDash(temppath):
#     # temppath = temppath.replace('\\','^',temppath.rfind('\\'))
#     print(temppath.rfind('\\'))
#     temppath = temppath.replace('\\','^',temppath.rfind('\\'))
#     print(temppath.rfind('\\'))
#         # temppath[name.rfind('\\')]='?'
#     for space in range(temppath.rfind('\\')):
#             print(' ', end="")
#     for dash in range(temppath.rfind('^')):
#             print('─', end="")


# def printLevel(temppath):
#     for name in glob.glob(temppath):
#         printSpaceDash(temppath)
#         #ile jest liter do ostatniego \

#         if "." in name:
#             # print("geeks", end =" ") 
#             print(" "+ name[name.rfind('\\'):])
#         else:
#             print(" "+ name[name.rfind('\\'):])
#             #print(" "+ name) # ┤└
#             printLevel(name + '\\*')



# print('SPIS FOLDEROW')
# import sys
# print("The Python version is %s.%s.%s" % sys.version_info[:3])
# printLevel(myPath)
# # print('.', end=" ")
# # print('.', end=" ")
# # print('.', end=" ")
# # print('.', end=" ")

# # print('Named explicitly:')
# # # for name in glob.glob('*'):
# # for name in glob.glob(myPathTemp):
# #     print ('\t', name)
# #     if "." in name:
# #         print("plik")
# #     else:
# #         print("folder")


# # myPathTemp += '\\*'
# # print('Named with wildcard:')
# # for name in glob.glob(myPathTemp):
# # # for name in glob.glob('*/*'):
# #     print ('\t', name)


# # print ('\t', myPath)
