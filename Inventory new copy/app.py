from flask import Flask,render_template,request,redirect,session
from flaskext.mysql import MySQL
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import emoji
import re
mysql = MySQL()


app = Flask(__name__)
app.secret_key="hello"
app.config['MYSQL_DATABASE_USER']='QF53HUUBsI'
app.config['MYSQL_DATABASE_PASSWORD']='qPbAANR3I3'
app.config['MYSQL_DATABASE_DB']='QF53HUUBsI'
app.config['MYSQL_DATABASE_HOST']='remotemysql.com'

mysql.init_app(app)
@app.route('/')
def root():
   return redirect('/home')


@app.route("/home")
def home():
    return render_template('home.html')



@app.route("/admin",methods=['GET','POST'])
def admin():
    if request.method=="POST":
        username1=request.form['username']
        session['username']  = username1
        password=request.form['password']
        conn=mysql.connect()
        cur=conn.cursor()
        cur.execute("select `password`,`email` from `adminregister` WHERE `name`=%s",(username1))
        data=cur.fetchall()
        email= data[0][1]
        session['email']=email
        
        
        if password==data[0][0]:
            return redirect('/view')
        else:
            return " admin login failed"

    else:

        return render_template('admin.html')


    
@app.route("/adminregister",methods=['GET','POST'])

def adminregister():
    msg = ''
    if request.method == 'POST' :
        username1=request.form['fname']
        password1=request.form['pass']
        EmailID=request.form['emailid']
        session['username']  = username1
        session['email']  = EmailID
        conn=mysql.connect()
        cur=conn.cursor()
        cur.execute('SELECT * FROM adminregister WHERE name = % s', (username1, ))
        account = cur.fetchone()
        print(account)
        if account:
            msg = 'Account already exists! please Login or try to register with different username'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', EmailID):
            msg = 'Invalid email address !'
        elif not re.match(r'[A-Za-z0-9]+', username1):
            msg = 'name must contain only characters and numbers !'
        else:
            cur.execute("INSERT INTO `adminregister`(`name`, `password`, `email`) VALUES(%s,%s,%s)",(username1,password1,EmailID))
            conn.commit()
            msg = 'You have successfully registered !'
            return redirect('/view')
            
    elif request.method == 'POST':
        msg = 'Please fill out the form !'
    return render_template('adminregister.html', msg = msg)

@app.route("/add",methods=['GET','POST'])
def add():
    if request.method=="POST":
        un=request.form['un']
        pn=request.form['pn']
        pd=request.form['pd']
        pr=request.form['pr']
        pq=request.form['pq']
        location=request.form['lo']
        unit=request.form['unit']
        session['username']  = un
        conn=mysql.connect()
        cur=conn.cursor()
        cur.execute("INSERT INTO `product`(`username`,`productname`, `productdesc`,`location`, `price`, `avlqty`,`units`) VALUES(%s,%s,%s,%s,%s,%s,%s)",(un,pn,pd,location,pr,pq,unit))
        conn.commit()
        
        
        return redirect('view')

    else:
        
        return render_template('view.html')
        
        
        
    



@app.route("/userbuy",methods=['GET','POST'])
def userbuy():
    conn=mysql.connect()
    cur=conn.cursor()
    cur.execute("SELECT `productid`, `productname`, `productdesc`, `price`, `units`, `avlqty` FROM `product` where username=%s" ,(session['username'],))
    data=cur.fetchall()
    
    return render_template('userbuy.html',data=data)

        



@app.route("/buy")
def buy():
    conn=mysql.connect()
    cur=conn.cursor()
    cur.execute("select * from userbuy")
    data=cur.fetchall()

    return render_template('buy.html',data=data)






@app.route("/edit",methods=['GET','POST'])
def edit():
    if request.method=="POST":
        
        id=request.form['id']
        productname=request.form['productname']
        productdesc=request.form['productdesc']
        price=request.form['price']
        avlqty=request.form['qty']
        unit=request.form['unit']

        conn=mysql.connect()
        cur=conn.cursor()
        cur.execute("UPDATE `product` SET  `productname`='"+productname+"',`productdesc`='"+productdesc+"',`price`='"+price+"',`units`='"+unit+"',`avlqty`='"+avlqty+"' WHERE `productid`='"+id+"'")
        conn.commit()
        return redirect('view')
    else:
        id=request.args.get('id')
        conn=mysql.connect()
        cur=conn.cursor()
        cur.execute("select * from product where `productid`='"+str(id)+"'")
        data=cur.fetchone()
        return render_template('edit.html',product=data)



