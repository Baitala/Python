import pupil as p

pupil1 = p.pupil ()
pupil2 = p.pupil ()

pupil1_mark = int(input("Enter current mark of the pupil1: "))
pupil1.set_mark(pupil1_mark)
print("Last mark is", pupil1.marks)

pupil1_mark = int(input("Enter current mark of the pupil1: "))
pupil1.set_mark(pupil1_mark)
print("Last mark is", pupil1.marks)
print("Pupil1 average mark is", pupil1.average_mark())