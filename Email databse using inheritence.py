from tkinter import*
root=Tk()
root.title("User Database")
root.geometry('500x300')

label1=Label(root,text="User Name:")
label1.place(relx=0.35,rely=0.2,anchor=CENTER)
user_name_input=Entry(root)
user_name_input.place(relx=0.6,rely=0.2,anchor=CENTER)

label2=Label(root,text="User Email:")
label2.place(relx=0.35,rely=0.3,anchor=CENTER)
user_email_input=Entry(root)
user_email_input.place(relx=0.6,rely=0.3,anchor=CENTER)

data_l=Label(root)
data_l.place(relx=0.5,rely=0.5,anchor=CENTER)
dictionary={}
class Users():

    def add_user(key,value):
        global dictionary
        dictionary[key]=value
        data_l['text']=dictionary
        user_name_input.delete(0, 'end')
        user_email_input.delete(0, 'end')
        
class Get_Users(Users):

    def getting_user(self):
        user_name=user_name_input.get()
        user_email=user_email_input.get()
        Users.add_user(user_name,user_email)
    
obj_user=Get_Users()
btn_user=Button(root,text="Add User",command=obj_user.getting_user)
btn_user.place(relx=0.5,rely=0.7,anchor=CENTER)

root.mainloop()