@app.route("/editcart",methods=['GET','POST'])
def editcart():
        if request.method=="POST":
            id=request.form['id']
            productname=request.form['productname']
            productdesc=request.form['productdesc']
            price=request.form['price']
            
            qty=request.form['qty']
            
            conn=mysql.connect()
            cur=conn.cursor()
            cur.execute("select `avlqty` from `product` WHERE `productid`=%s",(id))
            data=cur.fetchall()
    
            try:
            
                if float(qty)>float(data[0][0]):
                    return "not available"
       
                elif float(qty)<float(data[0][0]):
                  
                   price=request.form['price']
                   qty=request.form['qty']
                   total=str(float(price)*float(qty))
    
               
                   resu=str(float(data[0][0])-float(qty))
                   cur.execute("select `username` from `product` where name=%s",(session['username'],))
                   abc=cur.fetchall()
                   
    
                   session['username']=abc[0][0]
                   cur.execute("INSERT INTO `cart`(`productid`,`username`,`productname`, `productdesc`, `price`, `qty`,`total`,`avlqty`) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",(id,str(abc[0][0]),productname,productdesc,price,qty,total,resu))
                   cur.execute("INSERT INTO `track`(`productname`, `productdesc`, `price`, `qty`,`total`,`avlqty`) VALUES(%s,%s,%s,%s,%s,%s)",(productname,productdesc,price,qty,total,resu))
                  
                   conn.commit()
                   
                   cur.execute("UPDATE `product` SET `avlqty`='"+resu+"' WHERE `productid`=%s",(id))
                   conn.commit()
                   
                   return redirect('cart')
                else:
                    price=request.form['price']
                    qty=request.form['qty']
                    total=str(float(price)*float(qty))
                    
                    
                    resu=str(float(data[0][0])-float(qty))
                    cur.execute("select `username` from `product` where name=%s",(session['username'],))
                    abc=cur.fetchall()
                   
    
                    session['username']=abc[0][0]
                    cur.execute("INSERT INTO `cart`(`productid`,`username`,`productname`, `productdesc`, `price`, `qty`,`total`,`avlqty`) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",(id,str(abc[0][0]),productname,productdesc,price,qty,total,resu))
                    cur.execute("INSERT INTO `track`(`productname`, `productdesc`, `price`, `qty`,`total`,`avlqty`) VALUES(%s,%s,%s,%s,%s,%s)",(productname,productdesc,price,qty,total,resu))
                  
                    conn.commit()
                    cur.execute("UPDATE `product` SET `avlqty`='"+resu+"' WHERE `productid`=%s",(id))
                    conn.commit()
                    return redirect('cart')
                    
    
                    
            except Exception as e:
                    return emoji.emojize('please enter valid number:pouting_face:')
           
               
            
            
           
            
            

        else:
            
            id=request.args.get('id')
            conn=mysql.connect()
            cur=conn.cursor()
            cur.execute("SELECT `productid`, `productname`, `productdesc`, `price`, `units`, `avlqty` FROM `product` where `productid`='"+str(id)+"'")
            data=cur.fetchone()
            return render_template('editcart.html',product=data)
        
        
@app.route("/shipping",methods=['GET','POST'])
def shipping():
    

           
           
           
    
            conn=mysql.connect()
            cur=conn.cursor()
           
            cur.execute(" select sum(total) from cart")
            grand=cur.fetchall()
            threshold=10.0
            if float(grand[0][0])>=threshold:
               
                from flask import session
                cur.execute("SELECT `avlqty` from product where username=%s" ,(session['username'],))
                data=cur.fetchall()
                
                
                length=int(len(data))
                for i in range(length):
                    if float(data[i][0])==0:
                        
                        from flask import session
                        
                        
                        mail_content = "IT SEEMS ONE OR MORE PRODUCT QUANTITY IS/ARE NO LONGER AVAILABLE IN YOUR STORE.PLEASE LOGIN TO YOUR INVENTORY MANAGEMENT ACCOUNT AND CHECK THE QUANTITY OF ALL THE PRODUCTS AND UPDATE IT SOON..."
                                    
                                    #The mail addresses and password
                        sender_address = 'hegde1317@gmail.com'
                        sender_pass = '123456789Appu'
                        receiver_address =session['email']
                        
                                        #Setup the MIME
                        message = MIMEMultipart()
                        message['From'] = sender_address
                        message['To'] = receiver_address
                        message['Subject'] = 'ALERT MESSAGE TO RETAILERS'   #The subject line
                                        #The body and the attachments for the mail
                        message.attach(MIMEText(mail_content, 'plain'))
                                        #Create SMTP session for sending the mail
                        session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
                        session.starttls() #enable security
                        session.login(sender_address, sender_pass) #login with mail_id and password
                        text = message.as_string()
                        session.sendmail(sender_address, receiver_address, text)
                        session.quit()
                        length=length-1
                        return redirect('thank')
                return redirect('thank')
            
                
            
            else:
                return "cart cost must be greater then 10 for shipping"
                

        



        

@app.route("/delete",methods=['GET','POST'])
def delete():
    id=request.args.get('id')
    conn=mysql.connect()
    cur=conn.cursor()
    cur.execute("DELETE FROM `product` WHERE `productid`='"+id+"'")
    conn.commit()
    return redirect('view')

