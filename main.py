import os

def create_project(website_name):
    f = open("index.html", "a")
    f.write("<!--Website created with Webz Builder-->\n<!--https://github.com/nottimnik/webz-builder-->\n\n<title>"+website_name+"</title>\n")
    
def clear():
    os.system("clear")

def add_objects(website_name):
    f = open("index.html", "a")
    print("What do you want to add to the website:")
    print("1. A header")
    print("2. A paragraph")
    print("3. A link")
    print("4. A Image")
    print("5. Exit")

    choice_objects = int(input())

    clear()

    #Header
    if(choice_objects==1):
        print("Enter the size of the Header:")
        print("1. H1 - Huge Header")
        print("2. H2 - Very Big Header")
        print("3. H3 - Big Header")
        print("4. H4 - Normal Header")
        print("5. H5 - Small Header")
        print("6. H6 - Very Small Header")
        print("\nEnter:",end="")

        size = int(input())

        if(size < 7 and size > 0):
            clear()
            print("Enter the content of the Header")
            print("Enter:", end="")
            content = str(input())
            f.write("<h"+str(size)+">"+content+"</h"+str(size)+">"+"\n")
        else:
            while(size > 6 or size < 1):
                clear()

                print("Invalid Input:" + str(size)+" !")
                print("Enter the size of the Header:")
                print("1. H1 - Huge Header")
                print("2. H2 - Very Big Header")
                print("3. H3 - Big Header")
                print("4. H4 - Normal Header")
                print("5. H5 - Small Header")
                print("6. H6 - Very Small Header")
                print("\nEnter:",end="")

                size = int(input())    

            clear()
            print("Enter the content of the Header")
            print("Enter:", end="")
            content = str(input())
            f.write("<h"+str(size)+">"+content+"</h"+str(size)+">"+"\n")

    #Paragraph
    elif(choice_objects==2):
        print("Enter the content of the Paragraph")
        print("Enter:", end="")
        content = str(input())
        f.write("<p>"+content+"</p>\n")
    elif(choice_objects==3):
        print("Enter the link:")
        print("Enter:", end="")
        link = str(input())

        clear()

        print("Enter the content of the link:")
        print("Enter:", end="")
        content = str(input())
        f.write(f"<a href=\"{link}\">{content}</a>\n")

    elif(choice_objects==4):
        print("Enter the link to the image or the path of the image:")
        print("Enter:", end="")
        img = str(input())

        clear()

        print("Enter the content of the height:")
        print('Enter \"default\" to use the default height.')
        print("Enter:", end="")
        height = str(input())

        print("Enter the content of the width:")
        print('Enter \"default\" to use the default width.')
        print("Enter:", end="")
        width = str(input())

        f.write(f"<img src=\"{img}\" width=\"")
        if(width=="default"):
            f.write("")
        else:
            f.write(f"{width}")
        f.write("\" height=\"")

        if(height=="default"):
            f.write("")
        else:
            f.write(f"{height}")
        f.write("\">\n")
    elif(choice_objects==5):
        return False
    else:
        print("Invalid Input!")


print("Welcome to Webz Builder v1.0")
print("Menu:")
print("1. Create Website")
print("\nEnter:",end="")

choice = int(input())

if(choice==1):
    print("Enter the name of the website:", end="")
    website_name = str(input())

    create_project(website_name)

    running = True

    while(running == True):
        clear()
        running = add_objects(website_name)

else: #Inavlid Choice Handling
    while(choice!=1):
        clear()
        print("Invalid Input:" + str(choice) + "\n")
        print("Welcome to Webz Builder v1.0")
        print("Menu:")
        print("1. Create Website")
        print("\nEnter:",end="")
