a = input('Enter text to write to the file:')
with open('sample.txt','w')as file1:
    appending_file = file1.write(a)
    print("Data successfully written to sample.txt.")
    b = input('Enter additional text to append:')
    with open('sample.txt','a')as file1:
        appending_file = file1.write("\n"+b)
        print('Data succesfully appended.')
        print("Final content of output.txt:")
        with open('sample.txt','r')as file1:
        reading_file = file1.read()
 print(reading_file)
        