@app.route("/deletecart",methods=['GET','POST'])
def deletecart():
    id=request.args.get('id')
    conn=mysql.connect()
    cur=conn.cursor()
   
    cur.execute("select `qty` from `cart` WHERE `productid`=%s",(id))
    data=cur.fetchall()
    cur.execute("select `avlqty` from `cart` WHERE `productid`=%s",(id))
    data1=cur.fetchall()
    cur.execute("DELETE FROM `cart` WHERE `productid`='"+id+"'")
    conn.commit()
    
    result=str(float(data[0][0])+float(data1[0][0]))
    cur.execute("UPDATE `product` SET `avlqty`='"+result+"' WHERE `productid`=%s",(id))
               

    conn.commit()
    
    
    
   
    return redirect('cart')
    

@app.route("/deletetrack",methods=['GET','POST'])
def deletetrack():
    id=request.args.get('id')
    conn=mysql.connect()
    cur=conn.cursor()
   
   
    cur.execute("DELETE FROM `track` WHERE `productid`='"+id+"'")
    conn.commit()
    
    
    
    
    
   
    return redirect('track')
    

  

   
    
    
    
   

@app.route("/view",methods=['GET','POST'])
def view():
    conn=mysql.connect()
    cur=conn.cursor()
    
    cur.execute("SELECT `productid`, `productname`, `productdesc`,`location`, `price`, `units`, `avlqty` FROM `product` where username=%s" ,(session['username'],))
    data=cur.fetchall()
    cur.execute("SELECT `name` FROM `adminregister` where name=%s" ,(session['username'],))
    name=cur.fetchall()
    
    
    
    return render_template('view.html',data=data,name=name)


@app.route("/track",methods=['GET','POST'])
def track():
    conn=mysql.connect()
    cur=conn.cursor()
    cur.execute("SELECT * from track" )
    data=cur.fetchall()

    return render_template('track.html',data=data)




@app.route("/cart")
def cart():
    conn=mysql.connect()
    cur=conn.cursor()
    cur.execute("SELECT * from cart where username=%s" ,(session['username'],))
    data=cur.fetchall()
    
   
    
    
    
    conn.commit()
    
    
    
    

    return render_template('cart.html',data=data)




@app.route("/total")
def total():
    conn=mysql.connect()
    cur=conn.cursor()
    
    cur.execute(" select sum(total) from cart")
    data=cur.fetchall()
    
    
    
    conn.commit()
    return render_template('shipping.html',data=data)


@app.route("/tracktotal",methods=['GET','POST'])
def tracktotal():
    if request.method=="POST":
        conn=mysql.connect()
        cur=conn.cursor()
        date=request.form['date']
        cur.execute(" select  sum(total),sum(qty) from track")
        data=cur.fetchall()
        cur.execute("select `username` from product where username=%s",(session['username'],))
        abc=cur.fetchall()
    
        session['username']=abc[0][0]
        
        cur.execute("INSERT INTO `history`(`username`,`date`,`totalqty`,`totalprice`) VALUES(%s,%s,%s,%s)",(str(abc[0][0]),date,str(data[0][0]),str(data[0][1])))
        
        
        
        conn.commit()
        return render_template('tracktotal.html',data=data)
        
        
    else:
        return render_template('tracktotal.html',data=data)



@app.route("/stock")
def stock():
    conn=mysql.connect()
    cur=conn.cursor()
    cur.execute("SELECT `productid`, `productname`, `productdesc`, `price`, `units`, `avlqty` FROM `product` where username=%s" ,(session['username'],))
    data=cur.fetchall()

    return render_template('stock.html',data=data)



@app.route("/help")
def help():
    return render_template('help.html')

@app.route("/thank")
def thank():
    conn=mysql.connect()
    cur=conn.cursor()

    cur.execute("delete from cart")
    conn.commit()
    return render_template('thank.html')
    
@app.route("/history")
def history():
    conn=mysql.connect()
    cur=conn.cursor()
    
    cur.execute("select * from history where username=%s" ,(session['username'],))
    data=cur.fetchall()
    conn.commit()      
        
            
                             
        
   
    
    return render_template('history.html',data=data)
@app.route("/clearhistory")
def clearhistory():
    conn=mysql.connect()
    cur=conn.cursor()
    
    cur.execute("delete from history where username=%s" ,(session['username'],))
    data=cur.fetchall()
    conn.commit()      
        
            
                             
        
   
    
    return render_template('history.html',data=data)
@app.route("/logout")
def logout():
    conn=mysql.connect()
    cur=conn.cursor()
    cur.execute("delete from cart")
    cur.execute("delete from track")
    conn.commit()
    session.pop("username",None)
    
        
        
            
                             
        
   
    
    return render_template('home.html')

if __name__=="__main__":
    app.run(host='0.0.0.0',debug = True, port = 5000)