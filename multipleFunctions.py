class multipleFunctions():
    def Subfields():
        listSubfields=["Machine Learning","Neural Networks","Neural Networks","Robotics","Speech Processing","Natural Language Processing"]
        print("Sub-fields in AI are:")
        for subfields in listSubfields:
            print(subfields)

    def OddEven():
        num=int(input("Enter a number:"))
        if(num%2==1):
            print(num,"is Odd number")
        else:
            print(num,"is Even number")

    def Eligible():
        gender=(input("Your Gender:"))
        age=int(input("Your Age:"))
        if (gender=="Male"):
            if(age>20):
                print("ELIGIBLE")
            else:
                print("NOT ELIGIBLE")
        elif (gender=="Female"):
            if(age>17):
                print("ELIGIBLE")
            else:
                print("NOT ELIGIBLE")

    def percentage():
        sub1=int(input("Subject1:"))
        sub2=int(input("Subject2:"))
        sub3=int(input("Subject3:"))
        sub4=int(input("Subject4:"))
        sub5=int(input("Subject5:"))
        total=sub1+sub2+sub3+sub4+sub5
        percentage=(total/500)*100
        print("Total :", total)
        print("Percentage :",percentage)

    def triangle():
        height=int(input("Height:"))
        breadth=int(input("Breadth:"))
        print("Area formula: (Height*Breadth)/2")
        area=(height*breadth)/2
        print("Area of Triangle:",area)
        height1=int(input("Height1:"))
        height2=int(input("Height2:"))
        breadth=int(input("Breadth:"))
        print("Perimeter formula: Height1+Height2+Breadth")
        perimeter=(height1+height2+breadth)
        print("Perimeter of Triangle:",perimeter)

