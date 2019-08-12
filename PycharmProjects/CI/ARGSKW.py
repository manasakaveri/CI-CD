def student (name, age,**marks):
    print("name: ",name)
    print('age',age)
    print ('marks',marks)

    for key,value in marks.items():
        print(key,'',value)

student('Raghu', 42, english=100,math=99 ,Infosecurity=98 ,Data=90)
