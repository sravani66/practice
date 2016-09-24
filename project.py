from flask import Flask
from mongoengine import connect
app=Flask(__name__)

#connect('project', host='192.168.99.100', port=27017)      no o/p
 #connect('project1', username='webapp', password='pwd123')   no o/p
connect('project1', host='mongodb://192.168.99.100/ramya')      #no o/p
#connect( nabcame='test', username='user', password='12345', host='mongodb://admin:qwerty@localhost/production' )
@app.route('/attend')
def abc():
    return "hi user"
if __name__ =='__main__':    
     app.run(debug=True)    