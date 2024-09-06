#Data for the game
data_list = [
    {'name': 'John Doe', 'number':  4567, 'job': 'Software Engineer'},
    {'name': 'Jane Smith', 'number': 5678, 'job': 'Data Scientist'},
    {'name': 'Emily Johnson', 'number': 6789, 'job': 'Graphic Designer'},
    {'name': 'Michael Brown', 'number': 7890, 'job': 'Marketing Manager'},
    {'name': 'Sarah Davis', 'number': 8901, 'job': 'Product Manager'},
    {'name': 'James Wilson', 'number': 9012, 'job': 'Financial Analyst'},
    {'name': 'Linda Clark', 'number': 1234, 'job': 'HR Specialist'},
    {'name': 'David Lee', 'number': 2345, 'job': 'Operations Manager'},
    {'name': 'Sophia Martinez', 'number': 3456, 'job': 'Sales Executive'},
    {'name': 'Daniel Thomas', 'number': 4567, 'job': 'Customer Support Specialist'},
    {'name': 'Olivia Anderson', 'number': 5678, 'job': 'Business Consultant'},
    {'name': 'Matthew Taylor', 'number': 6789, 'job': 'Research Scientist'},
    {'name': 'Ava Jackson', 'number': 7890, 'job': 'Content Writer'},
    {'name': 'Ethan White', 'number': 8901, 'job': 'Web Developer'},
    {'name': 'Mia Harris', 'number': 9012, 'job': 'Event Planner'},
    {'name': 'Lucas Martin', 'number': 1234, 'job': 'UI/UX Designer'},
    {'name': 'Charlotte Thompson', 'number': 2345, 'job': 'Project Coordinator'},
    {'name': 'Liam Garcia', 'number': 3456, 'job': 'Network Administrator'},
    {'name': 'Isabella Robinson', 'number': 4567, 'job': 'Supply Chain Manager'},
    {'name': 'Noah Walker', 'number': 5678, 'job': 'Legal Advisor'},
    {'name': 'Emma Young', 'number': 6789, 'job': 'Education Specialist'},
    {'name': 'Benjamin Scott', 'number': 7890, 'job': 'Product Designer'},
    {'name': 'Avery Adams', 'number': 8901, 'job': 'Digital Marketer'},
    {'name': 'Mason Nelson', 'number': 9012, 'job': 'IT Consultant'},
    {'name': 'Harper Carter', 'number': 1234, 'job': 'Biomedical Engineer'},
    {'name': 'Alexander Mitchell', 'number': 2345, 'job': 'Strategic Planner'},
    {'name': 'Ella Perez', 'number': 3456, 'job': 'Graphic Artist'},
    {'name': 'Jackson Roberts', 'number': 4567, 'job': 'Sales Manager'},
    {'name': 'Lily Hall', 'number': 5678, 'job': 'Executive Assistant'},
    {'name': 'Sebastian King', 'number': 6789, 'job': 'Architect'},
    {'name': 'Aria Turner', 'number': 7890, 'job': 'Data Analyst'},
    {'name': 'Owen Lewis', 'number': 8901, 'job': 'Business Development Manager'},
    {'name': 'Evelyn Walker', 'number': 9012, 'job': 'Technical Writer'},
    {'name': 'William Allen', 'number': 1234, 'job': 'Customer Success Manager'},
    {'name': 'Chloe Young', 'number': 2345, 'job': 'Public Relations Specialist'},
    {'name': 'James Hernandez', 'number': 3456, 'job': 'Systems Analyst'},
    {'name': 'Mila Ramirez', 'number': 4567, 'job': 'Product Marketing Manager'},
    {'name': 'Henry Carter', 'number': 5678, 'job': 'Database Administrator'},
    {'name': 'Amelia Clark', 'number': 6789, 'job': 'Training Coordinator'},
    {'name': 'Logan Scott', 'number': 7890, 'job': 'E-commerce Specialist'},
    {'name': 'Madison Lee', 'number': 8901, 'job': 'Creative Director'},
    {'name': 'Elijah Evans', 'number': 9012, 'job': 'Business Intelligence Analyst'},
    {'name': 'Zoe Murphy', 'number': 1234, 'job': 'Healthcare Administrator'},
    {'name': 'Jacob Martinez', 'number': 2345, 'job': 'Construction Manager'},
    {'name': 'Natalie Wright', 'number': 3456, 'job': 'Insurance Agent'},
    {'name': 'Matthew Lewis', 'number': 4567, 'job': 'Retail Manager'},
    {'name': 'Lillian Johnson', 'number': 5678, 'job': 'Software Tester'},
    {'name': 'Eli Hall', 'number': 6789, 'job': 'Operations Analyst'},
    {'name': 'Hannah Green', 'number': 7890, 'job': 'Content Strategist'},
    {'name': 'Jackson Mitchell', 'number': 8901, 'job': 'Creative Writer'},
    {'name': 'Ella Allen', 'number': 9012, 'job': 'Marketing Coordinator'},
    {'name': 'Gabriel Taylor', 'number': 1234, 'job': 'Risk Manager'},
    {'name': 'Grace Adams', 'number': 2345, 'job': 'Customer Insights Analyst'},
    {'name': 'Aiden Johnson', 'number': 3456, 'job': 'Legal Consultant'},
    {'name': 'Zara Williams', 'number': 4567, 'job': 'Clinical Research Coordinator'},
    {'name': 'Daniel Harris', 'number': 5678, 'job': 'Mobile App Developer'},
    {'name': 'Riley Brown', 'number': 6789, 'job': 'Brand Strategist'},
    {'name': 'Victoria Walker', 'number': 7890, 'job': 'Social Media Manager'},
    {'name': 'James White', 'number': 8901, 'job': 'Public Affairs Specialist'},
    {'name': 'Sofia Davis', 'number': 9012, 'job': 'Operations Director'}
]


#pick two data randomly
import random
cha=random.choice(data_list)
chb=random.choice(data_list)
print("Higher or lower?")


# a loop to make the user play until he make mistake
tr=1
while(tr>0):
    #make sure a not equal to b
    test=True
    while test:
        if(cha==chb):
            cha=random.choice(data_list)
            chb=random.choice(data_list)

        elif(cha!=chb):
            break
        
    print(f" A is {cha['name']}, {cha['job']}")
    print(f" B is {chb['name']}, {chb['job']}")
    i=input(f"Who have higher number of followrs? a or b?:").lower()
    
    if(i=='a' and cha['number']>chb['number']):
        cha=random.choice(data_list)
        chb=random.choice(data_list)
        
    elif(i=='b' and chb['number']>cha['number']):
        cha=random.choice(data_list)
        chb=random.choice(data_list)
        
    else:
        print("Game Over")
        break
     
