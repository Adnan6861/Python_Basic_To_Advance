class Hostel:
 def __init__(self):  # constractor
   self.students={}
   self.room_avb=[101,102,103,104,105,106,107,108,109,110]
def room_check(self):
    room=int(input('Enter the Room Number 101--110:'))
    if room in self.room_avb:
        print(f"Room is Free:{room}")
    else:
        print('Sorry! Room ara Not Free')
def add_student(self):
    student_idx=int(input('Enter Student Id'))
    if student_idx in self.students:
        print('Already Existed')
        return
    try:
        name=input('Enter Your Name:')
        age=int(input('Enter Your Age:'))
        contact=int(input('Enter Your Contact:'))
        data={
            'studnet_idx':student_idx,
            'name':name,
            'contact':contact,
            'age':age,
            'room':
        }
    except Exception as e:
        print(f"Print error {[e]}")
        
        

   
            
                                 
        