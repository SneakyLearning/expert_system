import MySQLdb
db = MySQLdb.connect('localhost','root','wang+-*/','Welding',charset='utf8')
cursor = db.cursor()



def get():
    material1 = input('input material1')
    material2 = input('input material2')
    thickness = int(eval(input('input thickness')))
    return material1,material2,thickness
material1,material2,thickness = get()

from rules import rules
meathod,chamfer,current,voltage,gas = rules(material1,material2,thickness)

#print(meathod,chamfer,current,voltage,gas)
sql = "insert into weld values (3,\'"+material1+'\',\''+material2+'\',\''+meathod+'\',\''+chamfer+'\',\''+str(thickness)+'\',\''+str(current)+'\',\''+str(voltage)+'\',\''+gas+'\');'
cursor.execute(sql)
db.commit()
select = "select * from weld;"
cursor.execute(select)
result = cursor.fetchall()
print(result)
db.close()