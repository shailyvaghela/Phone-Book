import sys
import csv
def add(i):
    with open('data.csv','a',newline='') as file:
        writer=csv.writer(file)
        writer.writerow(i)

#add(['urv','1234','urv@gmail.com'])
#add(['urv1','123','urv@gmail.com'])
#add(['urv2','12','urv@gmail.com'])
def view():
    data=[]
    with open('data.csv') as file:
        read=csv.reader(file)
        for row in read:
            data.append(row)
    print(data)
    return data
#view()

def remove(i):
    def save(j):
        with open('data.csv','w',newline='') as file:
            writer=csv.writer(file)
            writer.writerows(j)

    new_list=[]
    number=i

    with open('data.csv','r') as file:
        read =csv.reader(file)
        for row in read:
            new_list.append(row)

            for element in row:
                if element == number:
                    new_list.remove(row)
    save(new_list)

#remove('1234')
#view()

def update(i):
    def update_newlist(j):
        with open('data.csv','w',newline='') as file:
            writer=csv.writer(file)
            writer.writerows(j)
    new_list=[]
    number=i[0]

    with open('data.csv','r') as file:
        reader=csv.reader(file)
        for row in reader:
            new_list.append(row)
            for element in row:
                if element == number:
                    name=i[1]
                    number=i[2]
                    email=i[3]
                    data=[name,number,email]
                    index=new_list.index(row)
                    new_list[index]=data
    update_newlist(new_list)
#sample=['123','patel','123','patel@gmail.com']
#update(sample)
def search(i):
    data=[]
    number=i

    with open('data.csv','r') as file:
        reader=csv.reader(file)
        for row in reader:
            for element in row:
                if element == number:
                    data.append(row)
    print(data)           
    return data

search('12')



