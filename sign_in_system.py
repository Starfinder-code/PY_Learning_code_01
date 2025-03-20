class PassPort:
    def __init__(self,name,password):
        self.name = name
        self.password = password
        self.trytim = 0
        
    def chg_nam(self,new_nam):
        if new_nam != self.name:
            self.name = new_nam
        else:
            print("deny!")
            
    def sign_in(self):
        while self.trytim <= 4:
            inpu = input("input your password! ")
            if inpu == self.password:
                print("welcome")
                break
            else:
                self.trytim += 1
                print(f"deny!,and only {5 - self.trytim} times to try!")
                
    def chg_pas(self,new_pas):
        if new_pas != self.password:
            self.password = new_pas
        else:
            print("deny!")
    
Hubowen = PassPort("hubowen", "123456")     #sign up for a new user!

while 1>0:
    print("welcome to this system")
    serve_choose = input("choose the serve: 1 for sign in. 2 for change password. 3 for change name\n")
    serve_choose = int(serve_choose)
    
    if serve_choose == 1:
        Hubowen.sign_in()
    elif serve_choose == 2:
        new_pass = input("please put in your new password!")
        Hubowen.chg_pas(new_pass)
    elif serve_choose == 3:
        new_name = input("please put in your new password!")
        Hubowen.chg_nam(new_name)
    else:
        print("wrong input,QUIT!")
        break
    