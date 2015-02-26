with open("text.txt",mode="w",encoding = "utf-8") as test_file:
    for count in range(5):
        test_file.write(input("Enter data to store in file: "))
        test_file.write("\n")
  
