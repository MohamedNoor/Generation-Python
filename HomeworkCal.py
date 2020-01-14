#calculate program student ict grade

def Student(name,homework,assesment,final_exam):
      final_homework= int(homework/25 * 100 )
      final_assesment= int(assesment/50 * 100)
      final_ICT= int(final_exam/100 * 100)
      average= round((final_homework + final_assesment + final_ICT)/3)
      
      if average >= 80:
            print(name,"A")
      elif average < 80 and average>= 70:
            print(name,"B")
      elif average < 70 and average>= 60:
            print(name,"c")
      elif average < 60 and average>= 50:
            print(name,"d")
      elif average < 50 and average>= 40:
            print(name,"e")
      else:
            print(name," you have failed in life")    



def Student2(name,homework,assesment,final_exam):
      final_homework= int(homework/25 * 25 )
      final_assesment= int(assesment/50 * 35)
      final_ICT= int(final_exam/100 * 40)
      average= round((final_homework + final_assesment + final_ICT))
      
      if average >= 80:
            print(name,"your score is A you have achieve", average,"%")
      elif average < 80 and average>= 70:
            print(name,"your score is B you have achieve", average,"%")
      elif average < 70 and average>= 60:
            print(name,"your score is C you have achieve", average,"%")
      elif average < 60 and average>= 50:
            print(name,"your score is D you have achieve", average,"%")
      elif average < 50 and average>= 40:
            print(name,"your score is E you have achieve", average,"%")
      else:
            print(name," you have achieve below and E\nYour score",average) 
Student2("jo",0,0,65)
Student2("paul",20,30,33)
Student2("luke",25,50,33)