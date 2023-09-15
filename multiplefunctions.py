class allfunctions():
    def subfields():
        print("sub-fields in AI are:")
        subfields='Machine Learning','Neural Networks','Vision','Robotics','Speech Processing','Natural Language Processing'
        for i in subfields:
            print(i)
        return subfields
    
    def oddeven():
        num=int(input('enter your number:'))
        if((num%2)==1):
            print(num,"number is odd")
            message=num,'number is odd'
        else:
            print(num,'number is even')
            message=num,'number is even'
            return message
        
    def eligible():
        gender=input("enter your gender:")
        age=int(input('enter your age:'))
        if ((age>=21 and gender=="male") or (age>=18 and gender=="female")):
            print("eligible")
            send="eligible"
        else:
            print('not eligible')
            send='not eligible'
            return send
        
        
    def percentage():
        sub1=int(input('subject1:'))
        sub2=int(input('subject2:'))
        sub3=int(input('subject3:'))
        sub4=int(input('subject4:'))
        sub5=int(input('subject5:'))
        totel=sub1+sub2+sub3+sub4+sub5
        print('Totel:',totel)
        percentage=(totel/500)*100
        print('percentage:',percentage)
    
    
    def triangle():
        height=int(input('enter height of triangle:'))
        breadth=int(input('enter breadth of triangle:'))
        area=height*breadth*(1/2)
        print('area of triangle:',area)
        side1=int(input("enter side1 of triangle:"))
        side2=int(input("enter side2 of triangle:"))
        side3=int(input("enter side3 of triangle:"))
        perimeter=side1+side2+side3
        print("perimeter of triangle:",perimeter)
    